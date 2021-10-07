# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_main.ipynb (unless otherwise specified).

__all__ = ['BTYPES', 'FILTER_ATTRS', 'CACHE_FOLDER', 'log', 'custom_theme', 'console', 'filter_spectrum', 'process_bin',
           'extract_bin_data', 'extract_bin_stats', 'BTYPES', 'FILTER_ATTRS', 'filter_spectrum', 'extract_bin_data',
           'BTYPES', 'FILTER_ATTRS', 'filter_spectrum', 'extract_bin_data']

# Cell
from datetime import datetime
from typing import *
import os
import logging
from fastcore.xtras import Path
from fastcore.script import call_parse, Param, store_true
from fastcore.basics import listify
from fastcore.foundation import L
import numpy as np
import pandas as pd
from rich.progress import Progress
from rich.console import Console
from rich.theme import Theme
from rich.logging import RichHandler
from rich import print
# from fire import Fire
from .utils import *
from .constants import SPECTRAL_BLOCKS
from .parser import *

BTYPES = [21, 40, 63, 67, 68]
FILTER_ATTRS = {21: ['hostname', 'method'],
                40: ['altitude', 'latitude', 'longitude'],
                63: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'start_mega', 'stop_mega'],
                67: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                68: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega']}

CACHE_FOLDER = Path.cwd() / ".cache"

# Cell
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("rich")

