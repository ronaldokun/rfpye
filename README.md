# RFPYE
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca <a href='https://fastcore.fast.ai/basics.html'>fastcore</a>, que expande e otimiza as estruturas de dados da linguagem python. 


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

Precisamos necessariamente de um diretório de entrada, contendo um ou mais arquivos `.bin`
> Mude os caminhos abaixo para suas pastas locais

```python
from fastcore.xtras import Path
from rfpye.utils import get_files
from rich import print
```

A função abaixo baixa alguns arquivos de exemplo:

```python
path = Path(r'binfiles')
if not path.exists() or not len(get_files(path, extensions=['.bin'])):
    path = Path('.')
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T202310_CRFSBINv.5.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T202310_CRFSBINv.5.bin' --output-document 'rfeye002092_210208_T202310_CRFSBINv.5.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T203131_CRFSBINv.2.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T203131_CRFSBINv.2.bin' --output-document 'rfeye002092_210208_T203131_CRFSBINv.2.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T202215_CRFSBINv.4.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T202215_CRFSBINv.4.bin' --output-document 'rfeye002292_210208_T202215_CRFSBINv.4.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T203238_CRFSBINv.3.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T203238_CRFSBINv.3.bin' --output-document 'rfeye002292_210208_T203238_CRFSBINv.3.bin'

```

A função `parse_bin` é a função principal que encapsula o processamento dos arquivos bin.


<h4 id="parse_bin" class="doc_header"><code>parse_bin</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/parser.py#L252" class="source_link" style="float:right">[source]</a></h4>

> <code>parse_bin</code>(**`bin_file`**:`Union`\[`str`, `Path`\])

Receives a CRFS binfile and returns a dictionary with the file metadata, a GPS Class and a list with the different Spectrum Classes
A block is a piece of the .bin file with a known start and end and that contains different types of information.
It has several fields: file_type, header, data and footer.
Each field has lengths and information defined in the documentation.
Args:
    bin_file (Union[str, Path]): path to the bin file

Returns:
    Dictionary with the file metadata, file_version, string info, gps and spectrum blocks.


## CRFS Bin - Versão 5
Vamos listar arquivos da última versão do script Logger, Versão 5

