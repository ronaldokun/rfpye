# AUTOGENERATED! DO NOT EDIT! File to edit: 00_main.ipynb (unless otherwise specified).

__all__ = ['parse_input']

# Cell
from pathlib import Path
from typing import *
from fastcore.script import *
from .parser import get_files

# Cell
@call_parse
def parse_input(entrada:Param("Diretório contendo arquivos .bin", str),
                saida:Param("Diretório para salvar os arquivos de saída", str),
                recursivo:Param("Buscar arquivos de maneira recursiva?", bool_arg)=True,
                pastas:Param("Limita a busca às pastas", Iterable[str]) = None,
                verbose:Param("Imprimir mensagens de execução?", bool_arg) = False):

        lista_bins = get_files(entrada, extensions=['.bin'], recurse=recursivo, folders=pastas)

        if verbose:
            print(lista_bins)
        return lista_bins