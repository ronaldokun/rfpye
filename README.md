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
A função seguinte `file2block` recebe um arquivo `.bin` e mapeia os blocos contidos nele retornando um dicionário que tem como chave o tipo de bloco e os valores como uma lista com os blocos extraídos sequencialmente.

```python
#show_doc(file2block)
```

```python
block = file2block(bin_file)
```

```python
block.keys()
```

Exceto o primeiro bloco, que é simplesmente ignorado, os demais blocos são conhecidos e tratados individualmente.

```python
block[63]
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

```python
bloco[0], bloco[-1]
```

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


A função seguinte extrai os metadados `META` definidos no cabeçalho do arquivo `parser.py` e retorna um DataFrame.

```python
#hide
#show_doc(export_bin_meta)
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


A função seguinte extrai as frequências e nível num formato de Tabela Dinâmica:
* Colunas: Frequências (MHz)
* Índice: Números de Bloco
* Valores: Níveis (dBm ou dBuV/m)

```python
#hide
#show_doc(export_bin_level)
```

```python
%%time
levels = export_bin_level(block) ; levels.head()
```

```python
levels.info()
```

Essa matriz com mais de 98 milhões de valores ocupa somente `187.1MB` de memória


Caso o parâmetro `pivoted = False` é retornada a versão tabular empilhada. No entanto o processamento é muito mais lento tendo em vista a redundância de dados que é adicionada.

```python
%%time
levels = export_bin_level(block, pivoted=False) ; levels.head()
```

```python
levels.info()
```

Como não vamos fazer cálculos com essa matriz, somente extração e armazenamento, podemos manipular e salvar os valores como o tipo `category` do pandas. que ocupa o mesmo que um `int16` nesse caso.

```python
levels.tail()
```

```python
%%time
levels.to_feather(saida / 'file_b.fth')
```
