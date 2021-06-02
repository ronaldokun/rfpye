# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_parser.ipynb (unless otherwise specified).

__all__ = ['path_type', 'bin_val', 'bytes_encoded', 'datetime_object', 'parse_bin', 'classify_blocks', 'extract_level',
           'meta2df', 'extract_metadata', 'export_meta', 'export_level']

# Cell
# from multiprocessing import set_start_method, Pool
# try:
#     set_start_method("spawn")
# except RuntimeError:
#     pass
import os
from pathlib import Path
from typing import *
from datetime import datetime
from collections import defaultdict
from fastcore.basics import uniqueify, partialler
from fastcore.utils import parallel
from fastcore.foundation import L
from rich.progress import track
from rfpy.blocks import *
from rfpy.utils import *
from rfpy.constants import *
from rfpy.cyparser import cy_extract_compressed
import pandas as pd
import numpy as np

path_type = Union[str, Any]
bin_val = Union[int, bytes]
bytes_encoded = Union[int, bytes]
datetime_object = datetime

# Cell
def parse_bin(
    bin_file, bytes_header: int = BYTES_HEADER, marker: bytes = ENDMARKER, slice_=None
):
    with open(bin_file, mode="rb") as bfile:
        # O primeiro bloco do arquivo é o cabeçalho e tem 36 bytes de tamanho.
        header = bfile.read(bytes_header)
        body = bfile.read()
    if slice_ is not None:
        assert (
            slice_.start >= bytes_header
        ), f"The start of your slice has to be >= {bytes_header}, you passed {slice_.start} "
        body = body[slice_]
    return {
        "file_version": bin2int(header[:4]),
        "string": bin2str(header[4:]),
        "blocks": classify_blocks(body.split(marker)),
    }

# Cell
def classify_blocks(blocks: list) -> Mapping[Tuple, Tuple]:
    """Receives an iterable L with binary blocks and returns a defaultdict with a tuple (block types, thread_id) as keys and a list of the Class Blocks as values
    :param file: A string or pathlib.Path like path to a `.bin`file generated by CFRS - Logger
    :return: A Dictionary with block types as keys and a list of the Class Blocks available as values
    """
    map_block: Mapping[Tuple, L] = defaultdict(L)
    index = BYTES_HEADER
    for block in blocks:
        bloco = create_base_block(block)
        btype, btid = bloco.type, bloco.thread_id
        stop = index + DATA_BLOCK_HEADER + len(bloco.data) + CHECKSUM
        if btype not in MAIN_BLOCKS.keys():
            index = stop + LEN_MARKER
            continue
        bloco = block_constructor(btype, bloco)
        if btype in SPECTRAL_BLOCKS:
            gerror = getattr(bloco, "gerror", -1)
            if gerror != -1 or bloco._level_len != bloco.ndata:
                index = stop + LEN_MARKER
                continue

        map_block[(btype, btid)].append(
            ((index, stop), block_constructor(btype, bloco))
        )
        index = stop + LEN_MARKER
    return map_block

# Cell
def _extract_uncompressed(
    blocks: Iterable, rows: int, cols: int, min_level: float, dtype=np.float16
):
    levels = np.full((rows, cols), min_level, dtype=dtype)
    for b, block in enumerate(blocks):
        levels[b] = block.block_data
    return levels


def extract_level(spectrum_blocks: L, dtype=np.float32) -> pd.DataFrame:
    """Receives a mapping `spectrum_blocks` and returns the Matrix with the Levels as values, Frequencies as columns and Block Number as index.
    :param pivoted: If False, optionally returns an unpivoted version of the Matrix
    """
    assert len(spectrum_blocks), f"The spectrum block list is empty"
    spectrum_blocks = spectrum_blocks.itemgot(1)
    block = spectrum_blocks[0]
    assert block.type in (63, 64, 67, 68), f"The input blocks are not spectral blocks"
    rows = len(spectrum_blocks)
    min_level = block.offset - 127.5
    if block.type in (63, 67):
        cols = block.ndata
        frequencies = getattr(block, "frequencies")
        return pd.DataFrame(
            _extract_uncompressed(spectrum_blocks, rows, cols, min_level, dtype),
            columns=frequencies,
        )
    else:
        cols = block.norig
        thresh = block.thresh - 1
        block_data = [b.block_data for b in spectrum_blocks]
        frequencies = np.linspace(block.start_mega, block.stop_mega, num=cols)
        levels = cy_extract_compressed(block_data, rows, cols, thresh, min_level)
        if dtype != np.float32:
            levels = levels.astype(dtype)
        return pd.DataFrame(levels, columns=frequencies)

