```python
#hide
%load_ext autoreload
%autoreload 2 
```


```python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
from rich import print
```

# RFPYE
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca [fastcore](https://fastcore.fast.ai/basics.html), que expande e otimiza as estruturas de dados da linguagem python. 

## Instalação
Como parte dessa lib utiliza código c compilado com `Cython`, é preciso que um compilador `C` esteja instalado. Em Windows, uma opção é instalar a versão apropriada do Visual Studio seguindo as orientações do site da Microsoft. No entanto uma solução mais simples e a recomendada é utilizando o `conda`.

Primeiramente instale o [miniconda](https://docs.conda.io/en/latest/miniconda.html). Com o conda instalado e disponível no seu `PATH` ou através do `Anaconda Prompt` execute o comando:

```bash
conda install -c intel libpython m2w64-toolchain -y

echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg
```

Depois disso basta instalar normalmente a lib:
`python -m pip install rfpye`

Em Linux normalmente o sistema já possui o compilador `gcc` instalado então basta executar o comando `pip install` acima.

## Como utilizar
Abaixo mostramos as funcionalidades principais dos módulos, utilizando-os dentro de algum outro script ou `REPL`

Precisamos necessariamente de um diretório de entrada, contendo um ou mais arquivos `.bin` e um diretório de saída no qual iremos salvar os arquivos processados. 
> Mude os caminhos abaixo para suas pastas locais caso for executar o exemplo.

Ao utilizar o script `process_bin`, as pastas `entrada` e `saída` esses serão repassadas como parâmetros na linha de comando.


```python
from fastcore.xtras import Path
VERBOSE = True
entrada = Path(r'D:\OneDrive - ANATEL\Backup_Rfeye_SP\CPV\2021')
saida = Path(r'C:\Users\rsilva\Downloads\saida')
```

## Leitura de Arquivos

No módulo `parser.py`, há funções auxiliares para lidar com os arquivos `.bin`, pastas e para processar tais arquivos em formatos úteis. Nesse caso utilizaremos a função `get_files` que busca de maneira recursiva arquivos de dada extensão, inclusive links simbólicos se existirem
O caráter recursivo e a busca em links, `recurse` e `followlinks` simbólicos pode ser desativados por meio dos parâmetros e opcionalmente pode ser varrido somente o conjunto de pastas indicado em `folders` 


```python
from rfpye.utils import get_files
arquivos = get_files(entrada, extensions=['.bin']) ; print(arquivos[:10])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[</span>Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210204_T184230.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210204_T184230_MaskBroken.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210204_T184431.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210204_T184431_MaskBroken.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210206_T210901.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210208_T233102.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210211_T004502.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CPV/2021/rfeye002310_210211_T004502_MaskBroken.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/RFeye002310_210211_T011350.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - ANATEL/Backup_Rfeye_SP/CPV/2021/RFeye002310_210213_T033501.bin'</span><span style="font-weight: bold">)]</span>
</pre>



> O Objeto retornado `L` é uma extensão da lista python com funcionalidades adicionais, uma delas como  podemos ver é que a representação da lista impressa mostra o comprimento da lista. Esse objeto pode ser usado de maneira idêntica à uma lista em python e sem substituição desta.


```python
bin_file = arquivos[-1] ; print(bin_file.name)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">RFeye002310_210520_T181500.bin
</pre>



## Processamento dos blocos
A função seguinte `parse_bin` recebe um arquivo `.bin` e mapeia os blocos contidos nele retornando um dicionário que tem como chave o tipo de bloco e os valores como uma lista com os blocos extraídos sequencialmente.


```python
from rfpye.parser import parse_bin, extract_metadata, extract_level
```


```python
%%time
map_bin = parse_bin(bin_file)['blocks']
```

    Wall time: 4.48 s
    


```python
for k, b in map_bin.items():
    print(f'Tipo de Bloco: {k[0]}, Fluxo (Thread ID): {k[1]}, #Blocos: {len(b)}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">90</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3023</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">604</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">604</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">604</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50</span>
</pre>




```python
gps = map_bin[(40,1)]
spec = map_bin[(67,20)]
```

A seguir é mostrado um exemplo dos atributos contidos num bloco de gps e num bloco de espectro


```python
from rfpye.utils import getattrs
print(getattrs(gps[0][1]))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">571.6</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_size'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps_datetime'</span>: datetime.datetime<span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">16</span><span style="font-weight: bold">)</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps_status'</span>: <span style="color: #008000; text-decoration-color: #008000">'Standard GPS'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'heading'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.101629</span>,
    <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-45.7066</span>,
    <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>,
    <span style="color: #008000; text-decoration-color: #008000">'speed'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.04</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'wallclock_datetime'</span>: numpy.datetime64<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'2021-05-20T18:16:00.785620'</span><span style="font-weight: bold">)</span>
