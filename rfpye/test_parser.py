import sys
from pathlib import Path

# Insert in Path Project Directory
sys.path.insert(0, str(Path(__file__).parent))


from rfpye.parser import parse_bin
from fastcore.xtras import Path
from rfpye.utils import get_files
from rich import print

file = r"D:\rfeye002159_SLMA_bimestral_PEAK_210313_120302.bin"

dados = parse_bin(file)
