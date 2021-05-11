# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.0
#   kernelspec:
#     display_name: Python [conda env:rfpy]
#     language: python
#     name: conda-env-rfpy-py
# ---

# # Leitura de dados binários - um exemplo de otimização em Python
# > As atividades de monitoramento do espectro de radiofrequência na ANATEL, especificamente aquelas que utilizam estações remotas de monitoramento, geram centenas de GB de dados. Um dos primeiros desafios para a utilização mais eficiente desses dados é a sua leitura eficiente. Nesse artigo é detalhada as iterações realizadas para resolver esse problema, primeiramente tornar essa leitura viável e posteriormente os passos de otimização aplicados no algoritmo para decodificar os dados de arquivos comprimidos 
#
# - toc: true
# - branch: master
# - badges: true
# - comments: true
# - categories: [spectrum monitoring, profiling, numpy, cython]
# - image: images/multiplication.jpg
# - hide_binder_badge: true
# - author: Ronaldo S.A. Batista

# ![](images/knuth.jpeg "Crédito: https://twitter.com/lpolovets/status/816117631572807680")

# O objeto desse artigo são arquivos binários com extensão `.bin` - gerados pela aplicação `Logger` embarcada nas estações de monitoramento do tipo [Rfeye Node 20-6](http://agc.com.br/produto/rfeye-node/).
#
# Estes arquivos armazenam diversos metadados sobre a medição e blocos com informação numérica, que são as medidas em si, chamadas aqui de _dados de espectro_ ou _dados espectrais_. 
#
# A versão recente da aplicação `Logger` gera dados comprimidos de maneira muito eficiente, o que torna a descompressão desafiadora para arquivos com muitos dados e bastante demorada caso seja feita de maneira "ingênua".
#
# Mesmo que essa o problema apresentado aqui pareça obscuro, as técnicas de otimização podem ser aplicadas em outros contextos que sejam relevantes para quem lê.

# > Note: Nos parágrafos a seguir irei passar por cima deliberadamente ( por não serem relevantes para a otimização e por pouco conhecimento no assunto ) de explicações sobre a parte de física / engenharia de telecomunicações e irei focar mais no problema específico de decodificação dos arquivos.

# ## Explorando o arquivo `.bin`
#
# Cada arquivo `.bin` possui dados distintos em um mesmo arquivo, em dois níveis `blocos` e `thread_id`.
#
# * Um `bloco` determina o tipo de dado: espectro, gps, dados textuais etc...
# * O `thread_id` nada mais é que um identificador da faixa específica de varredura armazenada naquele bloco.
#
# A função a seguir `parse_bin` encapsula a leitura do arquivo e seus metadados e retorna um dicionário cujas chaves são as diferentes combinações de `blocos` e `thread_id` e os valores são listas com os blocos. 
#
# > Note: Cada bloco é uma classe python contendo seus atributos. Os detalhes de implementação dessa função podem ser ignorados, o que nos interessa aqui é uma vez que temos os bytes de dados com os valores de níveis como o lemos de maneira eficiente.
#
# > Tip: A biblioteca `rfpy` criada para o processamento desses arquivos faz amplo uso da biblioteca [fastcore](https://fastcore.fast.ai/). Esta expande as funcionalidades da linguagem python inspirada em atributos muito úteis de outras linguagens. Recomendo fortemente para quem deseja expandir o seu inventário de ferramentas python

#hide
# %load_ext autoreload
# %load_ext line_profiler
# %load_ext cython
# %autoreload 2 

import sys, os
from tqdm.notebook import tqdm
from fastcore.xtras import Path
# Insert in Path Project Directory
sys.path.insert(0, str(Path().cwd().parent))
from multiprocessing import set_start_method, Pool
try:
    set_start_method("spawn")
except RuntimeError:
    pass
import gc
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
from rfpy.parser import parse_bin
from rfpy.utils import public_attrs
from fastcore.foundation import L
import numpy as np
import pandas as pd
from pprint import pprint as pp
from IPython.display import display
import gc

# +
blocks = parse_bin('~/Code/rfpy/binfiles/rfeye002092_210223_T163131_MaskBroken.bin')
blocks = blocks['blocks']

RUN = 255
ESC = 254

compressed_blocks = blocks[(68,301)].itemgot(1)


#hide
from rfpy.parser import run_length_decode6

from functools import partial
from fastcore.utils import parallel
def test_prealloc_mp(blocks):
    thresh = blocks[0].thresh
    decoded = np.full((len(blocks), blocks[0].norig), thresh, dtype=np.float16)
    offset=blocks[0].offset
    items = list(range(len(blocks)))
    func = partial(run_length_decode6, decoded=decoded, blocks=blocks)
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(run_length_decode6, items)
    return decoded

# %%time
d = test_prealloc_mp(compressed_blocks)

