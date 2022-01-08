from rfpye.utils import get_files
from rfpye.parser import parse_bin
from rich import print
from time import time

for f in get_files('binfiles', ".bin").shuffle():
    print(f'Testing for file {f.name}')
    start = time()
    dados = parse_bin(f)
    total = time() - start
    #print(dados)
    for spec in dados['spectrum']:
        print(repr(spec))
        print(spec.levels.shape)
    print(f'Tempo total de processamento: {total:.2f}s')


