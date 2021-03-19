```python
#hide
%load_ext autoreload
%autoreload 2 
```


```python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
from pprint import pprint
import rfpy
from rfpy.parser import *
from nbdev.showdoc import *
from fastcore.xtras import Path
```

# RFPY
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca [fastcore](https://fastcore.fast.ai/basics.html), que expande e otimiza as estruturas de dados da linguagem python. 

## Instalação
`pip install rfpy`

## Como utilizar
Abaixo mostramos as funcionalidades principais dos módulos, utilizando-os dentro de algum outro script ou `REPL`

Precisamos necessariamente de um diretório de entrada, contendo um ou mais arquivos `.bin` e um diretório de saída no qual iremos salvar os arquivos processados. 
> Note: Mude os caminhos abaixo para suas pastas locais caso for executar o exemplo.

Ao utilizar o script `process_bin`, as pastas `entrada` e `saída` esses serão repassadas como parâmetros na linha de comando.


```python
VERBOSE = True
entrada = Path(r'D:\OneDrive - ANATEL\Backup_Rfeye_SP\RPO\PMEC2020\Ribeirao_Preto_SP\SLMA')
saida = Path(r'C:\Users\rsilva\Downloads\saida')
```

## Leitura de Arquivos

No módulo `parser.py`, há funções auxiliares para lidar com os arquivos `.bin`, pastas e para processar tais arquivos em formatos úteis. Nesse caso utilizaremos a função `get_files` que busca de maneira recursiva arquivos de dada extensão, inclusive links simbólicos se existirem
O caráter recursivo e a busca em links, `recurse` e `followlinks` simbólicos pode ser desativados por meio dos parâmetros e opcionalmente pode ser varrido somente o conjunto de pastas indicado em `folders` 


```python
#show_doc(get_files)
```


```python
arquivos = get_files(entrada, extensions=['.bin']) ; arquivos
```

> Important: O Objeto retornado `L` é uma extensão da lista python com funcionalidades adicionais, uma delas como  podemos ver é que a representação da lista impressa mostra o comprimento da lista. Esse objeto pode ser usado de maneira idêntica à uma lista em python e sem substituição desta.

Temos 255 arquivos bin na pasta entrada. Podemos filtrar por pasta também


```python
arquivos_bin = get_files(entrada, extensions=['.bin'], folders='tmp') ; arquivos_bin
```

Nesse caso dentro da pasta 'tmp' há somente 1 arquivo `.bin`


```python
bin_file = arquivos_bin[0] ; bin_file.name
```

## Processamento dos blocos
A função seguinte `parse_bin` recebe um arquivo `.bin` e mapeia os blocos contidos nele retornando um dicionário que tem como chave o tipo de bloco e os valores como uma lista com os blocos extraídos sequencialmente.


```python
show_doc(parse_bin)
```


```python
%%time
map_bin = parse_bin(bin_file)
```


```python
block.keys()
```

Exceto o primeiro bloco, que é simplesmente ignorado, os demais blocos são conhecidos e tratados individualmente.


```python
block[63]
```


```python
block[40]
```

Temos nesse arquivo 6605 blocos do tipo 63 - Bloco contendo dados de espectro.


```python
bloco = block[63][0]
```


```python
pprint([d for d in dir(bloco) if not d.startswith('_')])
```

Esses são os atributos do Bloco de Espectro acima do tipo 63. Todos podem ser acessados por meio da notação `.`


```python
bloco.data_points
```


```python
bloco.start_mega
```


```python
bloco.stop_mega
```


```python
bloco.level_offset
```

O bloco se comporta como um objeto python do tipo lista. 

Podemos selecionar items da lista, é retornado uma tupla com a frequência em `MHz` e o nível medido em `dBm / dBuV/m` 


```python
for freq, nível in bloco:
    print(freq, nível)
    break
```

Podemos iterar as medidas num loop


```python
len(bloco)
```

Esse é o mesmo valor do atributo `data_points`

## Metadados
A função seguinte extrai os metadados `META` definidos no cabeçalho do arquivo `parser.py` e retorna um DataFrame.


```python
#hide
show_doc(export_bin_meta)
```


```python
%%time
meta = export_bin_meta(block)
meta.tail(10)
```


```python
meta.info()
```

Os metadados de um arquivo `.bin` de cerca de `100MB` ocupa somente `226KB`


```python
meta.to_feather(saida / 'file_a.fth')
```

## Frequência e Nível
A função seguinte extrai as frequências e nível num formato de Tabela Dinâmica:
* Colunas: Frequências (MHz)
* Índice: Números de Bloco
* Valores: Níveis (dBm ou dBuV/m)


```python
#hide
#show_doc(export_bin_level)
```


```python
block[24].attrgot('thread_id')
```


```python
%%time
levels = export_bin_level(block) ; levels.head()
```


```python
levels.info()
```

Essa matriz com mais de 98 milhões de valores ocupa somente `187.1MB` de memória

Caso o parâmetro `pivoted = False` é retornada a versão tabular empilhada. No entanto o processamento é mais lento tendo em vista a redundância de dados que é adicionada.

Os tipos de dados a seguir são os automaticamente retornados pelo `numpy` / `pandas` no momento de criação da matriz


```python
dtypes = {'Block_Number': 'int32', 'Frequency(MHz)': 'float64', 'Nivel(dBm)': 'float64'}
```


```python
%%time
levels = export_bin_level(block, pivoted=False, dtypes=dtypes) ; levels.head()
```


```python
levels.info()
```

Esse formato de dados é extremamente redundante, repete-se o conjunto de blocos e frequências a cada bloco existente, por isso ocupa `1.8GB` de memória.

O número de bloco pode ser perfeitamente armazenado como um `int16`, a frequência como um `float32` e os níveis, dado termos somente 1 casa decimal, podem ser armazenados como `float16`


```python
dtypes = {'Block_Number': 'int16', 'Frequency(MHz)': 'float32', 'Nivel(dBm)': 'float32'}
```


```python
%%time
levels = export_bin_level(block, pivoted=False, dtypes=dtypes) ; levels.head()
```


```python
levels.info()
```

Reduzimos de `1.8GB` para `748.2MB` sem perda de informação.

No entanto, como não vamos fazer cálculos com essa matriz, somente extraí-la e armazená-la no momento, podemos manipular e salvar os valores em `float32` como `category` do pandas que ocupa o mesmo espaço próximo de um `int16` nesse caso, isso irá economizar bastante espaço tendo em vista o número fixo de frequências.


```python
dtypes = {'Block_Number': 'int16', 'Frequency(MHz)': 'category', 'Nivel(dBm)': 'float16'}
```


```python
%%time
levels = export_bin_level(block, pivoted=False, dtypes=dtypes) ; levels.head()
```


```python
levels.info()
```

Reduzimos assim de `1.8GB` para `561.9MB` sem perda de informação nos dados. Qualquer redução adicional implica numa transformação dos dados ou perda de precisão.


```python
%%time
levels.to_feather(saida / 'file_b.fth')
```
