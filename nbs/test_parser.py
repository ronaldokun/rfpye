from rfpye.utils import get_files
from rfpye.parser import parse_bin
from fastcore.basics import partialler
from fastcore.utils import parallel
from pathos.parallel import ParallelPool as Pool
from typing import *
from rich import print
from time import time
from pathlib import Path
import numpy as np


def parse_folder(
    path: Union[str, Path], recursive: bool = True, precision=np.float32
) -> Union[list, dict]:
    folder = Path(path)
    if folder.is_file():
        return parse_bin(folder, precision)
    elif folder.is_dir():
        # function = partialler(parse_bin, precision=precision)
        pool = Pool(nodes=8)
        # setattr(function, "__module__", "rfpye.parser")
        return pool.imap(parse_bin, get_files(folder, extensions=".bin", recurse=True))


def main():
    inicio = time()
    for folder in Path("binfiles").iterdir():
        print(f"Teste para arquivos do tipo {folder.name}")
        for file in get_files(folder, ".bin"):
            print(f"\t{file.name}")
            start = time()
            dados = parse_bin(file)
            for m in dados["spectrum"].attrgot("levels"):
                print(m.shape)
            total = time() - start
            print(dados)
            print(f"Tempo de processamento: {total:.2f}s")
            print("=" * 100)
    # dados = list(parse_folder("binfiles"))
    # print(dados)
    print(f"Tempo total de processamento: {time() - inicio:.2f}s")


if __name__ == "__main__":
    main()
