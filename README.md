# RFPY - Extração otimizada dos dados de arquivos `.bin` provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node.
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro. Para talt utilizamos as várias funcionalidades da biblioteca <a href='https://fastcore.fast.ai/basics.html'>fastcore</a>, que expande e otimiza as estruturas de dados da linguagem python. 


## Instalação
`pip install rfpy`

## Como utilizar
Abaixo mostramos as funcionalidades principais dos módulos, utilizando-os dentro de algum outro script ou `REPL`

Precisamos necessariamente de um diretório de entrada, contendo um ou mais arquivos `.bin` e um diretório de saída no qual iremos salvar os arquivos processados. 
{% include note.html content='Mude os caminhos abaixo para suas pastas locais caso for executar o exemplo.' %}
Ao utilizar o script `process_bin`, as pastas `entrada` e `saída` esses serão repassadas como parâmetros na linha de comando.

```python
VERBOSE = True
entrada = Path(r'D:\OneDrive - ANATEL\Backup_Rfeye_SP\RPO\PMEC2020\Ribeirao_Preto_SP\SLMA')
saida = Path(r'C:\Users\rsilva\Downloads\saida')
```

## Leitura de Arquivos

No módulo `parser.py`, há funções auxiliares para lidar com os arquivos `.bin`, pastas e para processar tais arquivos em formatos úteis. Nesse caso utilizaremos a função `get_files` que busca de maneira recursiva arquivos de dada extensão, inclusive links simbólicos se existirem
O caráter recursivo e a busca em links, `recurse` e `followlinks` simbólicos pode ser desativados por meio dos parâmetros e opcionalmente pode ser varrido somente o conjunto de pastas indicado em `folders` 


<h4 id="get_files" class="doc_header"><code>get_files</code><a href="https://github.com/ronaldokun/rfpy/tree/master/rfpy/parser.py#L64" class="source_link" style="float:right">[source]</a></h4>

> <code>get_files</code>(**`path`**, **`extensions`**=*`None`*, **`recurse`**=*`True`*, **`folders`**=*`None`*, **`followlinks`**=*`True`*)

Get all the files in `path` with optional `extensions`, optionally with `recurse`, only in `folders`, if specified.