```python
files = get_files(r'D:\OneDrive - ANATEL\Sensores', extensions=['.bin'])
files
```




    (#65) [Path('D:/OneDrive - ANATEL/Sensores/rfeye002073/rfeye002073_210620_T231206.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002080/rfeye002080_691231_T210111.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002081/rfeye002081_210620_T232204.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002083/rfeye002083_210621_T160001.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002084/rfeye002084_210623_T144012.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002086/rfeye002086_210622_T004723.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002087/rfeye002087_210628_T224301.bin'),Path('D:/OneDrive - ANATEL/Sensores/RFeye002090-VCP/rfeye002090-VCP_210623_T024236.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002091/rfeye002091_210618_T145747.bin'),Path('D:/OneDrive - ANATEL/Sensores/rfeye002092/rfeye002092_210603_T205009.bin')...]



```python
file = files.shuffle()[0]
```

```python
%%time
v5 = parse_bin(file)
```

    Wall time: 13.2 s
    

```python
print(v5)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002166_210620_T115535.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">23</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V023'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002166'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'ScriptRFeye2021_v2.cfg'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'INFO'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.56443</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-55.68867</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">661.90</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span> ,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">310</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">155.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">165.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 1 de 4).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">90.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-65.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-65.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD</span>
<span style="color: #008000; text-decoration-color: #008000">2021 (Faixa principal 2 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>,
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-53.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-53.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 3 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">170.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-66.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-66.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">principal 4 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">470.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5888</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-65.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-65.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">200</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 1 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 2 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1710.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1980.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6912</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 3 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2100.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002168.999</span>, 
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1792</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">230</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 4 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2290.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2390.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2560</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">240</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 5 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2500.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4864</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 3 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">330</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 4 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001218.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">350</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 6 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001388.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001428.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">360</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001648.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">370</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 8 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002898.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">380</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 9 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5000.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5160.0</span>,
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4096</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">390</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 10 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005338.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005458.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3328</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">250</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 6 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3290.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3700.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10496</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



A saída da função é um dicionário, com os metadados do arquivo:

![image.png](nbs\attachment:83a77abf-8623-4f82-ae74-8a0d077b1aa8.png)

No entanto as duas chaves mais importantes do dicionário retornado são `gps` e `spectrum`

```python
from rfpye.utils import getattrs

print(getattrs(v5['gps']))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">661.9</span>, <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.564427</span>, <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-55.688672</span>, <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span><span style="font-weight: bold">}</span>
</pre>



Se você imprimir a classe retornada pela chave `gps` é retornado um resumo dos seus atributos:

```python
print(v5['gps'])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.56443</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-55.68867</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">661.90</span> #Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span> 
</pre>



Os atributos listados são os valores consolidados por meio da __mediana__ dos diversos blocos de GPS do arquivo. 

> Caso desejar a lista original de valores, os atributos são os mesmos mas precedidos de `_`, o que os torna __atributos privados__ em python, isso somente quer dizer que não são explicitados em algus métodos como `getattrs`, pois normalmente não são acessíveis diretamente, mas nada impede que sejam acessados.

```python
v5['gps']._latitude, v5['gps']._longitude, v5['gps']._altitude, v5['gps']._num_satellites 
```




    ((#9057) [-22.564446,-22.564431,-22.564439,-22.564445,-22.564439,-22.564445,-22.564449,-22.564439,-22.564428,-22.564426...],
     (#9057) [-55.688672,-55.688673,-55.688677,-55.688679,-55.688672,-55.688664,-55.688675,-55.688681,-55.688678,-55.688693...],
     (#9057) [660.4,662.2,660.5,661.9,665.2,662.9,660.1,658.2,660.1,662.0...],
     (#9057) [12,12,12,12,12,12,12,12,12,12...])



Cada arquivo bin normalmente possui vários fluxos de espectro distintos, cada fluxo espectral é uma classe Python, na chave `spectrum` é retornado uma lista com todos os fluxos de espectro.

Vamos investigar alguns deles:

```python
fluxo = v5['spectrum'][0]
```

Ao imprimir um fluxo é mostrado informações mínimas sobre o seu conteúdo:

```python
print(fluxo)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Blocks of Type : <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Thread_id: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span> and Span <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span> MHz - <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span> MHz
</pre>



A função `repr` retorna uma representação com todos os metadados do fluxo:

```python
print(repr(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>
</pre>



No entanto o principal atributo de um fluxo de espectro são os valores de nível medidos, os valores medidos são retornados por meio do atributo: `levels`:

```python
print(fluxo.levels)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-105.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-116.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-110</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-115</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-116</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-108</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-107</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-130</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-109.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-106.5</span><span style="font-weight: bold">]</span>
 <span style="color: #808000; text-decoration-color: #808000">...</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-103</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-108.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-114</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-104.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-110.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-96</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-106.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-103</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-110</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-109.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-104.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-108</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-106</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-111</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-113.5</span><span style="font-weight: bold">]]</span>
</pre>



```python
print(f'Formato da matriz com os níveis: {fluxo.levels.shape}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Formato da matriz com os níveis: <span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8963</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)</span>
</pre>



O nº de linhas da matriz nos dá o número de pontos medidos naquele dado fluxo e as colunas o número de traços no qual o Span ( Stop - Start ) foi dividido. O número de traços pode ser retornada também por meio da função `len`

```python
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8963</span>
</pre>



O atributo anterior retorna uma `numpy.ndarray`, que é um formato eficiente para processamento. 

No entanto temos adicionalmente o método `.matrix()` que retorna a matriz de dados como um _Pandas Dataframe_ formatada com o tempo da medição de cada traço como índice das linhas e as frequências de cada traço como coluna.

