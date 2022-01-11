from rfpye.utils import get_files
from rfpye.parser import parse_bin
from rich import print
from time import time
from pathlib import Path                                                                                                

inicio = time()
for folder in Path('binfiles').iterdir():
    print(f'Teste para arquivos do tipo {folder.name}')
    for file in get_files(folder, '.bin'):
        print(f'\t{file.name}')
        start = time()
        dados = parse_bin(file)
        total = time() - start
        print(dados)       
        print(f'Tempo de processamento: {total:.2f}s')
        print('='*100)
print(f'Tempo total de processamento: {time() - inicio:.2f}s')


