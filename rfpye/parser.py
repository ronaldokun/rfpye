# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_parser.ipynb (unless otherwise specified).

__all__ = ['parse_bin', 'classify_blocks', 'extract_level', 'meta_from_blocks', 'export_metadata', 'export_level']

# Internal Cell
import os
from pathlib import Path
from typing import *
from datetime import datetime
from collections import defaultdict
from fastcore.basics import uniqueify, partialler, listify
from fastcore.utils import parallel
from fastcore.foundation import L
from rich.progress import track
from .blocks import *
from .utils import *
from .constants import *
from .cyparser import cy_extract_compressed
import pandas as pd
import numpy as np

path_type = Union[str, Any]
bin_val = Union[int, bytes]
bytes_encoded = Union[int, bytes]
datetime_object = datetime

# Cell
def parse_bin(
    bin_file: Union[str, Path],
    btypes: Iterable = MAIN_BLOCKS.keys(),
    slice_: slice = None,
    bytes_header: int = BYTES_HEADER,
    marker: bytes = ENDMARKER,
) -> dict:
    """Receives a CRFS binfile and return a dictionary with its different blocks:


    Args:
        bin_file (Union[str, Path]): path to the bin file
        btypes (Iterable, optional): Restrict processing to only these block types. Defaults to MAIN_BLOCKS.keys().
        slice_ (slice, optional): Slice to cut the bin file if desired. Defaults to None.
        bytes_header (int, optional): File Header Size. Defaults to BYTES_HEADER.
        marker (bytes, optional): Byte marker delimiting the end of one block. Defaults to ENDMARKER.

    Returns:
        [type]: Dictionary with the bin_file version and dictionary of the different blocks.
    """

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
        #         "string": bin2str(header[4:]),
        "blocks": classify_blocks(body.split(marker), btypes=btypes),
    }

# Cell
def classify_blocks(
    blocks: Iterable, btypes: Iterable = MAIN_BLOCKS.keys()
) -> Mapping[Tuple, Tuple]:
    """Receives an iterable L with binary blocks and returns a defaultdict with a tuple (block types, thread_id) as keys and a list of the Class Blocks as values
    :param file: A string or pathlib.Path like path to a `.bin`file generated by CFRS - Logger
    :return: A Dictionary with block types as keys and a list of the Class Blocks available as values
    """
    map_block: Mapping[Tuple, L] = defaultdict(L)
    btypes = listify(btypes)
#     index = BYTES_HEADER
    for block in blocks:
        if block == b'': continue
        checksum = np.frombuffer(block[-4:], dtype=np.uint32).item()
        calculated_checksum = np.frombuffer(block[:-4], dtype=np.uint8).sum().astype(np.uint32).item()
        if calculated_checksum != checksum: continue
        bloco_base = create_base_block(block, checksum)
        btype, btid = bloco_base.type, bloco_base.thread_id
#         stop = index + DATA_BLOCK_HEADER + len(bloco_base.data) + CHECKSUM
        if btype not in btypes:
            #             index = stop + LEN_MARKER
            continue
        bloco = block_constructor(btype, bloco_base)
        if btype in SPECTRAL_BLOCKS:
            gerror = getattr(bloco, "gerror", 0)
            if gerror != -1:
                continue
#                index = stop + LEN_MARKER
        if btype == GPS_BLOCK and not getattr(bloco, "gps_status"):
            continue  # equals to zero

        map_block[(btype, btid)].append(bloco)
#         index = stop + LEN_MARKER
    return map_block

# Internal Cell
def _extract_uncompressed(
    blocks: Iterable, rows: int, cols: int, min_level: float, dtype=np.float16
):
    levels = np.full((rows, cols), min_level, dtype=dtype)
    block_data = "raw_data" if dtype == np.uint8 else "block_data"
    for b, block in enumerate(blocks):
        levels[b] = getattr(block, block_data)
    return levels

# Cell
def extract_level(spectrum_blocks: L, dtype=np.float32) -> pd.DataFrame:
    """Receives a mapping `spectrum_blocks` and returns the Matrix with the Levels as values, Frequencies as columns and Block Number as index.
    :param pivoted: If False, optionally returns an unpivoted version of the Matrix
    """
    assert len(spectrum_blocks), 'The spectrum block list is empty'
#     spectrum_blocks = spectrum_blocks.itemgot(1)
    block = spectrum_blocks[0]
    assert block.type in (
        63,
        64,
        67,
        68,
    ), 'The input blocks are not spectral blocks'

    rows = len(spectrum_blocks)
    cols = min(len(block.data[block.start:block.stop]), block.ndata)
    min_level = 0 if dtype == np.uint8 else block.offset - 127.5
    if block.type in (63, 67):
