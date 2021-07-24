# RFPYE
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca <a href='https://fastcore.fast.ai/basics.html'>fastcore</a>, que expande e otimiza as estruturas de dados da linguagem python. 


```python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
from rich import print
```

## Instalação

`Ubuntu`: 

```bash
python -m pip install rfpye
```

`Windows`:

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
entrada = Path(r'D:\OneDrive - ANATEL\Backup_Rfeye_SP\CGH\2021')
saida = Path(r'C:\Users\rsilva\Downloads\saida')
```

## Leitura de Arquivos

No módulo `parser.py`, há funções auxiliares para lidar com os arquivos `.bin`, pastas e para processar tais arquivos em formatos úteis. Nesse caso utilizaremos a função `get_files` que busca de maneira recursiva arquivos de dada extensão, inclusive links simbólicos se existirem
O caráter recursivo e a busca em links, `recurse` e `followlinks` simbólicos pode ser desativados por meio dos parâmetros e opcionalmente pode ser varrido somente o conjunto de pastas indicado em `folders` 

```python
from rfpye.utils import get_files
arquivos = get_files(entrada, extensions=['.bin']) ; print(arquivos[:10])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[</span>Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210319_T160137.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210325_T230001.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210401_T060001.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210404_T152752.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210410_T222501.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210416_T104037.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210422_T113942.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210428_T183501.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210505_T013201.bin'</span><span style="font-weight: bold">)</span>, 
Path<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'D:/OneDrive - </span>
<span style="color: #008000; text-decoration-color: #008000">ANATEL/Backup_Rfeye_SP/CGH/2021/rfeye002279-SP-Congonhas_210511_T083001.bin'</span><span style="font-weight: bold">)]</span>
</pre>



> O Objeto retornado `L` é uma extensão da lista python com funcionalidades adicionais, uma delas como  podemos ver é que a representação da lista impressa mostra o comprimento da lista. Esse objeto pode ser usado de maneira idêntica à uma lista em python e sem substituição desta.

```python
bin_file = arquivos[-3] ; print(bin_file.name)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">rfeye002279-SP-Congonhas_210516_T144208.bin
</pre>



```python
from rfpye.parser import parse_bin, extract_metadata, extract_level
```

## Processamento dos blocos
A função seguinte `parse_bin` recebe um arquivo `.bin` e mapeia os blocos contidos nele retornando um dicionário que tem como chave o tipo de bloco e os valores como uma lista com os blocos extraídos sequencialmente.

```python
%%time
map_bin = parse_bin(bin_file)['blocks']
```

    Wall time: 5.26 s
    

```python
for k, b in map_bin.items():
    print(f'Tipo de Bloco: {k[0]}, Fluxo (Thread ID): {k[1]}, #Blocos: {len(b)}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6341</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6341</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">310</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6341</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">100</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1268</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1268</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1268</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">230</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">240</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">360</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">380</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">423</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Tipo de Bloco: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, Fluxo <span style="font-weight: bold">(</span>Thread ID<span style="font-weight: bold">)</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, #Blocos: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>
</pre>



```python
gps = map_bin[(40,1)]
spec = map_bin[(67,110)]
```

A seguir é mostrado um exemplo dos atributos contidos num bloco de gps e num bloco de espectro

```python
from rfpye.utils import getattrs
print(getattrs(gps[0][1]))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">815.3</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_size'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps_datetime'</span>: datetime.datetime<span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">16</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">43</span><span style="font-weight: bold">)</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps_status'</span>: <span style="color: #008000; text-decoration-color: #008000">'Differential GPS'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'heading'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.635858</span>,
    <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-46.654255</span>,
    <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>,
    <span style="color: #008000; text-decoration-color: #008000">'speed'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.014</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'wallclock_datetime'</span>: numpy.datetime64<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'2021-05-16T14:43:00.532926'</span><span style="font-weight: bold">)</span>
<span style="font-weight: bold">}</span>
</pre>



```python
print(getattrs(spec[0][1]))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'antenna_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_size'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1164</span>,
    <span style="color: #008000; text-decoration-color: #008000">'data_type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'desclen'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">36</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 2 de 4).'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'dynamic_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gerror'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gflags'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'group_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'minimum'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-32.5</span>,
    <span style="color: #008000; text-decoration-color: #008000">'n_agc'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>,
    <span style="color: #008000; text-decoration-color: #008000">'n_tunning'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>,
    <span style="color: #008000; text-decoration-color: #008000">'namal'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'ndata'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>,
    <span style="color: #008000; text-decoration-color: #008000">'npad'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>,
    <span style="color: #008000; text-decoration-color: #008000">'offset'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">95</span>,
    <span style="color: #008000; text-decoration-color: #008000">'padding'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'processing'</span>: <span style="color: #008000; text-decoration-color: #008000">'peak'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'resolution_bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>,
    <span style="color: #008000; text-decoration-color: #008000">'sample'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6230</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">139</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_channel'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mili'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'step'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.039100684261974585</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1163</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_channel'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mili'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>,
    <span style="color: #008000; text-decoration-color: #008000">'wallclock_datetime'</span>: numpy.datetime64<span style="font-weight: bold">(</span><span style="color: #008000; text-decoration-color: #008000">'2021-05-16T14:45:00.790881'</span><span style="font-weight: bold">)</span>
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
      <th>2021-05-16 14:43:00.532926</th>
      <td>344</td>
      <td>399</td>
      <td>815.299988</td>
      <td>40</td>
      <td>2021-05-16 14:43:00</td>
      <td>Differential GPS</td>
      <td>0.0</td>
      <td>-23.635859</td>
      <td>-46.654255</td>
      <td>12</td>
      <td>0.014</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-16 14:44:00.330070</th>
      <td>5324</td>
      <td>5379</td>
      <td>817.299988</td>
      <td>40</td>
      <td>2021-05-16 14:43:59</td>
      <td>Differential GPS</td>
      <td>0.0</td>
      <td>-23.635857</td>
      <td>-46.654263</td>
      <td>12</td>
      <td>0.025</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-16 14:45:00.752895</th>
      <td>10304</td>
      <td>10359</td>
      <td>816.200012</td>
      <td>40</td>
      <td>2021-05-16 14:45:00</td>
      <td>Differential GPS</td>
      <td>0.0</td>
      <td>-23.635859</td>
      <td>-46.654266</td>
      <td>12</td>
      <td>0.007</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-16 14:46:00.402776</th>
      <td>86092</td>
      <td>86147</td>
      <td>815.299988</td>
      <td>40</td>
      <td>2021-05-16 14:46:00</td>
      <td>Differential GPS</td>
      <td>0.0</td>
      <td>-23.635864</td>
      <td>-46.654263</td>
      <td>12</td>
      <td>0.005</td>
      <td>1</td>
      <td>40</td>
    </tr>
    <tr>
      <th>2021-05-16 14:47:00.302816</th>
      <td>91072</td>
      <td>91127</td>
      <td>818.099976</td>
      <td>40</td>
      <td>2021-05-16 14:47:00</td>
      <td>Differential GPS</td>
      <td>0.0</td>
      <td>-23.635859</td>
      <td>-46.654266</td>
      <td>12</td>
      <td>0.025</td>
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
      <th>2021-05-21 00:00:00.695624</th>
      <td>69731068</td>
      <td>69732247</td>
      <td>0</td>
      <td>40</td>
      <td>1164</td>
      <td>1</td>
      <td>36</td>
      <td>PRD 2021 (Faixa principal 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1163</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>110</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-21 00:05:00.635638</th>
      <td>69826776</td>
      <td>69827955</td>
      <td>0</td>
      <td>40</td>
      <td>1164</td>
      <td>1</td>
      <td>36</td>
      <td>PRD 2021 (Faixa principal 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1163</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>110</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-21 00:10:00.606404</th>
      <td>69861632</td>
      <td>69862811</td>
      <td>0</td>
      <td>40</td>
      <td>1164</td>
      <td>1</td>
      <td>36</td>
      <td>PRD 2021 (Faixa principal 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1163</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>110</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-21 00:15:00.355210</th>
      <td>69896488</td>
      <td>69897667</td>
      <td>0</td>
      <td>40</td>
      <td>1164</td>
      <td>1</td>
      <td>36</td>
      <td>PRD 2021 (Faixa principal 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1163</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>110</td>
      <td>67</td>
    </tr>
    <tr>
      <th>2021-05-21 00:20:00.385654</th>
      <td>69992196</td>
      <td>69993375</td>
      <td>0</td>
      <td>40</td>
      <td>1164</td>
      <td>1</td>
      <td>36</td>
      <td>PRD 2021 (Faixa principal 2 de 4).</td>
      <td>0</td>
      <td>-1</td>
      <td>...</td>
      <td>0</td>
      <td>70</td>
      <td>0</td>
      <td>0.039101</td>
      <td>1163</td>
      <td>0</td>
      <td>110</td>
      <td>0</td>
      <td>110</td>
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
      <td>48.5</td>
      <td>47.5</td>
      <td>46.0</td>
      <td>42.5</td>
      <td>32.0</td>
      <td>39.0</td>
      <td>32.5</td>
      <td>41.0</td>
      <td>44.5</td>
      <td>45.5</td>
      <td>...</td>
      <td>34.0</td>
      <td>37.0</td>
      <td>38.5</td>
      <td>38.0</td>
      <td>32.5</td>
      <td>28.0</td>
      <td>36.0</td>
      <td>34.5</td>
      <td>27.5</td>
      <td>34.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>35.5</td>
      <td>35.5</td>
      <td>36.5</td>
      <td>46.0</td>
      <td>43.0</td>
      <td>44.5</td>
      <td>47.0</td>
      <td>45.5</td>
      <td>40.0</td>
      <td>38.5</td>
      <td>...</td>
      <td>35.5</td>
      <td>34.5</td>
      <td>31.0</td>
      <td>34.5</td>
      <td>35.5</td>
      <td>28.5</td>
      <td>21.5</td>
      <td>28.5</td>
      <td>27.0</td>
      <td>37.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>47.0</td>
      <td>44.5</td>
      <td>44.0</td>
      <td>41.5</td>
      <td>40.5</td>
      <td>42.0</td>
      <td>40.0</td>
      <td>40.0</td>
      <td>43.0</td>
      <td>39.5</td>
      <td>...</td>
      <td>31.0</td>
      <td>38.0</td>
      <td>41.5</td>
      <td>38.5</td>
      <td>31.0</td>
      <td>31.0</td>
      <td>31.0</td>
      <td>39.5</td>
      <td>39.5</td>
      <td>37.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40.0</td>
      <td>43.0</td>
      <td>42.0</td>
      <td>46.5</td>
      <td>45.5</td>
      <td>40.5</td>
      <td>35.0</td>
      <td>35.0</td>
      <td>37.5</td>
      <td>37.0</td>
      <td>...</td>
      <td>37.0</td>
      <td>38.5</td>
      <td>39.0</td>
      <td>35.5</td>
      <td>36.5</td>
      <td>32.5</td>
      <td>26.5</td>
      <td>33.5</td>
      <td>35.5</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40.0</td>
      <td>35.0</td>
      <td>32.0</td>
      <td>42.0</td>
      <td>41.0</td>
      <td>40.5</td>
      <td>36.5</td>
      <td>32.5</td>
      <td>46.0</td>
      <td>47.5</td>
      <td>...</td>
      <td>31.0</td>
      <td>28.0</td>
      <td>41.0</td>
      <td>42.5</td>
      <td>39.0</td>
      <td>31.0</td>
      <td>25.0</td>
      <td>16.5</td>
      <td>23.0</td>
      <td>23.0</td>
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




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'rfeye002279-SP-Congonhas_210516_T144208.bin'</span><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">]                                              </span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">Processando Blocos de: </span><span style="color: #800000; text-decoration-color: #800000">rfeye002279-SP-Congonhas_210516_T144208.bin</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080">Extraindo Metadados de: </span><span style="color: #800000; text-decoration-color: #800000">rfeye002279-SP-Congonhas_210516_T144208.bin</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"></pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">kbô 😆
</pre>



Se chamarmos a função novamente:

```python
process_bin(bin_file, saida)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800000; text-decoration-color: #800000; font-weight: bold">─────────────────────────── </span>Lista de Arquivos a serem processados<span style="color: #800000; text-decoration-color: #800000; font-weight: bold"> ───────────────────────────</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'rfeye002279-SP-Congonhas_210516_T144208.bin'</span><span style="color: #c0c0c0; text-decoration-color: #c0c0c0; font-weight: bold">]                                              </span>
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
      <td>18.0</td>
      <td>48.5</td>
      <td>37.81250</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50.039101</td>
      <td>10.5</td>
      <td>49.0</td>
      <td>37.62500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>50.078201</td>
      <td>8.5</td>
      <td>48.5</td>
      <td>37.59375</td>
    </tr>
    <tr>
      <th>3</th>
      <td>50.117302</td>
      <td>17.5</td>
      <td>49.5</td>
      <td>37.96875</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50.156403</td>
      <td>17.5</td>
      <td>50.0</td>
      <td>38.00000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>43003</th>
      <td>5159.843750</td>
      <td>-128.5</td>
      <td>-104.0</td>
      <td>-112.43750</td>
    </tr>
    <tr>
      <th>43004</th>
      <td>5159.882812</td>
      <td>-125.0</td>
      <td>-103.5</td>
      <td>-112.25000</td>
    </tr>
    <tr>
      <th>43005</th>
      <td>5159.921875</td>
      <td>-127.0</td>
      <td>-101.5</td>
      <td>-111.37500</td>
    </tr>
    <tr>
      <th>43006</th>
      <td>5159.960938</td>
      <td>-123.5</td>
      <td>-101.0</td>
      <td>-111.12500</td>
    </tr>
    <tr>
      <th>43007</th>
      <td>5160.000000</td>
      <td>-125.5</td>
      <td>-103.5</td>
      <td>-112.06250</td>
    </tr>
  </tbody>
</table>
<p>43008 rows × 4 columns</p>
</div>



Podemos filtrar o intervalo tanto de frequência quanto de tempo da extração:

```python
stats = extract_bin_stats(bin_file, cache=saida, freq_start=88.1, freq_stop=107.9)
print(stats.head(20))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">    Frequency   Min   Max      Mean
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.123169</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">69.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">96.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">89.43750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.162270</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">65.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">96.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">89.43750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.201370</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">53.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">96.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">83.62500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.240471</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">95.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">83.81250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.279572</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">37.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">95.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">71.93750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.318672</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">34.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">94.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">72.37500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.357773</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">28.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">87.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57.40625</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.396873</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">85.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">57.90625</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.435974</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">24.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">71.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46.00000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.475075</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">24.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46.40625</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.514175</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">55.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40.71875</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.553276</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">55.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">40.93750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.592377</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">53.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">38.06250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.631477</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">17.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">56.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">38.28125</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.670578</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">16.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">41.59375</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.709679</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">41.90625</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">16</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.748779</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">49.96875</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">17</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.787880</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">17.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50.25000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.826981</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">28.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">54.37500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">19</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">88.866081</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">31.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">54.68750</span>
</pre>



```python
print(stats.tail(20))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">      Frequency    Min   Max      Mean
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">833</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.705833</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-133.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-64.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.00000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">834</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.715599</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-120.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-62.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88.81250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">835</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.725372</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-117.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-60.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88.00000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">836</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.735138</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">19.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">75.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46.31250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">837</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.744904</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-128.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-58.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86.68750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">838</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.754677</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-121.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-57.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-84.31250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">839</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.764442</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-116.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-49.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-80.68750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">840</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.774208</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-120.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-41.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-76.37500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">841</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.783981</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">79.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">59.62500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">842</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.793747</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-121.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-72.37500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">843</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.803520</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-115.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-69.00000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">844</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.813286</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-116.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-66.68750</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">845</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.823051</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-118.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-40.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-65.12500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">846</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.832825</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">25.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">79.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">69.31250</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">847</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.842590</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-124.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-42.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-62.59375</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">848</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.852356</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-41.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-59.12500</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">849</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.862129</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-119.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-55.75000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">850</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.871895</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-110.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-53.15625</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">851</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.881660</span>   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">43.0</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">81.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73.25000</span>
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">852</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">107.891434</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-37.0</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-51.71875</span>
</pre>