# Cell
custom_theme = Theme({"info": "dim cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)

# Cell
def filter_spectrum(
    df: pd.DataFrame,
    time_start: str = None,
    time_stop: str = None,
    freq_start: str = None,
    freq_stop: str = None,
) -> pd.DataFrame:
    """Recebe o arquivo de espectro df e retorna de acordo com os filtros

    Args:
        df (pd.DataFrame): Arquivo de espectro. Timestamp como linhas e frequências como colunas
        time_start (str): Timestamp de início. Se None filtra desde o início do arquivo
        time_stop (str): Timestamp de fim. Se None filtra até o fim do arquivo
        freq_start (str): Filtro inicial de frequência. Se None retorna desde a menor frequências
        freq_stop (str): Filtro Final de frequência. Se None retorna até a maior frequência.

    Returns:
        pd.DataFrame: DataFrame com Frequência, min, max e mean após os filtros aplicados.
    """
    df = df.copy()
    if time_start is None:
        time_start = "01/01/2000"
    if time_stop is None:
        time_stop = "31/12/2100"
    try:
        time_start = pd.to_datetime(time_start)
        time_stop = pd.to_datetime(time_stop)
    except pd.errors.ParserError:
        log.error(
            f"[bold red blink] Datas inválidas! Verifique as strings de data {freq_start} e {freq_stop}"
        )

    try:
        df.set_index("index", inplace=True)
        df.index = pd.to_datetime(df.index)
    except pd.errors.KeyError:
        if not isinstance(df.index, pd.DatetimeIndex):
            log.warning(
                f"Não foi passado uma coluna ou índice com datetime a ser filtrado, todas as linhas serão processadas",
                exc_info=True,
            )
            time_start = 0
            time_stop = df.shape[0]

    cols = df.columns.values.astype("float")
    rows = df.index.values

    if freq_start is None:
        freq_start = 0
    if freq_stop is None:
        freq_stop = np.inf

    filtered_cols = df.columns[(float(freq_start) <= cols) & (cols <= float(freq_stop))]
    filtered_rows = df.index[(time_start <= rows) & (rows <= time_stop)]
    if len(filtered_cols) == 0 or len(filtered_rows) == 0:
        return None
    count = filtered_rows.shape[0]
    array = df.loc[filtered_rows, filtered_cols].values
    freq = filtered_cols.values.astype("float32")
    min_ = array.min(axis=0)
    max_ = array.max(axis=0)
    mean = array.mean(axis=0)
    return pd.DataFrame(
        {"Frequency": freq, "Min": min_, "Max": max_, "Mean": mean, "Count": count}
    )

# Internal Cell
def read_meta(filename):
    ext = filename.suffix
    if ext == ".csv":
        df = pd.read_csv(filename)
    elif ext == ".xlsx":
        df = pd.read_excel(filename, engine="openpyxl")
    elif ext == ".fth":
        df = pd.read_feather(filename)
        if "wallclock_datetime" in df.columns:
            df.set_index("wallclock_datetime", inplace=True)
    else:
        raise ValueError(f"Extension {ext} not implemented")
    return df

# Cell
def process_bin(
    entrada: str,
    saida: str,
    recursivo: bool = False,
    pastas: Iterable[str] = None,
    levels: bool = False,
    substituir: bool = False,
    dtype: str = "float16",
) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        entrada (str): Caminho para a Pasta ou Arquivo .bin
        saida (str): Pasta onde salvar os arquivos processados
        recursivo (bool, optional): Buscar os arquivos de entrada recursivamente. Defaults to False.
        pastas (Iterable[str], optional): Limitar a busca a essas pastas. Defaults to None.
        levels (bool, optional): Extrair e salvar os dados de espectro. Defaults to False.
        substituir (bool, optional): Reprocessar arquivos já processados?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """

    entrada = Path(entrada)
    if entrada.is_file():
        lista_bins = [entrada]
    else:
        lista_bins = get_files(
            entrada, extensions=[".bin"], recurse=recursivo, folders=pastas
        )
    parsed_bins = {}
    meta_path = Path(f"{saida}/meta")
    levels_path = Path(f"{saida}/levels")
    meta_path.mkdir(exist_ok=True, parents=True)
    levels_path.mkdir(exist_ok=True, parents=True)
    log_meta = Path(f"{saida}/log_meta.txt")
    log_levels = Path(f"{saida}/log_levels.txt")
    if substituir:
        done_meta = set()
        done_levels = set()
    else:

        done_meta = (
            set(log_meta.read_text().split("\n")) if log_meta.exists() else set()
        )
        done_levels = (
            set(log_levels.read_text().split("\n")) if log_levels.exists() else set()
        )

    console.rule("Lista de Arquivos a serem processados", style="bold red")
    console.print(
        [f.name for f in lista_bins],
        style="bold white",
        overflow="fold",
        justify="left",
    )
    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo .bin a processar :zzz:")
        return

    if not levels:
        lista_bins = [f for f in lista_bins if f.name not in done_meta]
    else:
        lista_bins = [f for f in lista_bins if f.name not in done_levels]

    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo novo a processar :zzz:")
        console.print(
            ":point_up: use --substituir no terminal ou substituir=True na chamada caso queira reprocessar os bins e sobrepôr os arquivos existentes :wink:"
        )
        return

    try:

        with Progress(transient=True, auto_refresh=False) as progress:
            bins = progress.track(
                lista_bins,
                total=len(lista_bins),
                description="[green]Processando Blocos Binários",
            )

            for file in bins:
                progress.console.print(f"[cyan]Processando Blocos de: [red]{file.name}")
                parsed_bins[file.name] = parse_bin(file)
                progress.refresh()

            lista_meta = [(k, v) for k, v in parsed_bins.items() if k not in done_meta]

            if lista_meta:
                blocks = progress.track(
                    lista_meta,
                    total=len(lista_meta),
                    description="[cyan]Exportando Metadados",
                )
                for filename, block_dict in blocks:
                    progress.console.print(f"[cyan]Extraindo Metadados de: [red]{file}")
                    export_metadata(filename, block_dict, meta_path, ext=".fth")
                    done_meta.add(file)
                    progress.refresh()
            if levels:
                lista_levels = lista_meta = [
                    (k, v) for k, v in parsed_bins.items() if k not in done_levels
                ]
                if lista_levels:
                    bins = progress.track(
                        lista_levels,
                        total=len(lista_levels),
                        description="[grey]Exportando Dados de Espectro",
                    )
                    for file, block_obj in bins:
                        progress.console.print(
                            f"[grey]Extraindo Espectro de: [red]{file}"
                        )
                        meta_index = []
                        blocks = block_obj["blocks"]
                        for (tipo, tid) in blocks.keys():
                            if tipo not in SPECTRAL_BLOCKS:
                                continue
                            meta_file = Path(
                                f"{meta_path}/{file}-B_{tipo}_TId_{tid}.fth"
                            )
                            if not meta_file.exists():
                                export_meta(
                                    file,
                                    block_obj,
                                    meta_path,
                                    ext=".fth",
                                )
                                done_meta.add(file)
                            meta_df = read_meta(meta_file)
                            meta_index.append(meta_df.index.tolist())
                        export_level(
                            file,
                            block_obj,
                            levels_path,
                            ext=".fth",
                            index=meta_index,
                            dtype=dtype,
                        )
                        done_levels.add(file)
                        progress.refresh()
        console.print("kbô :satisfied:")
    finally:
        log_meta.write_text("\n".join(sorted(list(done_meta))))
        log_levels.write_text("\n".join(sorted(list(done_levels))))

# Cell
def extract_bin_data(
    path: str,
    save_path: str = None,
    spec_data: bool = False,
    dtype: str = "float16",
) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        path (str): Caminho para a Pasta ou Arquivo .bin
        saida (str): Pasta onde salvar os arquivos processados
        recursivo (bool, optional): Buscar os arquivos de entrada recursivamente. Defaults to False.
        pastas (Iterable[str], optional): Limitar a busca a essas pastas. Defaults to None.
        substituir (bool, optional): Reprocessar arquivos já processados?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """

    path = Path(path)
    if path.is_file():
        lista_bins = [path]
    elif path.is_dir():
        lista_bins = get_files(
            path, extensions=[".bin"])
    else:
        raise ValueError(f"Caminho de Entrada inválido: {path}. Insira um caminho para uma pasta ou arquivo")

    parsed_bins = {}
    if save_path is not None:
        save_path = Path(save_path)
        save_path.mkdir(exist_ok=True, parents=True)
        log = Path(f"{save_path}/logger.txt")
        if substituir:
            done = set()
        else:

            done = (
                set(log.read_text().split("\n")) if log.exists() else set()
            )

    else:
        done = set()

    console.rule("Lista de Arquivos a serem processados", style="bold red")
    console.print(
        [f.name for f in lista_bins],
        style="bold white",
        overflow="fold",
        justify="left",
    )
    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo .bin a processar :zzz:")
        return

    lista_bins = [f for f in lista_bins if f.name not in done]

    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo novo a processar :zzz:")
        console.print(
            ":point_up: use --substituir no terminal ou substituir=True na chamada caso queira reprocessar os bins e sobrepôr os arquivos existentes :wink:"
        )
        return

    output = dict()
    for file in lista_bins:
        console.print(f"[green]Processando Blocos de: [red]{file.name}")
        parsed_bin = parse_bin(file, btypes=BTYPES)
        file_version, blocks = parsed_bin.values()
        metadata = export_metadata(blocks, filter_attrs=FILTER_ATTRS)
        out = dict()
        out['File_Name'] = file.name
        out['File_Version'] = file_version
        out['File_Type'] = 'RFEye Logger Trace'
        out['Device'] = 'Rfeye Node'
        out['Fluxos'] = dict()
        for (btype, tid), df in metadata.items():
            if btype == 21:
                out['Equipment_ID'] = df.hostname.item()
                out['Script_Version'] = df.method.item()
            elif btype == 40:
                out['Latitude'] = df.latitude.median()
                out['Longitude'] = df.longitude.median()
                out['Altitude'] = df.altitude.median()
                out['Count_GPS'] = df.shape[0]
                out['Sum_Latitude']  = df.latitude.sum()
                out['Sum_Longitude'] = df.longitude.sum()
            elif btype == 67:
                timestamp = df.index.values
                level = dict()
                level['Initial_Time'] = timestamp.min()
                level['Sample_Duration'] = df['sample'].median()
                fluxo = df.drop(['minimum', 'sample'], axis=1).iloc[0]
                level['Description'] = fluxo.description
                level['Start_Frequency'] = fluxo.start_mega
                level['Stop_Frequency'] = fluxo.stop_mega
                level['Trace_Type'] = fluxo.processing
                level['RBW'] = fluxo.bw
                level['Level_Units'] = fluxo.unit
                level['Num_Traces'] = df.shape[0]
                level['Vector_Length'] = fluxo.ndata
                level['Timestamp'] = timestamp
                if spec_data:
                    if save_path:
                        level['Minimum_Level'] = df.minimum.values.astype('float16')
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=np.uint8)
                    else:
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=dtype)

                out['Fluxos'][(btype, tid)] =  level
        done.add(file.name)
        output[file.name] = out

    if save_path:
        log.write_text("\n".join(sorted(list(done))))
    return output