#         frequencies = getattr(block, "frequencies")
        return _extract_uncompressed(spectrum_blocks, rows, cols, min_level, dtype)
    thresh = block.thresh - 1
    block_data = [b.raw_data for b in spectrum_blocks]
#         frequencies = np.linspace(block.start_mega, block.stop_mega, num=cols)
    levels = cy_extract_compressed(block_data, rows, cols, thresh, min_level)
    if dtype != np.float32:
        levels = levels.astype(dtype)
    return levels

# Internal Cell
def meta2df(meta_list: Iterable, optimize: bool = True) -> pd.DataFrame:
    """Receives and Iterable `metalist` with metadata and converts it to a DataFrame"""
    df = pd.DataFrame(meta_list)
    dt_features = ["wallclock_datetime"] if "wallclock_datetime" in df.columns else []
    if optimize:
        df = df_optimize(df, dt_features)
    if dt_features:
        df = df.set_index("wallclock_datetime")
    return df

# Internal Cell
def rowattrs(row, attrs):
    return {
        **{"start_byte": row[0][0], "stop_byte": row[0][1]},
        **getattrs(row[1], attrs),
    }

# Cell
def meta_from_blocks(blocks: L, attrs: list = None) -> pd.DataFrame:
    """Receives a list of blocks, extracts the metadata from them and return a DataFrame"""
    func = partialler(getattrs, attrs=attrs)
    return meta2df(blocks.map(func))

# Internal Cell
def _export_metadata(
    parsed_blocks: tuple,
    filter_attrs: Union[None, dict] = None,
    to_save: bool = False,
    bin_name: Union[str, os.PathLike] = None,
    outfolder: Union[str, os.PathLike] = None,
    extension: str = ".csv",
) -> Union[None, pd.DataFrame]:

    (tipo, tid), blocos = parsed_blocks
    if filter_attrs is None:
        attrs = None
    elif isinstance(filter_attrs, dict):
        attrs = filter_attrs.get(tipo)
    else:
        raise ValueError(
            f"Formato desconhecido do argumento {filter_attrs}:{type(filter_attrs)}, é esperado um dicionário"
        )
    meta = meta_from_blocks(blocos, attrs)
    if to_save:
        dt_features = isinstance(meta.index, pd.DatetimeIndex)
        name = f"{bin_name}-B_{tipo}_TId_{tid}"
        if extension == ".csv":
            meta.to_csv(Path(outfolder) / f"{name}{extension}", index=bool(dt_features))
        elif extension == ".xlsx":
            meta.to_excel(
                Path(outfolder) / f"{name}{extension}", index=bool(dt_features)
            )
        elif extension == ".fth":
            meta.to_feather(Path(outfolder) / f"{name}{extension}")
        else:
            raise ValueError(f"Extension {extension} not implemented")
    return (tipo, tid), meta

# Cell
def export_metadata(
    blocks: dict,
    filter_attrs: Union[None, dict] = None,
    to_save: bool = False,
    bin_name: Union[str, Path] = None,
    outfolder: Union[str, Path] = None,
    extension: str = ".csv",
) -> None:
    if not isinstance(blocks, dict):
        raise TypeError(
            f"It's expected the argument {blocks} to be a mapping (block type, thread_id) : List of Blocks"
        )

    func = partialler(
        _export_metadata,
        filter_attrs=filter_attrs,
        to_save=to_save,
        bin_name=bin_name,
        outfolder=outfolder,
        extension=extension,
    )
    func.__module__ = _export_metadata.__module__
    return dict(
        parallel(
        func, list(blocks.items()), n_workers=os.cpu_count()
        )
    )

# Internal Cell
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

    name = f"{stem}-B_{tipo}_TId_{tid}"
    if ext == ".fth":
        if index is not None:
            level = level.reset_index()
        level.columns = [str(c) for c in level.columns]
        level.to_feather(f"{saida}/{name}{ext}")
    else:
        raise ValueError(f"Extension {ext} not implemented")

# Cell
def export_level(
    stem: Union[str, Path],
    blocks: dict,
    saida: Union[str, Path],
    ext: str = ".fth",
    index: pd.DatetimeIndex = None,
    dtype: Union[str, np.dtype] = np.float16,
) -> None:

    blocks = [((t, i), b) for (t, i), b in blocks.items() if t in SPECTRAL_BLOCKS]
    if not index:
        index = [None] * len(blocks)
    items = list(zip(blocks, index))
    func = partialler(_export_level, stem=stem, saida=saida, ext=ext, dtype=dtype)
    func.__module__ = _export_meta.__module__
    parallel(func, items, n_workers=os.cpu_count())