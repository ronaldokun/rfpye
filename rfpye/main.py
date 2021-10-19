# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_main.ipynb (unless otherwise specified).

__all__ = ['BTYPES', 'FILTER_ATTRS', 'parse_path', 'extract_bin_data', 'BTYPES', 'FILTER_ATTRS', 'parse_path',
           'extract_bin_data']

# Cell
from datetime import datetime
from typing import Union, Iterable
import os

from fastcore.basics import typed
from fastcore.xtras import Path
from fastcore.xtras import is_listy
from fastcore.foundation import L
import numpy as np
import pandas as pd

from rich import print
from loguru import logger
from .utils import *
from .constants import SPECTRAL_BLOCKS, console
from .parser import parse_bin, export_metadata

BTYPES = [21, 40] + SPECTRAL_BLOCKS
FILTER_ATTRS = {21: ['hostname', 'method'],
                40: ['altitude', 'latitude', 'longitude'],
                63: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                67: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                68: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega']}

# Internal Cell
logger.add("rfpye.log", rotation="1 week", compression='zip', backtrace=True, diagnose=True)

# Cell
def parse_path(path: Union[list, str])->Iterable:
    if is_listy(path):
        return [f for f in L(path).map(Path) if f.is_file() and f.suffix == '.bin']
    if isinstance(path, (str, Path)):
        path = Path(path)
        if path.is_file() and path.suffix == '.bin':
                return [path]
        elif path.is_dir():
            return get_files(path, extensions=[".bin"])
    raise ValueError(f"Caminho de Entrada inválido: {path}. Insira um caminho para uma pasta, um arquivo ou lista de arquivos")

# Cell
@logger.catch
def extract_bin_data(
    path: Union[list, str],
    meta_attrs: Iterable = None,
    spec_data: bool = False,
    spec_dtype: str = "float16",

) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        path (str): Arquivo ou Lista de Arquivos .bin | Caminho para a Pasta
        spec_data (bool, optional): Retornar dados de Espectro?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """
    lista_bins = parse_path(path)

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

    output = []
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
from typing import Union, Iterable
import os

from fastcore.basics import typed
from fastcore.xtras import Path
from fastcore.xtras import is_listy
from fastcore.foundation import L
import numpy as np
import pandas as pd

from rich import print
from loguru import logger
from .utils import *
from .constants import SPECTRAL_BLOCKS, console
from .parser import parse_bin, export_metadata

BTYPES = [21, 40] + SPECTRAL_BLOCKS
FILTER_ATTRS = {21: ['hostname', 'method'],
                40: ['altitude', 'latitude', 'longitude'],
                63: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                67: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega'],
                68: ['wallclock_datetime', 'sample', 'minimum', 'ndata', 'processing', 'bw', 'unit', 'description', 'start_mega', 'stop_mega']}

# Internal Cell
logger.add("rfpye.log", rotation="1 week", compression='zip', backtrace=True, diagnose=True)

# Cell
def parse_path(path: Union[list, str])->Iterable:
    if is_listy(path):
        return [f for f in L(path).map(Path) if f.is_file() and f.suffix == '.bin']
    if isinstance(path, (str, Path)):
        path = Path(path)
        if path.is_file() and path.suffix == '.bin':
                return [path]
        elif path.is_dir():
            return get_files(path, extensions=[".bin"])
    raise ValueError(f"Caminho de Entrada inválido: {path}. Insira um caminho para uma pasta, um arquivo ou lista de arquivos")

# Cell
@logger.catch
def extract_bin_data(
    path: Union[list, str],
    meta_attrs: Iterable = None,
    spec_data: bool = False,
    spec_dtype: str = "float16",

) -> None:
    """Recebe uma pasta ou arquivo bin, processa e salva os metadados e espectro na saida.

    Args:
        path (str): Arquivo ou Lista de Arquivos .bin | Caminho para a Pasta
        spec_data (bool, optional): Retornar dados de Espectro?. Defaults to False.
        dtype (str, optional): Tipo de dados a salvar o espectro. Defaults to "float16".
    """
    lista_bins = parse_path(path)

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

    output = []
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