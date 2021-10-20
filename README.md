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


<h4 id="parse_bin" class="doc_header"><code>parse_bin</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/parser.py#L35" class="source_link" style="float:right">[source]</a></h4>

> <code>parse_bin</code>(**`bin_file`**:`Union`\[`str`, `Path`\])

Receives a CRFS binfile and returns a dictionary with the file metadata, a GPS Class and a list with the different Spectrum Classes
A block is a piece of the .bin file with a known start and end and that contains different types of information.
It has several fields: file_type, header, data and footer.
Each field has lengths and information defined in the documentation.
Args:
    bin_file (Union[str, Path]): path to the bin file

Returns:
    Dictionary with the file metadata, file_version, string info, gps and spectrum blocks.


## Extração de Dados

Vamos listar arquivos da última versão do script Logger, **CRFS Bin - Versão 5**

```python
files = get_files(r'D:\OneDrive - ANATEL\Sensores', extensions=['.bin'])
file = files.shuffle()[0]
```

```python
%%time
dados = parse_bin(file)
```

    Wall time: 13.2 s
    

```python
print(dados)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002130_210622_T151702.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">23</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V023'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002130'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'ScriptRFeye2021_v.1'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'INFO'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-10.68619</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-37.43918</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210.10</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span> ,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">310</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">155.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">165.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 1 de 4).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">90.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-70.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-70.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD</span>
<span style="color: #008000; text-decoration-color: #008000">2021 (Faixa principal 2 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>,
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-29.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-29.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 3 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">170.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-69.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-69.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">principal 4 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">470.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5888</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-42.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-42.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
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
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">250</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 6 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3290.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3700.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10496</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 3 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">330</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 4 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001218.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>,
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">350</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 6 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001388.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001428.999</span>, 
<span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">360</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001648.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">370</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 8 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002898.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">380</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 9 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5000.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5160.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4096</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">390</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 10 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005338.999</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005458.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3328</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



A saída da função é um dicionário, com os metadados do arquivo.

## GPS
No entanto as duas chaves mais importantes do dicionário retornado são `gps` e `spectrum`

Se você imprimir a classe retornada pela chave `gps` é retornado um resumo dos seus atributos:

```python
print(dados['gps'])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-10.68619</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-37.43918</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210.10</span> #Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span> 
</pre>



> Para extrair os atributos em si de dado objeto e retorná-los todos num dicionário, o módulo utils tem a função auxiliar `getattrs`


<h4 id="getattrs" class="doc_header"><code>getattrs</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/utils.py#L159" class="source_link" style="float:right">[source]</a></h4>

> <code>getattrs</code>(**`obj`**:`Any`, **`attrs`**:`Iterable`\[`T_co`\]=*`None`*)

Receives an object and return the atributes listed in `attrs`, if attrs is None return its public attributes


```python
print(getattrs(dados['gps']))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210.1</span>, <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-10.686185</span>, <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-37.43918</span>, <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span><span style="font-weight: bold">}</span>
</pre>



Os atributos listados são os valores consolidados por meio da __mediana__ dos diversos blocos de GPS do arquivo. 

### Dados Brutos de GPS
> Caso desejar a lista original de valores, os atributos são os mesmos mas precedidos de `_`, o que os torna __atributos privados__ em python, isso somente quer dizer que não são explicitados em algus métodos como `getattrs`, pois normalmente não são acessíveis diretamente, mas nada impede que sejam acessados.

```python
dados['gps']._latitude
```




    (#18116) [-10.686196,-10.686173,-10.686203,-10.686203,-10.686191,-10.686178,-10.686201,-10.686205,-10.686205,-10.686209...]



```python
dados['gps']._longitude
```




    (#18116) [-37.439175,-37.439172,-37.439143,-37.43916,-37.439191,-37.439171,-37.439177,-37.439192,-37.439172,-37.43917...]



```python
dados['gps']._altitude
```




    (#18116) [211.4,221.8,213.3,210.1,223.2,211.1,206.6,212.6,213.1,210.5...]



```python
dados['gps']._num_satellites 
```




    (#18116) [11,11,12,10,11,11,11,12,12,12...]



## Dados de Nível Espectral
Cada arquivo bin normalmente possui vários fluxos de espectro distintos, cada fluxo espectral é uma classe Python, na chave `spectrum` é retornado uma lista com todos os fluxos de espectro.

```python
fluxos = dados['spectrum']
print(len(fluxos))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>
</pre>



Vamos investigar um deles:

```python
fluxo = fluxos[0]
```

Ao imprimir um fluxo é mostrado informações mínimas sobre o seu conteúdo:

```python
print(fluxo)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Blocks of Type: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Thread_id: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, Start: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span> MHz, Stop: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span> MHz
</pre>



A função `repr` retorna uma representação com todos os metadados do fluxo:

```python
print(repr(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>
</pre>



Qualquer um dos atributos listados podem ser acessados diretamente:

```python
print(fluxo.description) , print(fluxo.bw)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">PMEC <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> <span style="font-weight: bold">(</span>Faixa <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span> de <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span><span style="font-weight: bold">)</span>.
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>
</pre>






    (None, None)



No entanto o principal atributo de um fluxo de espectro são os valores de nível medidos, os valores medidos são retornados por meio do atributo `levels`:

```python
print(fluxo.levels)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-93.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-93.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85.5</span><span style="font-weight: bold">]</span>
 <span style="color: #808000; text-decoration-color: #808000">...</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-93.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-96.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-93</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-95</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-89.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-94.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-94</span>. <span style="font-weight: bold">]]</span>
</pre>



```python
print(f'Formato da matriz com os níveis: {fluxo.levels.shape}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Formato da matriz com os níveis: <span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9058</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)</span>
</pre>



O nº de linhas da matriz nos dá o número de pontos medidos naquele dado fluxo e as colunas o número de traços no qual o Span ( Stop - Start ) foi dividido. O número de traços pode ser retornada também por meio da função `len`

```python
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9058</span>
</pre>



O atributo anterior retorna uma `numpy.ndarray`, que é um formato eficiente para processamento. 

### Medidas de nível como pandas dataframe
No entanto temos adicionalmente o método `.matrix()` que retorna a matriz de dados como um _Pandas Dataframe_ formatada com o tempo da medição de cada traço como índice das linhas e as frequências de cada traço como coluna.

Vamos mostrar as cinco primeiras e cinco últimas linhas e colunas. 

```python
fluxo.matrix().iloc[:5, :5]
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
    </tr>
    <tr>
      <th>Time</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-06-22 15:18:01.549012</th>
      <td>-93.5</td>
      <td>-99.5</td>
      <td>-90.5</td>
      <td>-90.0</td>
      <td>-92.0</td>
    </tr>
    <tr>
      <th>2021-06-22 15:19:01.408958</th>
      <td>-93.5</td>
      <td>-90.5</td>
      <td>-90.5</td>
      <td>-92.5</td>
      <td>-96.5</td>
    </tr>
    <tr>
      <th>2021-06-22 15:20:01.149028</th>
      <td>-90.5</td>
      <td>-86.5</td>
      <td>-86.5</td>
      <td>-95.0</td>
      <td>-86.5</td>
    </tr>
    <tr>
      <th>2021-06-22 15:21:00.968982</th>
      <td>-90.5</td>
      <td>-90.5</td>
      <td>-91.5</td>
      <td>-89.0</td>
      <td>-89.0</td>
    </tr>
    <tr>
      <th>2021-06-22 15:22:01.729287</th>
      <td>-91.0</td>
      <td>-90.0</td>
      <td>-86.5</td>
      <td>-91.0</td>
      <td>-93.0</td>
    </tr>
  </tbody>
</table>
</div>



```python
fluxo.matrix().iloc[-5:, -5:]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-06-28 22:11:01.172916</th>
      <td>-103.0</td>
      <td>-96.5</td>
      <td>-94.0</td>
      <td>-97.5</td>
      <td>-93.5</td>
    </tr>
    <tr>
      <th>2021-06-28 22:12:01.317300</th>
      <td>-92.0</td>
      <td>-95.0</td>
      <td>-93.5</td>
      <td>-93.0</td>
      <td>-92.0</td>
    </tr>
    <tr>
      <th>2021-06-28 22:13:01.742929</th>
      <td>-96.0</td>
      <td>-92.5</td>
      <td>-92.0</td>
      <td>-93.5</td>
      <td>-96.5</td>
    </tr>
    <tr>
      <th>2021-06-28 22:14:01.693040</th>
      <td>-94.5</td>
      <td>-93.0</td>
      <td>-92.5</td>
      <td>-91.5</td>
      <td>-91.0</td>
    </tr>
    <tr>
      <th>2021-06-28 22:15:01.614231</th>
      <td>-90.5</td>
      <td>-91.0</td>
      <td>-90.0</td>
      <td>-94.5</td>
      <td>-94.0</td>
    </tr>
  </tbody>
</table>
</div>



Novamente, caso desejado acessar todos os atributos de um fluxo no formato de dicionário, basta utilizar a função `getattrs`