# Internal Cell
def appended_mean(df: pd.Series) -> float:
    """Recebe um agrupamento do DataFrame e retorna sua média ponderada pela coluna Count

    Args:
        df (pd.DataFrame): Groupby do DataFrame

    Returns:
        float: Média Ponderada da linha pela coluna Count
    """
    return (df["Count"] * df["Mean"]).sum() / df["Count"].sum()

# Cell
def extract_bin_stats(
    filename: str,
    time_start: str = None,
    time_stop: str = None,
    freq_start: str = None,
    freq_stop: str = None,
    cache: str = CACHE_FOLDER,
) -> pd.DataFrame:
    """Recebe o caminho para um arquivo CRFS bin e retorna um dataframe com o resumo estatístico dos dados de espectro

    Args:
        filename (str): Caminho para o arquivo bin
        time_start (str): Timestamp de início. Se None filtra desde o início do arquivo
        time_stop (str): Timestamp de fim. Se None filtra até o fim do arquivo
        freq_start (str): Filtro inicial de frequência. Se None retorna desde a menor frequências
        freq_stop (str): Filtro Final de frequência. Se None retorna até a maior frequência.
        cache (str, optional): Caminho para a pasta de cache. Default é criar uma pasta oculta .cache no diretório atual.

    Returns:
        pd.DataFrame: Dataframe contendo o resumo estatístico do arquivo
    """

    cache = Path(cache)
    cache.mkdir(exist_ok=True, parents=True)
    filename = Path(filename)
    if filename.is_dir():
        filenames = get_files(filename, extensions=[".bin"])
    else:
        filenames = listify(filename)

    cached_files = get_files(cache / "levels")
    files = L()
    for filename in filenames:
        while True:
            # TODO filter based on metadata
            subset = cached_files.filter(lambda name: filename.stem in str(name))
            if not len(subset):
                process_bin(entrada=filename, saida=cache, levels=True)
            else:
                break
        files += subset
        subset = L()

    dfs = files.map(pd.read_feather)
    tids = files.map(lambda x: x.stem.split("_")[-1])
    spectra = dfs.map(
        filter_spectrum,
        time_start=time_start,
        time_stop=time_stop,
        freq_start=freq_start,
        freq_stop=freq_stop,
    )
    spectra = [(i, s) for i, s in zip(tids, spectra) if s is not None]
    columns = ["Tid", "Frequency", "Min", "Max", "Mean"]
    out = pd.DataFrame(columns=columns)
    if not spectra:
        log.warning(
            f"Os parâmetros repassados não correspondem a nenhum dado espectral do arquivo",
            exc_info=True,
        )
        return out
    for i, df in spectra:
        df["Tid"] = i
    spectra = [s for i, s in spectra]
    spectra = pd.concat(spectra)
    if len(spectra.Frequency) == len(spectra.Frequency.unique()):
        return spectra[columns]
    gb = spectra.groupby(["Tid", "Frequency"])
    out = gb.apply(appended_mean)
    Min = gb.min()["Min"]
    Max = gb.max()["Max"]
    Mean = gb.apply(appended_mean)
    out = pd.concat([Min, Max, Mean], axis=1).reset_index()
    out.columns = columns
    return out