```python
arquivos = get_files(entrada, extensions=['.bin']) ; arquivos
```




    (#255) [Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200317_232233.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200318_225525.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200318_225535.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200318_225556.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200318_225615.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200410_183001.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200423_162327.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200516_120002.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200520_054608.bin'),Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/rfeye002304_SLMA_bimestral_occ15min_200612_013001.bin')...]



{% include important.html content='O Objeto retornado `L` é uma extensão da lista python com funcionalidades adicionais, uma delas como  podemos ver é que a representação da lista impressa mostra o comprimento da lista. Esse objeto pode ser usado de maneira idêntica à uma lista em python e sem substituição desta.' %}

Temos 255 arquivos bin na pasta entrada. Podemos filtrar por pasta também

```python
arquivos_bin = get_files(entrada, extensions=['.bin'], folders='tmp') ; arquivos_bin
```




    (#1) [Path('D:/OneDrive - ANATEL/Backup_Rfeye_SP/RPO/PMEC2020/Ribeirao_Preto_SP/SLMA/tmp/rfeye002304_SLMA_bimestral_PEAK_200829_234902.bin')]



Nesse caso dentro da pasta 'tmp' há somente 1 arquivo `.bin`

```python
bin_file = arquivos_bin[0] ; bin_file.name
```




    'rfeye002304_SLMA_bimestral_PEAK_200829_234902.bin'



## Processamento dos blocos
A função seguinte `file2block` recebe um arquivo `.bin` e mapeia os blocos contidos nele retornando um dicionário que tem como chave o tipo de bloco e os valores como uma lista com os blocos extraídos sequencialmente.


<h4 id="file2block" class="doc_header"><code>file2block</code><a href="https://github.com/ronaldokun/rfpy/tree/master/rfpy/parser.py#L113" class="source_link" style="float:right">[source]</a></h4>

> <code>file2block</code>(**`file`**:`Union`\[`str`, `Path`\])

Receives a path to a bin file and returns a defaultdict with unique block types as keys and a list of the Class Blocks as values
:param file: A string or pathlib.Path like path to a `.bin`file generated by CFRS - Logger
:return: A Dictionary with block types as keys and a list of the Class Blocks available as values


```python
block = file2block(bin_file)
```

```python
block.keys()
```




    dict_keys([1413563424, 21, 41, 24, 40, 63])



Exceto o primeiro bloco, que é simplesmente ignorado, os demais blocos são conhecidos e tratados individualmente.

```python
block[63]
```




    (#6605) [<rfpy.blocks.DType63 object at 0x000002B54F47F940>,<rfpy.blocks.DType63 object at 0x000002B54F47FAC0>,<rfpy.blocks.DType63 object at 0x000002B54F47FBE0>,<rfpy.blocks.DType63 object at 0x000002B54F47FD00>,<rfpy.blocks.DType63 object at 0x000002B54F47FE20>,<rfpy.blocks.DType63 object at 0x000002B54F47FF40>,<rfpy.blocks.DType63 object at 0x000002B5482300A0>,<rfpy.blocks.DType63 object at 0x000002B5482301C0>,<rfpy.blocks.DType63 object at 0x000002B5482302E0>,<rfpy.blocks.DType63 object at 0x000002B548230400>...]



Temos nesse arquivo 6605 blocos do tipo 63 - Bloco contendo dados de espectro.

```python
bloco = block[63][0]
```

```python
pprint([d for d in dir(bloco) if not d.startswith('_')])
```

    ['agc_array',
     'banda_mega',
     'banda_mili',
     'block_data',
     'bw',
     'channel',
     'count',
     'data',
     'data_points',
     'date',
     'datetime_stamp',
     'default',
     'frequencies',
     'global_error_code',
     'global_flags_code',
     'group_id',
     'id_antenna',
     'index',
     'len_agc',
     'len_padding',
     'len_tunning_info',
     'level_offset',
     'nanosecs',
     'num_meas',
     'passo',
     'processing',
     'rbw',
     'size',
     'spent_time_microsecs',
     'start_mega',
     'start_mili',
     'stop_mega',
     'stop_mili',
     'thread_id',
     'time',
     'trailer',
     'tunning_info_array',
     'type',
     'unit']
    

Esses são os atributos do Bloco de Espectro acima do tipo 63. Todos podem ser acessados por meio da notação `.`

```python
bloco.data_points
```




    14848



```python
bloco.start_mega
```




    108



```python
bloco.stop_mega
```




    137



```python
bloco.level_offset
```




    -20



O bloco se comporta como um objeto python do tipo lista. 

```python
bloco[0], bloco[-1]
```




    ((108.0, -75.0), (137.0, -96.5))



Podemos selecionar items da lista, é retornado uma tupla com a frequência em `MHz` e o nível medido em `dBm / dBuV/m` 

```python
for freq, nível in bloco:
    print(freq, nível)
    break
```

    108.0 -75.0
    

Podemos iterar as medidas num loop

```python
len(bloco)
```




    14848



Esse é o mesmo valor do atributo `data_points`

A função seguinte extrai os metadados `META` definidos no cabeçalho do arquivo `parser.py` e retorna um DataFrame.


<h4 id="export_bin_meta" class="doc_header"><code>export_bin_meta</code><a href="https://github.com/ronaldokun/rfpy/tree/master/rfpy/parser.py#L179" class="source_link" style="float:right">[source]</a></h4>

> <code>export_bin_meta</code>(**`map_block`**:`Mapping`\[`int`, `L`\])

Receives a Mapping with the different `. bin` Blocks and extracts the metadata listed in [`META`](/rfpy/parser.html#META) in a dataframe format
    


```python
%%time
meta = export_bin_meta(block)
meta.tail(10)
```

    Wall time: 585 ms
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Block_Number</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Altitude</th>
      <th>Initial_Time</th>
      <th>Sample_Duration</th>
      <th>Start_Frequency</th>
      <th>Stop_Frequency</th>
      <th>Vector_Length</th>
      <th>Trace_Type</th>
      <th>Antenna_Type</th>
      <th>Equipement_ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6595</th>
      <td>6595</td>
      <td>-21.228973</td>
      <td>-47.759907</td>
      <td>623.5</td>
      <td>2020-09-03 13:45:01.833424</td>
      <td>60428</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6596</th>
      <td>6596</td>
      <td>-21.228973</td>
      <td>-47.759933</td>
      <td>621.5</td>
      <td>2020-09-03 13:46:00.811335</td>
      <td>60514</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6597</th>
      <td>6597</td>
      <td>-21.228977</td>
      <td>-47.759914</td>
      <td>623.0</td>
      <td>2020-09-03 13:47:01.501244</td>
      <td>60358</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6598</th>
      <td>6598</td>
      <td>-21.228973</td>
      <td>-47.759907</td>
      <td>625.0</td>
      <td>2020-09-03 13:48:00.511332</td>
      <td>60397</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6599</th>
      <td>6599</td>
      <td>-21.228964</td>
      <td>-47.759922</td>
      <td>620.0</td>
      <td>2020-09-03 13:49:01.191148</td>
      <td>60476</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6600</th>
      <td>6600</td>
      <td>-21.228956</td>
      <td>-47.759922</td>
      <td>620.5</td>
      <td>2020-09-03 13:50:01.891165</td>
      <td>60218</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6601</th>
      <td>6601</td>
      <td>-21.228941</td>
      <td>-47.759911</td>
      <td>621.0</td>
      <td>2020-09-03 13:51:00.811174</td>
      <td>60443</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6602</th>
      <td>6602</td>
      <td>-21.228968</td>
      <td>-47.759907</td>
      <td>619.0</td>
      <td>2020-09-03 13:52:01.501244</td>
      <td>60415</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6603</th>
      <td>6603</td>
      <td>-21.228954</td>
      <td>-47.759907</td>
      <td>620.5</td>
      <td>2020-09-03 13:53:00.411253</td>
      <td>60307</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
    <tr>
      <th>6604</th>
      <td>6604</td>
      <td>-21.228962</td>
      <td>-47.759907</td>
      <td>618.0</td>
      <td>2020-09-03 13:54:01.091231</td>
      <td>60272</td>
      <td>108</td>
      <td>137</td>
      <td>14848</td>
      <td>peak</td>
      <td>1</td>
      <td>rfeye002304</td>
    </tr>
  </tbody>
</table>
</div>



```python
meta.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6605 entries, 0 to 6604
    Data columns (total 12 columns):
     #   Column           Non-Null Count  Dtype         
    ---  ------           --------------  -----         
     0   Block_Number     6605 non-null   uint16        
     1   Latitude         6605 non-null   float32       
     2   Longitude        6605 non-null   float32       
     3   Altitude         6605 non-null   float16       
     4   Initial_Time     6605 non-null   datetime64[ns]
     5   Sample_Duration  6605 non-null   uint16        
     6   Start_Frequency  6605 non-null   uint32        
     7   Stop_Frequency   6605 non-null   uint32        
     8   Vector_Length    6605 non-null   uint16        
     9   Trace_Type       6605 non-null   category      
     10  Antenna_Type     6605 non-null   category      
     11  Equipement_ID    6605 non-null   category      
    dtypes: category(3), datetime64[ns](1), float16(1), float32(2), uint16(3), uint32(2)
    memory usage: 226.1 KB
    

Os metadados de um arquivo `.bin` de cerca de `100MB` ocupa somente `226KB`

A função seguinte extrai as frequências e nível num formato de Tabela Dinâmica:
* Colunas: Frequências (MHz)
* Índice: Números de Bloco
* Valores: Níveis (dBm ou dBuV/m)


<h4 id="export_bin_level" class="doc_header"><code>export_bin_level</code><a href="https://github.com/ronaldokun/rfpy/tree/master/rfpy/parser.py#L156" class="source_link" style="float:right">[source]</a></h4>

> <code>export_bin_level</code>(**`map_block`**:`Mapping`\[`int`, `L`\], **`pivoted`**:`bool`=*`True`*, **`freq_dtype`**:`str`=*`'float32'`*)

Receives a mapping `map_block` and returns the Matrix with the Levels as values, Frequencies as columns and Block Number as index.
:param pivoted: If False, optionally returns an unpivoted version of the Matrix


```python
%%time
levels = export_bin_level(block) ; levels.head()
```

    Wall time: 7.37 s
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>108.000000</th>
      <th>108.001953</th>
      <th>108.003907</th>
      <th>108.005860</th>
      <th>108.007813</th>
      <th>108.009766</th>
      <th>108.011720</th>
      <th>108.013673</th>
      <th>108.015626</th>
      <th>108.017579</th>
      <th>...</th>
      <th>136.982421</th>
      <th>136.984374</th>
      <th>136.986327</th>
      <th>136.988280</th>
      <th>136.990234</th>
      <th>136.992187</th>
      <th>136.994140</th>
      <th>136.996093</th>
      <th>136.998047</th>
      <th>137.000000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-75.0</td>
      <td>-75.5</td>
      <td>-76.5</td>
      <td>-77.0</td>
      <td>-77.5</td>
      <td>-78.5</td>
      <td>-79.0</td>
      <td>-80.5</td>
      <td>-80.5</td>
      <td>-80.5</td>
      <td>...</td>
      <td>-95.0</td>
      <td>-93.5</td>
      <td>-95.0</td>
      <td>-93.5</td>
      <td>-91.5</td>
      <td>-92.0</td>
      <td>-98.0</td>
      <td>-99.0</td>
      <td>-97.5</td>
      <td>-96.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-66.0</td>
      <td>-70.5</td>
      <td>-74.0</td>
      <td>-75.5</td>
      <td>-75.5</td>
      <td>-76.0</td>
      <td>-77.0</td>
      <td>-77.5</td>
      <td>-75.0</td>
      <td>-75.5</td>
      <td>...</td>
      <td>-93.5</td>
      <td>-95.0</td>
      <td>-94.0</td>
      <td>-91.0</td>
      <td>-92.0</td>
      <td>-94.0</td>
      <td>-96.0</td>
      <td>-96.5</td>
      <td>-96.5</td>
      <td>-96.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-83.5</td>
      <td>-84.5</td>
      <td>-89.5</td>
      <td>-81.5</td>
      <td>-84.5</td>
      <td>-87.0</td>
      <td>-85.5</td>
      <td>-83.0</td>
      <td>-84.5</td>
      <td>-87.5</td>
      <td>...</td>
      <td>-93.5</td>
      <td>-93.5</td>
      <td>-92.5</td>
      <td>-92.0</td>
      <td>-92.5</td>
      <td>-93.5</td>
      <td>-97.5</td>
      <td>-98.0</td>
      <td>-98.5</td>
      <td>-96.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-87.5</td>
      <td>-87.5</td>
      <td>-91.5</td>
      <td>-69.5</td>
      <td>-85.5</td>
      <td>-85.5</td>
      <td>-89.0</td>
      <td>-90.5</td>
      <td>-88.5</td>
      <td>-87.0</td>
      <td>...</td>
      <td>-93.5</td>
      <td>-93.5</td>
      <td>-94.0</td>
      <td>-93.5</td>
      <td>-93.0</td>
      <td>-93.0</td>
      <td>-98.5</td>
      <td>-96.5</td>
      <td>-94.5</td>
      <td>-95.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-80.5</td>
      <td>-75.5</td>
      <td>-72.5</td>
      <td>-71.5</td>
      <td>-73.0</td>
      <td>-76.5</td>
      <td>-73.0</td>
      <td>-74.0</td>
      <td>-79.5</td>
      <td>-87.5</td>
      <td>...</td>
      <td>-95.0</td>
      <td>-95.0</td>
      <td>-94.0</td>
      <td>-94.0</td>
      <td>-93.5</td>
      <td>-93.0</td>
      <td>-96.5</td>
      <td>-96.5</td>
      <td>-95.5</td>
      <td>-96.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 14848 columns</p>
</div>



```python
levels.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6605 entries, 0 to 6604
    Columns: 14848 entries, 108.0 to 137.0
    dtypes: float16(14848)
    memory usage: 187.1 MB
    

Essa matriz com mais de 98 milhões de valores ocupa somente `187.1MB` de memória

Caso o parâmetro `pivoted = False` é retornada a versão tabular empilhada. No entanto o processamento é muito mais lento tendo em vista a redundância de dados que é adicionada.

```python
%%time
levels = export_bin_level(block, pivoted=False) ; levels.head()
```

    Wall time: 14.4 s
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Block_Number</th>
      <th>Frequency(MHz)</th>
      <th>Nivel(dBm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>108.000000</td>
      <td>-75.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>108.001953</td>
      <td>-75.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>108.003907</td>
      <td>-76.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>108.005860</td>
      <td>-77.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>108.007813</td>
      <td>-77.5</td>
    </tr>
  </tbody>
</table>
</div>



```python
levels.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 98071040 entries, 0 to 98071039
    Data columns (total 3 columns):
     #   Column          Dtype   
    ---  ------          -----   
     0   Block_Number    category
     1   Frequency(MHz)  category
     2   Nivel(dBm)      float16 
    dtypes: category(2), float16(1)
    memory usage: 562.6 MB
    

Como não vamos fazer cálculos com essa matriz, somente extração e armazenamento, podemos manipular e salvar os valores como o tipo `category` do pandas. que ocupa o mesmo que um `int16` nesse caso.

```python
levels.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Block_Number</th>
      <th>Frequency(MHz)</th>
      <th>Nivel(dBm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>98071035</th>
      <td>14847.0</td>
      <td>136.992187</td>
      <td>-94.0</td>
    </tr>
    <tr>
      <th>98071036</th>
      <td>14847.0</td>
      <td>136.994140</td>
      <td>-98.5</td>
    </tr>
    <tr>
      <th>98071037</th>
      <td>14847.0</td>
      <td>136.996093</td>
      <td>-98.5</td>
    </tr>
    <tr>
      <th>98071038</th>
      <td>14847.0</td>
      <td>136.998047</td>
      <td>-99.0</td>
    </tr>
    <tr>
      <th>98071039</th>
      <td>14847.0</td>
      <td>137.000000</td>
      <td>-98.5</td>
    </tr>
  </tbody>
</table>
</div>



```python
%%time
levels.to_feather(saida / 'file_b.fth')
```

    Wall time: 970 ms
    
