# AUTOGENERATED! DO NOT EDIT! File to edit: 01_parser.ipynb (unless otherwise specified).

__all__ = ['path_type', 'bin_val', 'bytes_encoded', 'datetime_object', 'META', 'LEVELS', 'BLOCO_40', 'BLOCO_63',
           'get_files', 'parse_bin', 'classify_blocks', 'extract_block_levels', 'export_bin_meta']

# Cell
from collections import defaultdict
from fastcore.basics import uniqueify
from fastcore.utils import parallel
from fastcore.foundation import L
from .blocks import create_base_block, block_constructor
from .utils import bin2dec, bin2str
import pandas as pd
import numpy as np
import os
from pathlib import Path
from typing import *
from datetime import datetime

path_type = Union[str, Any]
bin_val = Union[int, bytes]
bytes_encoded = Union[int, bytes]
datetime_object = datetime

META = {'Block_Number': 'uint16',
     'Latitude': 'float32',
     'Longitude': 'float32',
     'Altitude': 'float16',
     'Initial_Time': 'datetime64[ns]',
     'Sample_Duration': 'uint16',
     'Start_Frequency': 'uint32',
     'Stop_Frequency': 'uint32',
     'Vector_Length': 'uint16',
     'Trace_Type': 'category',
     'Antenna_Type': 'category',
     'Equipement_ID': 'category'}

LEVELS = {'Block_Number': 'category', 'Frequency(MHz)': 'float32', "Nivel(dBm)" : 'float16'}

BLOCO_40 = ['latitude', 'longitude', 'altitude']

BLOCO_63 = ['datetime_stamp',
            'spent_time_microsecs',
            'start_mega',
            'stop_mega',
            'data_points',
            'processing',
            'id_antenna']

# Cell
def _get_files(p, fs, extensions=None):
    p = Path(p)
    res = [p/f for f in fs if not f.startswith('.')
           and ((not extensions) or f'.{f.split(".")[-1].lower()}' in extensions)]
    return res

def get_files(path, extensions=None, recurse=True, folders=None, followlinks=True):
    "Get all the files in `path` with optional `extensions`, optionally with `recurse`, only in `folders`, if specified."
    path = Path(path)
    folders=L(folders)
    if extensions is not None:
        extensions = set(uniqueify(extensions))
        extensions = {e.lower() for e in extensions}
    if recurse:
        res = []
        for i,(p,d,f) in enumerate(os.walk(path, followlinks=followlinks)): # returns (dirpath, dirnames, filenames)
            if len(folders) !=0 and i==0: d[:] = [o for o in d if o in folders]
            else:                         d[:] = [o for o in d if not o.startswith('.')]
            if len(folders) !=0 and i==0 and '.' not in folders: continue
            res += _get_files(p, f, extensions)
    else:
        f = [o.name for o in os.scandir(path) if o.is_file()]
        res = _get_files(path, f, extensions)
    return L(res)

# Cell
def parse_bin(bin_file, bytes_header: int = 36, marker: bytes = b'\x00UUUU'):
    with open(bin_file, mode='rb') as bfile:
        # O primeiro bloco do arquivo é o cabeçalho e tem 36 bytes de tamanho.
        header = bfile.read(bytes_header)
        body = bfile.read()
    return {'file_version': bin2dec(header[:4]), 'string': bin2str(header[4:]), 'blocos': classify_blocks(L(body.split(marker)))}

# Cell
def classify_blocks(blocks: L)->Mapping[int,L]:
    """Receives an iterable L with binary blocks and returns a defaultdict with a tuple (block types, thread_id) as keys and a list of the Class Blocks as values
        :param file: A string or pathlib.Path like path to a `.bin`file generated by CFRS - Logger
        :return: A Dictionary with block types as keys and a list of the Class Blocks available as values
    """
    map_block = defaultdict(L)
    for bloco in blocks.map(create_base_block):
        btype, btid = bloco.type, bloco.thread_id
        if btype == btid == 0:
            continue
        map_block[(btype, btid)].append(block_constructor(btype, bloco))
    return map_block

# Cell
def _extract_level(bloco: Any):
    return np.expand_dims(bloco.block_data, 0) # reshape((-1, 1))

def extract_block_levels(spectrum_blocks: Mapping[int,L], pivoted: bool = True, dtypes: Mapping[str, str] = None)->pd.DataFrame:
    """Receives a mapping `spectrum_blocks` and returns the Matrix with the Levels as values, Frequencies as columns and Block Number as index.
       :param pivoted: If False, optionally returns an unpivoted version of the Matrix
    """
    assert len(spectrum_blocks), f"The spectrum block list is empty"
    levels = np.concatenate(parallel(_extract_level, spectrum_blocks, n_workers=8, progress=False))
    frequencies = getattr(spectrum_blocks[0], 'frequencies')
    pivot = pd.DataFrame(levels, columns=frequencies)
    if not pivoted:
#         unpivot = pivot.melt(var_name="Frequency(MHz)", value_name="Nivel(dBm)")
#         unpivot['Block_Number'] = levels.shape[0] * list(range(levels.shape[1]))
#         unpivot.sort_values(['Block_Number', 'Frequency(MHz)'], inplace=True)
#         unpivot.reset_index(drop=True, inplace=True)
#         unpivot =  unpivot.astype({'Block_Number': 'category', 'Frequency(MHz)': 'float32', "Nivel(dBm)" : 'float16'})

        # Doing directly as numpy is faster than pandas
        unpivot = np.array([np.repeat(np.arange(levels.shape[1]), levels.shape[0]),
                            np.tile(frequencies, levels.shape[0]),
                            levels.flatten()]).T
        if not dtypes:
            dtypes = LEVELS
        return pd.DataFrame(unpivot, columns=LEVELS.keys()).astype(dtypes)
    return pivot

# Cell
def export_bin_meta(map_blocks: Mapping[int,L])->pd.DataFrame:
    """Receives a Mapping with the different `. bin` Blocks and extracts the metadata from them excluding spectral data.
    """
    for (tipo, tid), blocos in map_blocks.items():
            pass
    return df.astype(META)