# Cell
from datetime import datetime
from typing import *
import os

from fastcore.xtras import Path
from fastcore.xtras import is_listy
from fastcore.foundation import L
import numpy as np
import pandas as pd

from rich import print
from loguru import logger
from .utils import *
from .constants import SPECTRAL_BLOCKS
from .parser import *

BTYPES = [21, 40] + SPECTRAL_BLOCKS
FILTER_ATTRS = {21: ['hostname', 'method'],
                40: ['altitude', 'latitude', 'longitude'],
                63: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                67: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                68: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega']}

# Internal Cell
logger.add("rfpye.log", rotation="1 week", compression='zip', backtrace=True, diagnose=True)

# Cell
@logger.catch
def filter_spectrum(
    df: pd.DataFrame,
    time_start: str = None,
    time_stop: str = None,
    freq_start: str = None,
    freq_stop: str = None,
) -> pd.DataFrame:
    """Recebe o arquivo de espectro df e retorna de acordo com os filtros

    Args:
        df (pd.DataFrame): Arquivo de espectro. Timestamp como linhas e frequências como colunas
        time_start (str): Timestamp de início. Se None filtra desde o início do arquivo
        time_stop (str): Timestamp de fim. Se None filtra até o fim do arquivo
        freq_start (str): Filtro inicial de frequência. Se None retorna desde a menor frequências
        freq_stop (str): Filtro Final de frequência. Se None retorna até a maior frequência.

    Returns:
        pd.DataFrame: DataFrame com Frequência, min, max e mean após os filtros aplicados.
    """
    df = df.copy()
    if time_start is None:
        time_start = "01/01/2000"
    if time_stop is None:
        time_stop = "31/12/2100"
    try:
        time_start = pd.to_datetime(time_start)
        time_stop = pd.to_datetime(time_stop)
    except pd.errors.ParserError:
        log.error(
            f"[bold red blink] Datas inválidas! Verifique as strings de data {freq_start} e {freq_stop}"
        )

    try:
        df.set_index("index", inplace=True)
        df.index = pd.to_datetime(df.index)
    except pd.errors.KeyError:
        if not isinstance(df.index, pd.DatetimeIndex):
            log.warning(
                f"Não foi passado uma coluna ou índice com datetime a ser filtrado, todas as linhas serão processadas",
                exc_info=True,
            )
            time_start = 0
            time_stop = df.shape[0]

    cols = df.columns.values.astype("float")
    rows = df.index.values

    if freq_start is None:
        freq_start = 0
    if freq_stop is None:
        freq_stop = np.inf

    filtered_cols = df.columns[(float(freq_start) <= cols) & (cols <= float(freq_stop))]
    filtered_rows = df.index[(time_start <= rows) & (rows <= time_stop)]
    if len(filtered_cols) == 0 or len(filtered_rows) == 0:
        return None
    count = filtered_rows.shape[0]
    array = df.loc[filtered_rows, filtered_cols].values
    freq = filtered_cols.values.astype("float32")
    min_ = array.min(axis=0)
    max_ = array.max(axis=0)
    mean = array.mean(axis=0)
    return pd.DataFrame(
        {"Frequency": freq, "Min": min_, "Max": max_, "Mean": mean, "Count": count}
    )

# Internal Cell
def read_meta(filename):
    ext = filename.suffix
    if ext == ".csv":
        df = pd.read_csv(filename)
    elif ext == ".xlsx":
        df = pd.read_excel(filename, engine="openpyxl")
    elif ext == ".fth":
        df = pd.read_feather(filename)
        if "wallclock_datetime" in df.columns:
            df.set_index("wallclock_datetime", inplace=True)
    else:
        raise ValueError(f"Extension {ext} not implemented")
    return df

# Cell
@logger.catch
def extract_bin_data(
    path: str,
    spec_data: bool = False,
    dtype: str = "float16",

) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        path (str): Caminho para a Pasta ou Arquivo .bin
        saida (str): Pasta onde salvar os arquivos processados
        recursivo (bool, optional): Buscar os arquivos de entrada recursivamente. Defaults to False.
        pastas (Iterable[str], optional): Limitar a busca a essas pastas. Defaults to None.
        substituir (bool, optional): Reprocessar arquivos já processados?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """
    if is_listy(path):
        lista_bins = L()
        for f in path:
            if f.is_file():
                if f.suffix == '.bin':
                    lista_bins.append(f)
                else:
                    raise TypeErrorror(f"A extensão de arquivo é inválida: {f.suffix}. Somente arquivos .bin são aceitos.")
    else:
        path = Path(path)
        if path.is_file():
            if path.suffix == '.bin':
                lista_bins = [path]
            else:
                raise TypeErrorror(f"A extensão de arquivo é inválida: {path.suffix}. Somente arquivos .bin são aceitos.")
        elif path.is_dir():
            lista_bins = get_files(
                path, extensions=[".bin"])

        else:
            raise ValueError(f"Caminho de Entrada inválido: {path}. Insira um caminho para uma pasta ou arquivo")

    console.rule("Lista de Arquivos a serem processados", style="bold red")
    console.print(
        [f.name for f in lista_bins],
        style="bold white",
        overflow="fold",
        justify="left",
    )
    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo .bin a processar :zzz:")
        return

    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo novo a processar :zzz:")
        console.print(
            ":point_up: use --substituir no terminal ou substituir=True na chamada caso queira reprocessar os bins e sobrepôr os arquivos existentes :wink:"
        )
        return

    output = dict()
    for file in lista_bins:
        console.print(f"[green]Processando Blocos de: [red]{file.name}")
        parsed_bin = parse_bin(file, btypes=BTYPES)
        file_version, blocks = parsed_bin.values()
        metadata = export_metadata(blocks, filter_attrs=FILTER_ATTRS)
        out = dict()
        out['File_Name'] = file.name
        out['File_Version'] = file_version
        out['File_Type'] = 'RFEye Logger Trace'
        out['Device'] = 'Rfeye Node'
        out['Fluxos'] = dict()
        for (btype, tid), df in metadata.items():
            if btype == 21:
                out['Equipment_ID'] = df.hostname.item()
                out['Script_Version'] = df.method.item()
            elif btype == 40:
                out['Latitude'] = df.latitude.median()
                out['Longitude'] = df.longitude.median()
                out['Altitude'] = df.altitude.median()
                out['Count_GPS'] = df.shape[0]
                out['Sum_Latitude']  = df.latitude.sum()
                out['Sum_Longitude'] = df.longitude.sum()
            elif btype in SPECTRAL_BLOCKS:
                timestamp = df.index.values
                level = dict()
                level['Initial_Time'] = timestamp.min()
                level['Sample_Duration'] = df['sample'].median()
                fluxo = df.drop(['minimum', 'sample'], axis=1).iloc[0]
                level['Description'] = fluxo.description
                level['Start_Frequency'] = fluxo.start_mega
                level['Stop_Frequency'] = fluxo.stop_mega
                level['Trace_Type'] = fluxo.processing
                level['Resolution'] = fluxo.bw
                level['Level_Units'] = fluxo.unit
                level['Num_Traces'] = df.shape[0]
                level['Vector_Length'] = fluxo.ndata
                level['Timestamp'] = timestamp
                if spec_data:
                    if save_path:
                        level['Minimum_Level'] = df.minimum.values.astype('float16')
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=np.uint8).flatten()
                    else:
                        level['Frequency'] = np.linspace(fluxo.start_mega, fluxo.stop_mega, num=fluxo.ndata)
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=dtype)
                out['Fluxos'][(btype, tid)] =  level
            else:
                print(btype)
        done.add(file.name)
        output[file.name] = out

    if save_path:
        log.write_text("\n".join(sorted(list(done))))
    return output

# Cell
from datetime import datetime
from typing import *
import os

from fastcore.xtras import Path
from fastcore.xtras import is_listy
from fastcore.foundation import L
import numpy as np
import pandas as pd

from rich import print
from loguru import logger
from .utils import *
from .constants import SPECTRAL_BLOCKS
from .parser import *

BTYPES = [21, 40] + SPECTRAL_BLOCKS
FILTER_ATTRS = {21: ['hostname', 'method'],
                40: ['altitude', 'latitude', 'longitude'],
                63: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                67: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                68: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega']}

# Internal Cell
logger.add("rfpye.log", rotation="1 week", compression='zip', backtrace=True, diagnose=True)

# Cell
@logger.catch
def filter_spectrum(
    df: pd.DataFrame,
    time_start: str = None,
    time_stop: str = None,
    freq_start: str = None,
    freq_stop: str = None,
) -> pd.DataFrame:
    """Recebe o arquivo de espectro df e retorna de acordo com os filtros

    Args:
        df (pd.DataFrame): Arquivo de espectro. Timestamp como linhas e frequências como colunas
        time_start (str): Timestamp de início. Se None filtra desde o início do arquivo
        time_stop (str): Timestamp de fim. Se None filtra até o fim do arquivo
        freq_start (str): Filtro inicial de frequência. Se None retorna desde a menor frequências
        freq_stop (str): Filtro Final de frequência. Se None retorna até a maior frequência.

    Returns:
        pd.DataFrame: DataFrame com Frequência, min, max e mean após os filtros aplicados.
    """
    df = df.copy()
    if time_start is None:
        time_start = "01/01/2000"
    if time_stop is None:
        time_stop = "31/12/2100"
    try:
        time_start = pd.to_datetime(time_start)
        time_stop = pd.to_datetime(time_stop)
    except pd.errors.ParserError:
        log.error(
            f"[bold red blink] Datas inválidas! Verifique as strings de data {freq_start} e {freq_stop}"
        )

    try:
        df.set_index("index", inplace=True)
        df.index = pd.to_datetime(df.index)
    except pd.errors.KeyError:
        if not isinstance(df.index, pd.DatetimeIndex):
            log.warning(
                f"Não foi passado uma coluna ou índice com datetime a ser filtrado, todas as linhas serão processadas",
                exc_info=True,
            )
            time_start = 0
            time_stop = df.shape[0]

    cols = df.columns.values.astype("float")
    rows = df.index.values

    if freq_start is None:
        freq_start = 0
    if freq_stop is None:
        freq_stop = np.inf

    filtered_cols = df.columns[(float(freq_start) <= cols) & (cols <= float(freq_stop))]
    filtered_rows = df.index[(time_start <= rows) & (rows <= time_stop)]
    if len(filtered_cols) == 0 or len(filtered_rows) == 0:
        return None
    count = filtered_rows.shape[0]
    array = df.loc[filtered_rows, filtered_cols].values
    freq = filtered_cols.values.astype("float32")
    min_ = array.min(axis=0)
    max_ = array.max(axis=0)
    mean = array.mean(axis=0)
    return pd.DataFrame(
        {"Frequency": freq, "Min": min_, "Max": max_, "Mean": mean, "Count": count}
    )

# Internal Cell
def read_meta(filename):
    ext = filename.suffix
    if ext == ".csv":
        df = pd.read_csv(filename)
    elif ext == ".xlsx":
        df = pd.read_excel(filename, engine="openpyxl")
    elif ext == ".fth":
        df = pd.read_feather(filename)
        if "wallclock_datetime" in df.columns:
            df.set_index("wallclock_datetime", inplace=True)
    else:
        raise ValueError(f"Extension {ext} not implemented")
    return df

# Cell
@logger.catch
def extract_bin_data(
    path: str,
    spec_data: bool = False,
    dtype: str = "float16",

) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        path (str): Caminho para a Pasta ou Arquivo .bin
        saida (str): Pasta onde salvar os arquivos processados
        recursivo (bool, optional): Buscar os arquivos de entrada recursivamente. Defaults to False.
        pastas (Iterable[str], optional): Limitar a busca a essas pastas. Defaults to None.
        substituir (bool, optional): Reprocessar arquivos já processados?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """
    if is_listy(path):
        lista_bins = L()
        for f in path:
            if f.is_file():
                if f.suffix == '.bin':
                    lista_bins.append(f)
                else:
                    raise TypeErrorror(f"A extensão de arquivo é inválida: {f.suffix}. Somente arquivos .bin são aceitos.")
    else:
        path = Path(path)
        if path.is_file():
            if path.suffix == '.bin':
                lista_bins = [path]
            else:
                raise TypeErrorror(f"A extensão de arquivo é inválida: {path.suffix}. Somente arquivos .bin são aceitos.")
        elif path.is_dir():
            lista_bins = get_files(
                path, extensions=[".bin"])

        else:
            raise ValueError(f"Caminho de Entrada inválido: {path}. Insira um caminho para uma pasta ou arquivo")

    console.rule("Lista de Arquivos a serem processados", style="bold red")
    console.print(
        [f.name for f in lista_bins],
        style="bold white",
        overflow="fold",
        justify="left",
    )
    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo .bin a processar :zzz:")
        return

    if not lista_bins:
        console.print(":sleeping: Nenhum arquivo novo a processar :zzz:")
        console.print(
            ":point_up: use --substituir no terminal ou substituir=True na chamada caso queira reprocessar os bins e sobrepôr os arquivos existentes :wink:"
        )
        return

    output = dict()
    for file in lista_bins:
        console.print(f"[green]Processando Blocos de: [red]{file.name}")
        parsed_bin = parse_bin(file, btypes=BTYPES)
        file_version, blocks = parsed_bin.values()
        metadata = export_metadata(blocks, filter_attrs=FILTER_ATTRS)
        out = dict()
        out['File_Name'] = file.name
        out['File_Version'] = file_version
        out['File_Type'] = 'RFEye Logger Trace'
        out['Device'] = 'Rfeye Node'
        out['Fluxos'] = dict()
        for (btype, tid), df in metadata.items():
            if btype == 21:
                out['Equipment_ID'] = df.hostname.item()
                out['Script_Version'] = df.method.item()
            elif btype == 40:
                out['Latitude'] = df.latitude.median()
                out['Longitude'] = df.longitude.median()
                out['Altitude'] = df.altitude.median()
                out['Count_GPS'] = df.shape[0]
                out['Sum_Latitude']  = df.latitude.sum()
                out['Sum_Longitude'] = df.longitude.sum()
            elif btype in SPECTRAL_BLOCKS:
                timestamp = df.index.values
                level = dict()
                level['Initial_Time'] = timestamp.min()
                level['Sample_Duration'] = df['sample'].median()
                fluxo = df.drop(['minimum', 'sample'], axis=1).iloc[0]
                level['Description'] = fluxo.description
                level['Start_Frequency'] = fluxo.start_mega
                level['Stop_Frequency'] = fluxo.stop_mega
                level['Trace_Type'] = fluxo.processing
                level['Resolution'] = fluxo.bw
                level['Level_Units'] = fluxo.unit
                level['Num_Traces'] = df.shape[0]
                level['Vector_Length'] = fluxo.ndata
                level['Timestamp'] = timestamp
                if spec_data:
                    if save_path:
                        level['Minimum_Level'] = df.minimum.values.astype('float16')
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=np.uint8).flatten()
                    else:
                        level['Frequency'] = np.linspace(fluxo.start_mega, fluxo.stop_mega, num=fluxo.ndata)
                        level['Level_Data'] = extract_level(blocks[(btype, tid)], dtype=dtype)
                out['Fluxos'][(btype, tid)] =  level
            else:
                print(btype)
        done.add(file.name)
        output[file.name] = out

    if save_path:
        log.write_text("\n".join(sorted(list(done))))
    return output