```python
getattrs(fluxo)
```




    {'antenna_id': 0,
     'append': <bound method CrfsSpectrum.append of SpecData(type=67, thread_id=100, description='PRD 2021 (Faixa principal 1 de 4).', start_mega=50.0, stop_mega=90.0, unit='dBμV/m', ndata=1024, bw=73828, processing='peak', antenna_id=0, thresh=-35.5, minimum=-35.5)>,
     'bw': 73828,
     'description': 'PRD 2021 (Faixa principal 1 de 4).',
     'matrix': <bound method CrfsSpectrum.matrix of SpecData(type=67, thread_id=100, description='PRD 2021 (Faixa principal 1 de 4).', start_mega=50.0, stop_mega=90.0, unit='dBμV/m', ndata=1024, bw=73828, processing='peak', antenna_id=0, thresh=-35.5, minimum=-35.5)>,
     'minimum': -35.5,
     'ndata': 1024,
     'processing': 'peak',
     'start_mega': 50.0,
     'stop_mega': 90.0,
     'thread_id': 100,
     'thresh': -35.5,
     'timestamp': (#1812) [numpy.datetime64('2021-06-28T15:35:00.933900'),numpy.datetime64('2021-06-28T15:40:00.730000'),numpy.datetime64('2021-06-28T15:45:00.758300'),numpy.datetime64('2021-06-28T15:50:00.728300'),numpy.datetime64('2021-06-28T15:55:00.732700'),numpy.datetime64('2021-06-28T16:00:00.722200'),numpy.datetime64('2021-06-28T16:05:00.729500'),numpy.datetime64('2021-06-28T16:10:00.709200'),numpy.datetime64('2021-06-28T16:15:00.732700'),numpy.datetime64('2021-06-28T16:20:00.734800')...],
     'type': 67,
     'unit': 'dBμV/m'}



### CRFS Bin - Versão 5 - Arquivos Comprimidos
Vamos listar arquivos da última versão do script Logger, Versão 5, arquivos comprimidos onde o piso de ruído é suprimido.

```python
file = r'binfiles\compressed\rfeye002290_210922_T204046_MaskBroken.bin'
```

```python
%%time
compressed = parse_bin(file)
```

    Wall time: 9.97 s
    

```python
print(compressed)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002290_210922_T204046_MaskBroken.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">23</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V023'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002290'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'ScriptRFeye2021_v2.cfg'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'INFO'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.70008</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-47.66684</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">518.40</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span> ,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">321</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 3 de 10). @ </span>
<span style="color: #008000; text-decoration-color: #008000">-80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">301</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10). @ -80dBm, 10kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">137.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14848</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">341</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">5 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001218.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">311</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10). @ -80dBm, 10kHz.'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">156.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">163.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">371</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 8 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002898.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">351</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">6 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001388.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001428.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">331</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 4 de 10). @ -80dBm, 100kHz.'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">361</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001648.999</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```python
fluxo = compressed['spectrum'] ; fluxos
```




    (#8) [SpecData(type=68, thread_id=321, description='PMEC 2021 (Faixa 3 de 10). @ -80dBm, 100kHz.', start_mega=320.0, stop_mega=340.0, unit='dBm', ndata=512, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=301, description='PMEC 2021 (Faixa 1 de 10). @ -80dBm, 10kHz.', start_mega=108.0, stop_mega=137.0, unit='dBm', ndata=14848, bw=3690, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=341, description='PMEC 2021 (Faixa 5 de 10). @ -80dBm, 100kHz.', start_mega=960.0, stop_mega=1001218.999, unit='dBm', ndata=6656, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=311, description='PMEC 2021 (Faixa 2 de 10). @ -80dBm, 10kHz.', start_mega=156.0, stop_mega=163.0, unit='dBm', ndata=3584, bw=3690, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=371, description='PMEC 2021 (Faixa 8 de 10). @ -80dBm, 100kHz.', start_mega=2690.0, stop_mega=1002898.999, unit='dBm', ndata=5376, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=351, description='PMEC 2021 (Faixa 6 de 10). @ -80dBm, 100kHz.', start_mega=1001388.999, stop_mega=1001428.999, unit='dBm', ndata=1280, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=331, description='PMEC 2021 (Faixa 4 de 10). @ -80dBm, 100kHz.', start_mega=400.0, stop_mega=410.0, unit='dBm', ndata=256, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5),SpecData(type=68, thread_id=361, description='PMEC 2021 (Faixa 7 de 10). @ -80dBm, 100kHz.', start_mega=1530.0, stop_mega=1001648.999, unit='dBm', ndata=3072, bw=73828, processing='peak', antenna_id=0, thresh=-100, minimum=-147.5)]



```python
fluxo = fluxos[0]
fluxo.matrix().iloc[:5, [0, 1, 2, -3, -2, -1]]
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
      <th>320.000000</th>
      <th>320.039139</th>
      <th>320.078278</th>
      <th>339.921722</th>
      <th>339.960861</th>
      <th>340.000000</th>
    </tr>
    <tr>
      <th>Time</th>
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
      <th>2021-09-22 20:41:05.113032</th>
      <td>-87.5</td>
      <td>-91.5</td>
      <td>-92.5</td>
      <td>-87.5</td>
      <td>-87.0</td>
      <td>-84.5</td>
    </tr>
    <tr>
      <th>2021-09-22 20:41:07.283024</th>
      <td>-82.0</td>
      <td>-82.0</td>
      <td>-84.5</td>
      <td>-89.0</td>
      <td>-84.0</td>
      <td>-84.0</td>
    </tr>
    <tr>
      <th>2021-09-22 20:41:09.630510</th>
      <td>-84.0</td>
      <td>-85.0</td>
      <td>-88.5</td>
      <td>-88.0</td>
      <td>-86.5</td>
      <td>-87.5</td>
    </tr>
    <tr>
      <th>2021-09-22 20:41:13.863041</th>
      <td>-85.5</td>
      <td>-84.5</td>
      <td>-88.5</td>
      <td>-85.0</td>
      <td>-81.5</td>
      <td>-83.0</td>
    </tr>
    <tr>
      <th>2021-09-22 20:41:21.673136</th>
      <td>-83.5</td>
      <td>-85.0</td>
      <td>-87.0</td>
      <td>-84.5</td>
      <td>-85.5</td>
      <td>-89.5</td>
    </tr>
  </tbody>
</table>
</div>



```python
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9788</span>
</pre>



### CRFS Bin - Versão 4

```python
file = r'binfiles\rfeye002292_210208_T202215_CRFSBINv.4.bin'
blocks = parse_bin(file)
print(blocks)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002292_210208_T202215_CRFSBINv.4.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V022'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002292'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'Script_CRFSBINv4'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'LOGGER_VERSION'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'group_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'text'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.70008</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-47.66684</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">518.30</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span> ,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">39</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">48</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">51</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">47</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">59</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">44</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">49</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">43</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">54</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">37</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">53</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">45</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">55</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">58</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">unit</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">39</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antenna_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```python
blocks['spectrum'][0].matrix().iloc[:5, [0, 1, 2, -3, -2, -1]]
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
      <th>76.000000</th>
      <th>76.003907</th>
      <th>76.007813</th>
      <th>107.992187</th>
      <th>107.996093</th>
      <th>108.000000</th>
    </tr>
    <tr>
      <th>Time</th>
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
      <th>2021-02-08 20:22:15.500658</th>
      <td>-110.0</td>
      <td>-100.5</td>
      <td>-99.0</td>
      <td>-103.0</td>
      <td>-99.0</td>
      <td>-96.0</td>
    </tr>
    <tr>
      <th>2021-02-08 20:22:16.142770</th>
      <td>-105.5</td>
      <td>-100.0</td>
      <td>-97.5</td>
      <td>-94.5</td>
      <td>-95.0</td>
      <td>-98.0</td>
    </tr>
    <tr>
      <th>2021-02-08 20:22:16.500750</th>
      <td>-104.0</td>
      <td>-102.5</td>
      <td>-105.5</td>
      <td>-95.5</td>
      <td>-98.5</td>
      <td>-93.0</td>
    </tr>
    <tr>
      <th>2021-02-08 20:22:17.132990</th>
      <td>-105.0</td>
      <td>-107.0</td>
      <td>-103.0</td>
      <td>-99.5</td>
      <td>-99.5</td>
      <td>-102.5</td>
    </tr>
    <tr>
      <th>2021-02-08 20:22:17.501352</th>
      <td>-97.5</td>
      <td>-101.5</td>
      <td>-97.0</td>
      <td>-104.5</td>
      <td>-102.0</td>
      <td>-99.5</td>
    </tr>
  </tbody>
</table>
</div>



### CRFS Bin - Versão 3

```python
file = r'binfiles\rfeye002292_210208_T203238_CRFSBINv.3.bin'
blocks = parse_bin(file)
print(blocks)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002292_210208_T203238_CRFSBINv.3.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002292'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'Script_CRFSBINv3'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'LOGGER_VERSION'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-22.70008</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-47.66684</span>, Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">518.30</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span> ,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[]</span>
<span style="font-weight: bold">}</span>
</pre>