```python
fluxo.matrix()
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
      <th>Frequencies</th>
      <th>105.000000</th>
      <th>105.009768</th>
      <th>105.019537</th>
      <th>105.029305</th>
      <th>105.039073</th>
      <th>105.048842</th>
      <th>105.058610</th>
      <th>105.068378</th>
      <th>105.078147</th>
      <th>105.087915</th>
      <th>...</th>
      <th>139.912085</th>
      <th>139.921853</th>
      <th>139.931622</th>
      <th>139.941390</th>
      <th>139.951158</th>
      <th>139.960927</th>
      <th>139.970695</th>
      <th>139.980463</th>
      <th>139.990232</th>
      <th>140.000000</th>
    </tr>
    <tr>
      <th>Time</th>
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
      <th>2021-06-20 11:56:00.734894</th>
      <td>-99.0</td>
      <td>-113.5</td>
      <td>-113.5</td>
      <td>-116.0</td>
      <td>-113.5</td>
      <td>-114.0</td>
      <td>-115.0</td>
      <td>-112.0</td>
      <td>-113.0</td>
      <td>-113.5</td>
      <td>...</td>
      <td>-105.0</td>
      <td>-105.0</td>
      <td>-105.0</td>
      <td>-105.5</td>
      <td>-111.5</td>
      <td>-109.5</td>
      <td>-105.5</td>
      <td>-105.5</td>
      <td>-113.0</td>
      <td>-116.5</td>
    </tr>
    <tr>
      <th>2021-06-20 11:57:00.734925</th>
      <td>-111.5</td>
      <td>-110.0</td>
      <td>-115.0</td>
      <td>-129.5</td>
      <td>-124.0</td>
      <td>-114.5</td>
      <td>-112.5</td>
      <td>-114.5</td>
      <td>-116.0</td>
      <td>-121.5</td>
      <td>...</td>
      <td>-105.0</td>
      <td>-101.0</td>
      <td>-100.5</td>
      <td>-104.0</td>
      <td>-107.0</td>
      <td>-105.5</td>
      <td>-112.5</td>
      <td>-116.0</td>
      <td>-111.0</td>
      <td>-108.0</td>
    </tr>
    <tr>
      <th>2021-06-20 11:58:00.734953</th>
      <td>-107.0</td>
      <td>-111.5</td>
      <td>-130.0</td>
      <td>-113.0</td>
      <td>-107.0</td>
      <td>-107.5</td>
      <td>-110.5</td>
      <td>-115.0</td>
      <td>-127.5</td>
      <td>-109.5</td>
      <td>...</td>
      <td>-104.5</td>
      <td>-107.0</td>
      <td>-108.0</td>
      <td>-110.0</td>
      <td>-108.0</td>
      <td>-105.5</td>
      <td>-119.5</td>
      <td>-113.5</td>
      <td>-109.5</td>
      <td>-106.5</td>
    </tr>
    <tr>
      <th>2021-06-20 11:59:00.735716</th>
      <td>-107.0</td>
      <td>-114.0</td>
      <td>-115.0</td>
      <td>-96.5</td>
      <td>-111.5</td>
      <td>-119.0</td>
      <td>-116.5</td>
      <td>-113.5</td>
      <td>-117.0</td>
      <td>-122.0</td>
      <td>...</td>
      <td>-109.5</td>
      <td>-105.5</td>
      <td>-102.5</td>
      <td>-104.0</td>
      <td>-110.5</td>
      <td>-116.5</td>
      <td>-111.5</td>
      <td>-111.5</td>
      <td>-111.0</td>
      <td>-108.0</td>
    </tr>
    <tr>
      <th>2021-06-20 12:00:00.736139</th>
      <td>-85.5</td>
      <td>-90.0</td>
      <td>-97.0</td>
      <td>-102.5</td>
      <td>-110.0</td>
      <td>-114.0</td>
      <td>-117.5</td>
      <td>-117.0</td>
      <td>-110.5</td>
      <td>-112.0</td>
      <td>...</td>
      <td>-108.5</td>
      <td>-112.5</td>
      <td>-120.0</td>
      <td>-115.5</td>
      <td>-111.5</td>
      <td>-115.5</td>
      <td>-112.0</td>
      <td>-114.5</td>
      <td>-122.0</td>
      <td>-111.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2021-06-26 18:47:00.734834</th>
      <td>-114.0</td>
      <td>-112.0</td>
      <td>-111.0</td>
      <td>-111.0</td>
      <td>-111.5</td>
      <td>-110.0</td>
      <td>-108.5</td>
      <td>-114.0</td>
      <td>-122.0</td>
      <td>-116.0</td>
      <td>...</td>
      <td>-106.5</td>
      <td>-105.5</td>
      <td>-105.0</td>
      <td>-105.0</td>
      <td>-103.5</td>
      <td>-101.5</td>
      <td>-103.5</td>
      <td>-101.5</td>
      <td>-102.0</td>
      <td>-103.0</td>
    </tr>
    <tr>
      <th>2021-06-26 18:48:00.734868</th>
      <td>-110.5</td>
      <td>-111.5</td>
      <td>-124.5</td>
      <td>-113.5</td>
      <td>-104.5</td>
      <td>-102.5</td>
      <td>-115.0</td>
      <td>-116.0</td>
      <td>-113.5</td>
      <td>-112.5</td>
      <td>...</td>
      <td>-107.0</td>
      <td>-107.5</td>
      <td>-108.5</td>
      <td>-106.5</td>
      <td>-104.5</td>
      <td>-104.0</td>
      <td>-105.0</td>
      <td>-108.0</td>
      <td>-109.0</td>
      <td>-106.0</td>
    </tr>
    <tr>
      <th>2021-06-26 18:49:00.734831</th>
      <td>-103.0</td>
      <td>-108.5</td>
      <td>-114.0</td>
      <td>-111.5</td>
      <td>-116.0</td>
      <td>-117.0</td>
      <td>-111.0</td>
      <td>-109.5</td>
      <td>-110.0</td>
      <td>-108.5</td>
      <td>...</td>
      <td>-112.5</td>
      <td>-110.0</td>
      <td>-108.5</td>
      <td>-112.5</td>
      <td>-105.5</td>
      <td>-100.0</td>
      <td>-99.5</td>
      <td>-104.5</td>
      <td>-110.5</td>
      <td>-111.5</td>
    </tr>
    <tr>
      <th>2021-06-26 18:50:00.734916</th>
      <td>-96.0</td>
      <td>-106.5</td>
      <td>-103.0</td>
      <td>-114.0</td>
      <td>-113.0</td>
      <td>-108.5</td>
      <td>-105.5</td>
      <td>-105.5</td>
      <td>-105.5</td>
      <td>-105.0</td>
      <td>...</td>
      <td>-108.0</td>
      <td>-107.5</td>
      <td>-105.5</td>
      <td>-112.0</td>
      <td>-106.0</td>
      <td>-103.5</td>
      <td>-129.0</td>
      <td>-110.0</td>
      <td>-109.5</td>
      <td>-113.0</td>
    </tr>
    <tr>
      <th>2021-06-26 18:52:00.734862</th>
      <td>-104.5</td>
      <td>-108.0</td>
      <td>-111.0</td>
      <td>-108.5</td>
      <td>-108.5</td>
      <td>-108.0</td>
      <td>-105.5</td>
      <td>-106.0</td>
      <td>-109.0</td>
      <td>-109.5</td>
      <td>...</td>
      <td>-110.0</td>
      <td>-111.5</td>
      <td>-102.0</td>
      <td>-99.0</td>
      <td>-102.0</td>
      <td>-105.5</td>
      <td>-106.5</td>
      <td>-106.0</td>
      <td>-111.0</td>
      <td>-113.5</td>
    </tr>
  </tbody>
</table>
<p>8963 rows × 3584 columns</p>
</div>