# Cell
def meta2df(meta_list: Iterable, optimize: bool = True) -> pd.DataFrame:
    """Receives and Iterable `metalist` with metadata and converts it to a DataFrame"""
    df = pd.DataFrame(meta_list)
    dt_features = ["wallclock_datetime"] if "wallclock_datetime" in df.columns else []
    if optimize:
        df = df_optimize(df, dt_features)
    if dt_features:
        df = df.set_index("wallclock_datetime")
    return df

# Cell
def extract_metadata(blocos: L, attrs: list = None) -> pd.DataFrame:
    """Receives a list of blocks, extracts the metadata from them and return a DataFrame"""
    df = meta2df(
        blocos.map(
            lambda item: {
                **{"start_byte": item[0][0], "stop_byte": item[0][1]},
                **getattrs(item[1], attrs),
            }
        )
    )
    return df

# Cell
def export_meta(
    stem: Union[str, Path], parsed_bin: dict, saida: Union[str, Path], ext: str = ".csv"
) -> None:

    file_version, string, blocks = parsed_bin.values()
    func = partialler(_export_meta, stem=stem, saida=saida, ext=ext)
    func.__module__ = _export_meta.__module__
    parallel(func, list(blocks.items()), n_workers=os.cpu_count(), pause=0.5)


def _export_meta(
    parsed_blocks: tuple,
    stem: Union[str, Path],
    saida: Union[str, Path],
    ext: str = ".csv",
) -> Union[None, pd.DataFrame]:

    (tipo, tid), blocos = parsed_blocks
    meta = extract_metadata(blocos)
    dt_features = isinstance(meta.index, pd.DatetimeIndex)

    #     if dt_features:
    #         start = meta.index.min().strftime("%Y%m%dT%H%M%S")
    #         end = meta.index.max().strftime("%Y%m%dT%H%M%S")
    #         name = f'{stem}-B_{tipo}_TId_{tid}-{start}_{end}'
    #     else:
    name = f"{stem}-B_{tipo}_TId_{tid}"

    if ext == ".csv":
        meta.to_csv(Path(saida) / f"{name}{ext}", index=bool(dt_features))
    elif ext == ".xlsx":
        meta.to_excel(Path(saida) / f"{name}{ext}", index=bool(dt_features))
    elif ext == ".fth":
        meta.reset_index().to_feather(Path(saida) / f"{name}{ext}")
    else:
        raise ValueError(f"Extension {ext} not implemented")

# Cell
def export_level(
    stem: Union[str, Path],
    parsed_bin: dict,
    saida: Union[str, Path],
    ext: str = ".fth",
    index: pd.DatetimeIndex = None,
    dtype: Union[str, np.dtype] = np.float16,
) -> None:

    _, _, blocks = parsed_bin.values()
    blocks = [((t, i), b) for (t, i), b in blocks.items() if t in SPECTRAL_BLOCKS]
    if not index:
        index = [None] * len(blocks)
    items = list(zip(blocks, index))
    func = partialler(_export_level, stem=stem, saida=saida, ext=ext, dtype=dtype)
    func.__module__ = _export_meta.__module__
    parallel(func, items, n_workers=os.cpu_count(), pause=0.5)


def _export_level(
    parsed_blocks: tuple,
    stem: Union[str, Path],
    saida: Union[str, Path],
    ext: str = ".fth",
    dtype: Union[str, np.dtype] = np.float16,
) -> Union[None, pd.DataFrame]:

    ((tipo, tid), blocos), index = parsed_blocks
    assert (
        tipo in SPECTRAL_BLOCKS
    ), "Tentativa de extrair espectro de um bloco que não é espectral"

    saida = Path(saida)
    level = extract_level(blocos, dtype)
    if index is not None:
        level.index = index
    dt_features = isinstance(level.index, pd.DatetimeIndex)

    name = f"{stem}-B_{tipo}_TId_{tid}"
    if ext == ".fth":
        if index is not None:
            level = level.reset_index()
        level.columns = [str(c) for c in level.columns]
        level.to_feather(f"{saida}/{name}{ext}")
    else:
        raise ValueError(f"Extension {ext} not implemented")

    # console.print(f"\nArquivo {name}{ext} exportado com sucesso!:sparkles:"