<span style="font-weight: bold">}</span>
</pre>




```python
print(getattrs(spec[0][1]))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'antenna_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_size'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1156</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'desclen'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">28</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa 2 de 4).'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'dynamic_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gerror'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gflags'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'group_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'minimum'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-56.5</span>,
    <span style="color: #008000; text-decoration-color: #008000">'n_agc'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>,
    <span style="color: #008000; text-decoration-color: #008000">'n_tunning'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>,
    <span style="color: #008000; text-decoration-color: #008000">'namal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'ndata'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>,
    <span style="color: #008000; text-decoration-color: #008000">'npad'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'offset'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">71</span>,
    <span style="color: #008000; text-decoration-color: #008000">'padding'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'processing'</span>: <span style="color: #008000; text-decoration-color: #008000">'peak'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'resolution_bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>,
    <span style="color: #008000; text-decoration-color: #008000">'sample'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5316</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">131</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_channel'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mili'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'step'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.039100684261974585</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1155</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_channel'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mili'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>,
    <span style="color: #008000; text-decoration-color: #008000">'wallclock_datetime'</span>: numpy.datetime64<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'2021-05-20T18:20:00.107910'</span><span style="font-weight: bold">)</span>
<span style="font-weight: bold">}</span>
</pre>



## Metadados
A função seguinte extrai os metadados `META` definidos no cabeçalho do arquivo `constants.py` e retorna um DataFrame.


```python
gps_meta = extract_metadata(gps)
gps_meta.head()
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
      <th>start_byte</th>
      <th>stop_byte</th>
      <th>altitude</th>
      <th>data_size</th>
      <th>gps_datetime</th>
      <th>gps_status</th>
      <th>heading</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>num_satellites</th>
      <th>speed</th>
      <th>thread_id</th>
      <th>type</th>
    </tr>
    <tr>
      <th>wallclock_datetime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-05-20 18:16:00.785620</th>
      <td>344</td>
      <td>399</td>
      <td>571.599976</td>
      <td>40</td>
      <td>2021-05-20 18:16:00</td>
      <td>Standard GPS</td>
      <td>0.0</td>
      <td>-23.101629</td>
      <td>-45.706600</td>
      <td>11</td>
      <td>0.040</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-20 18:17:00.283280</th>
      <td>31436</td>
      <td>31491</td>
      <td>574.799988</td>
      <td>40</td>
      <td>2021-05-20 18:17:00</td>
      <td>Standard GPS</td>
      <td>0.0</td>
      <td>-23.101616</td>
      <td>-45.706612</td>
      <td>11</td>
      <td>0.033</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-20 18:18:00.183600</th>
      <td>62528</td>
      <td>62583</td>
      <td>574.299988</td>
      <td>40</td>
      <td>2021-05-20 18:18:00</td>
      <td>Standard GPS</td>
      <td>0.0</td>
      <td>-23.101612</td>
      <td>-45.706612</td>
      <td>11</td>
      <td>0.037</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-20 18:19:00.219400</th>
      <td>93620</td>
      <td>93675</td>
      <td>577.200012</td>
      <td>40</td>
      <td>2021-05-20 18:19:00</td>
      <td>Standard GPS</td>
      <td>0.0</td>
      <td>-23.101606</td>
      <td>-45.706612</td>
      <td>11</td>
      <td>0.025</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-20 18:20:00.683610</th>
      <td>124712</td>
      <td>124767</td>
      <td>573.599976</td>
      <td>40</td>
      <td>2021-05-20 18:20:00</td>
      <td>Standard GPS</td>
      <td>0.0</td>
      <td>-23.101625</td>
      <td>-45.706608</td>
      <td>11</td>
      <td>0.053</td>
      <td>1</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
spec_meta = extract_metadata(spec)
spec_meta.tail()
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
      <th>start_byte</th>
      <th>stop_byte</th>
      <th>antenna_id</th>
      <th>bw</th>
      <th>data_size</th>
      <th>data_type</th>
      <th>desclen</th>
      <th>description</th>
      <th>dynamic_id</th>
      <th>gerror</th>
      <th>...</th>
      <th>start_channel</th>
      <th>start_mega</th>
      <th>start_mili</th>
      <th>step</th>
      <th>stop</th>
      <th>stop_channel</th>
      <th>stop_mega</th>
      <th>stop_mili</th>
      <th>thread_id</th>
      <th>type</th>
    </tr>
    <tr>
      <th>wallclock_datetime</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-05-22 20:15:00.160846</th>
      <td>99227964</td>
      <td>99229135</td>
      <td>0</td>
      <td>40</td>
      <td>1156</td>
      <td>1</td>
      <td>28</td>
      <td>PRD 2021 (Faixa 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1155</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>20</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-22 20:20:00.708650</th>
      <td>99393348</td>
      <td>99394519</td>
      <td>0</td>
      <td>40</td>
      <td>1156</td>
      <td>1</td>
      <td>28</td>
      <td>PRD 2021 (Faixa 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1155</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>20</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-22 20:25:00.230842</th>
      <td>99558732</td>
      <td>99559903</td>
      <td>0</td>
      <td>40</td>
      <td>1156</td>
      <td>1</td>
      <td>28</td>
      <td>PRD 2021 (Faixa 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1155</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>20</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-22 20:30:00.408390</th>
      <td>99724116</td>
      <td>99725287</td>
      <td>0</td>
      <td>40</td>
      <td>1156</td>
      <td>1</td>
      <td>28</td>
      <td>PRD 2021 (Faixa 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1155</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>20</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-22 20:35:00.180936</th>
      <td>99889500</td>
      <td>99890671</td>
      <td>0</td>
      <td>40</td>
      <td>1156</td>
      <td>1</td>
      <td>28</td>
      <td>PRD 2021 (Faixa 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1155</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>20</td>
      <td>67</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>



## Frequência e Nível
A função seguinte extrai as frequências e nível num formato de Tabela Dinâmica:
* Colunas: Frequências (MHz)
* Índice: Números de Bloco
* Valores: Níveis (dBm ou dBuV/m)


```python
levels = extract_level(spec, dtype='float16')
levels.head()
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
      <th>70.000000</th>
      <th>70.039101</th>
      <th>70.078201</th>
      <th>70.117302</th>
      <th>70.156403</th>
      <th>70.195503</th>
      <th>70.234604</th>
      <th>70.273705</th>
      <th>70.312805</th>
      <th>70.351906</th>
      <th>...</th>
      <th>109.648094</th>
      <th>109.687195</th>
      <th>109.726295</th>
      <th>109.765396</th>
      <th>109.804497</th>
      <th>109.843597</th>
      <th>109.882698</th>
      <th>109.921799</th>
      <th>109.960899</th>
      <th>110.000000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>31.5</td>
      <td>30.5</td>
      <td>32.0</td>
      <td>37.5</td>
      <td>36.5</td>
      <td>34.5</td>
      <td>35.0</td>
      <td>33.5</td>
      <td>33.0</td>
      <td>33.5</td>
      <td>...</td>
      <td>19.0</td>
      <td>19.0</td>
      <td>20.5</td>
      <td>21.0</td>
      <td>19.5</td>
      <td>8.0</td>
      <td>1.0</td>
      <td>19.5</td>
      <td>22.5</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>30.5</td>
      <td>32.0</td>
      <td>31.5</td>
      <td>27.5</td>
      <td>29.5</td>
      <td>29.0</td>
      <td>27.5</td>
      <td>27.5</td>
      <td>27.5</td>
      <td>29.5</td>
      <td>...</td>
      <td>16.5</td>
      <td>11.5</td>
      <td>20.0</td>
      <td>20.5</td>
      <td>14.5</td>
      <td>17.0</td>
      <td>20.0</td>
      <td>19.5</td>
      <td>18.0</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31.5</td>
      <td>28.5</td>
      <td>29.0</td>
      <td>33.0</td>
      <td>31.0</td>
      <td>29.0</td>
      <td>29.5</td>
      <td>31.0</td>
      <td>30.0</td>
      <td>33.0</td>
      <td>...</td>
      <td>13.5</td>
      <td>14.5</td>
      <td>17.5</td>
      <td>16.5</td>
      <td>6.0</td>
      <td>20.5</td>
      <td>20.5</td>
      <td>20.5</td>
      <td>19.5</td>
      <td>17.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31.5</td>
      <td>31.5</td>
      <td>31.5</td>
      <td>32.0</td>
      <td>33.5</td>
      <td>35.0</td>
      <td>34.0</td>
      <td>33.5</td>
      <td>33.0</td>
      <td>33.5</td>
      <td>...</td>
      <td>21.0</td>
      <td>19.5</td>
      <td>21.0</td>
      <td>23.5</td>
      <td>20.5</td>
      <td>20.0</td>
      <td>23.0</td>
      <td>22.0</td>
      <td>19.5</td>
      <td>16.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.5</td>
      <td>26.5</td>
      <td>31.0</td>
      <td>30.0</td>
      <td>30.0</td>
      <td>31.0</td>
      <td>30.5</td>
      <td>27.5</td>
      <td>26.0</td>
      <td>27.5</td>
      <td>...</td>
      <td>10.0</td>
      <td>0.5</td>
      <td>9.5</td>
      <td>14.0</td>
      <td>19.0</td>
      <td>21.0</td>
      <td>10.5</td>
      <td>20.0</td>
      <td>23.0</td>
      <td>22.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 1024 columns</p>
</div>



## Processamento, Extração e Salvamento dos Metadados e Espectro 
A função a seguir é um wrapper de toda funcionalidade desta biblioteca. Ela recebe o caminho `entrada` para um arquivo `.bin` ou pasta contendo vários arquivos `.bin`, extrai os metadados e os dados de espectro. Mescla o timestamp dos metadados com o arquivo de espectro e salva ambos na pasta `saida`. Essa pasta é usada como repositório e cache dos dados processados que serão utilizados pela função `extract_bin_stats`.


```python
from rfpye.filter import process_bin, extract_bin_stats
```


```python
process_bin(bin_file, saida)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000; font-weight: bold">─────────────────────────── </span>Lista de Arquivos a serem processados<span style="color: #800000; text-decoration-color: #800000; font-weight: bold"> ───────────────────────────</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'RFeye002310_210520_T181500.bin'</span><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">]                                                           </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">😴 Nenhum arquivo novo a processar 💤
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">☝ use --substituir no terminal ou <span style="color: #808000; text-decoration-color: #808000">substituir</span>=<span style="color: #00ff00; text-decoration-color: #00ff00; font-style: italic">True</span> na chamada caso queira reprocessar os bins 
e sobrepôr os arquivos existentes 😉
</pre>



Como vemos pela mensagem de saída, nada foi feito porque esse arquivo já foi processado anteriormente e todos os arquivos de metadados e espectros presentes já foram salvos na pasta `saida`

## Resumo do arquivo
Se o que interessa é somente os dados estatísticos do arquivo como `Min`, `Max` e `Mean` basta utilizar:


```python
stats = extract_bin_stats(bin_file, cache=saida)
stats
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
      <th>Frequency</th>
      <th>Min</th>
      <th>Max</th>
      <th>Mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50.000000</td>
      <td>-7.0</td>
      <td>36.0</td>
      <td>22.484375</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50.039101</td>
      <td>3.0</td>
      <td>37.5</td>
      <td>22.640625</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50.078201</td>
      <td>-3.5</td>
      <td>38.5</td>
      <td>22.593750</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50.117302</td>
      <td>-2.0</td>
      <td>35.0</td>
      <td>22.765625</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50.156403</td>
      <td>5.5</td>
      <td>33.0</td>
      <td>22.781250</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>26875</th>
      <td>1218.844360</td>
      <td>-137.0</td>
      <td>-102.5</td>
      <td>-112.500000</td>
    </tr>
    <tr>
      <th>26876</th>
      <td>1218.883301</td>
      <td>-146.5</td>
      <td>-101.0</td>
      <td>-113.000000</td>
    </tr>
    <tr>
      <th>26877</th>
      <td>1218.922119</td>
      <td>-136.5</td>
      <td>-96.5</td>
      <td>-112.500000</td>
    </tr>
    <tr>
      <th>26878</th>
      <td>1218.961060</td>
      <td>-142.0</td>
      <td>-95.0</td>
      <td>-112.312500</td>
    </tr>
    <tr>
      <th>26879</th>
      <td>1219.000000</td>
      <td>-146.0</td>
      <td>-96.5</td>
      <td>-112.500000</td>
    </tr>
  </tbody>
</table>
<p>26880 rows × 4 columns</p>
</div>



Podemos filtrar o intervalo tanto de frequência quanto de tempo da extração:


```python
stats = extract_bin_stats(bin_file, cache=saida, freq_start=88, freq_stop=108)
stats
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
      <th>Frequency</th>
      <th>Min</th>
      <th>Max</th>
      <th>Mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>88.005867</td>
      <td>1.0</td>
      <td>33.0</td>
      <td>21.109375</td>
    </tr>
    <tr>
      <th>1</th>
      <td>88.044968</td>
      <td>-6.5</td>
      <td>37.5</td>
      <td>24.031250</td>
    </tr>
    <tr>
      <th>2</th>
      <td>88.084068</td>
      <td>4.5</td>
      <td>36.5</td>
      <td>24.234375</td>
    </tr>
    <tr>
      <th>3</th>
      <td>88.123169</td>
      <td>2.0</td>
      <td>41.0</td>
      <td>26.328125</td>
    </tr>
    <tr>
      <th>4</th>
      <td>88.162270</td>
      <td>2.0</td>
      <td>37.5</td>
      <td>26.421875</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>866</th>
      <td>107.959808</td>
      <td>-6.0</td>
      <td>30.0</td>
      <td>18.140625</td>
    </tr>
    <tr>
      <th>867</th>
      <td>107.969582</td>
      <td>-140.0</td>
      <td>-87.5</td>
      <td>-105.562500</td>
    </tr>
    <tr>
      <th>868</th>
      <td>107.979347</td>
      <td>-143.5</td>
      <td>-92.0</td>
      <td>-105.875000</td>
    </tr>
    <tr>
      <th>869</th>
      <td>107.989113</td>
      <td>-140.5</td>
      <td>-94.0</td>
      <td>-105.875000</td>
    </tr>
    <tr>
      <th>870</th>
      <td>107.998886</td>
      <td>-133.5</td>
      <td>-94.5</td>
      <td>-106.000000</td>
    </tr>
  </tbody>
</table>
<p>871 rows × 4 columns</p>
</div>


