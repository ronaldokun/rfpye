# RFPYE
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca <a href='https://fastcore.fast.ai/basics.html'>fastcore</a>, que expande e otimiza as estruturas de dados da linguagem python. 


## Instalação

Como parte dessa lib utiliza código c compilado com `Cython`, é preciso que um compilador `C` esteja instalado. É recomendado a criação de um ambiente virtual para que a instalação das dependências não interfira com o a instalação base do python. Para tal é recomendamos o uso do conda. A seguir é mostrado instruções para a criação do ambiente virtual, com todas as dependências utilizando o conda.

Instale o [miniconda](https://docs.conda.io/en/latest/miniconda.html). Com o conda instalado e disponível no seu `PATH` ou através do `Anaconda Prompt`, execute os comando:

### Linux:

Em Linux normalmente o sistema já possui o compilador `gcc` instalado.

```bash
conda create -n rfpye pip python=3.7 gcc -c intel -c conda-forge -y
conda activate rfpye
python -m pip install rfpye
```

### Windows

É preciso ter o compilador `Microsoft Visual C++ 2015-2019 Redistributable x64` Versão 14.x instalado.    


```bash
conda create -n rfpye pip python=3.7 libpython m2w64-toolchain -c intel -y
conda activate rfpye
python -m pip install rfpye
```

O comando acima cria um ambiente virtual com o mesmo nome da biblioteca `rfpye`, instala as dependências básicas necessárias para a compilação, em seguida ativa o ambiente virtual e instala o módulo.

Depois disso basta instalar normalmente a lib:
`python -m pip install rfpye`

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


<h4 id="parse_bin" class="doc_header"><code>parse_bin</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/parser.py#L103" class="source_link" style="float:right">[source]</a></h4>

> <code>parse_bin</code>(**`bin_file`**:`Union`\[`str`, `Path`\], **`precision`**=*`float32`*)

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
files = get_files(r'binfiles/v5', extensions=['.bin'])
file = files.shuffle()[0]
```

```python
%%time
dados = parse_bin(file)
```

    Wall time: 8.45 s
    

```python
print(dados)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002092_210630_T094705.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">23</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V023'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002092'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'ScriptRFeye2021_v2.cfg'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'INFO'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.82684</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.47805</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120.80</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">310</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">155</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">165</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 1 de 4).'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">90</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 2 de 4).'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 3 de 4).'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">170</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 4 de 4).'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">470</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5888</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">200</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 1 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 2 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1710</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1980</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6912</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 3 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2100</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2169</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1792</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">230</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 4 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2290</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2390</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2560</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">240</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 5 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2500</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4864</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">250</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 6 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3290</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3700</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10496</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 3 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">330</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 4 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1219</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">350</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 6 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1389</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1429</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">360</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1649</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">370</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 8 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2899</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">380</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 9 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5000</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5160</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4096</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">390</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 10 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5339</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5459</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3328</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



A saída da função é um dicionário, com os metadados do arquivo.

## GPS
No entanto as duas chaves mais importantes do dicionário retornado são `gps` e `spectrum`

Se você imprimir a classe retornada pela chave `gps` é retornado um resumo dos seus atributos:

```python
print(dados['gps'])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.82684</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.47805</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120.80</span> #Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span>
</pre>



> Para extrair os atributos em si de dado objeto e retorná-los todos num dicionário, o módulo utils tem a função auxiliar `getattrs`


<h4 id="getattrs" class="doc_header"><code>getattrs</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/utils.py#L135" class="source_link" style="float:right">[source]</a></h4>

> <code>getattrs</code>(**`obj`**:`Any`, **`attrs`**:`Iterable`=*`None`*, **`as_tuple`**=*`False`*)

Receives an object and return the atributes listed in `attrs`, if attrs is None return its public attributes


```python
print(getattrs(dados['gps']))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120.8</span>, <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.826842</span>, <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.478047</span>, <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span><span style="font-weight: bold">}</span>
</pre>



Os atributos listados são os valores consolidados por meio da __mediana__ dos diversos blocos de GPS do arquivo. 

### Dados Brutos de GPS
> Caso desejar a lista original de valores, a classe é iterável num loop normalmente e também é possível selecionar os índices individualmente.

```python
dados['gps'][0] , dados['gps'][-1]
```




    ((-12.826869, -38.478055, 119.9, 9), (-12.826869, -38.478037, 114.4, 12))



```python
for coords in dados['gps']:
    lat, long, alt, num = coords
    print(f'{lat:.6f} {long:.6f} {alt:.6f} {num}')
    break
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.826869</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.478055</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">119.900000</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>
</pre>



Para saber quantos dados brutos existem, basta utilizar a função `len`:

```python
len(dados['gps'])
```




    9060



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


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Blocks of Type: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Thread_id: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, Start: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span> MHz, Stop: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span> MHz
</pre>



A função `repr` retorna uma representação com todos os metadados do fluxo:

```python
print(repr(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>
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


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-84</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-101</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-107.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-84</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-97</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-101.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-103</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-83</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-83</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-84.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-103.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99</span>. <span style="font-weight: bold">]</span>
 <span style="color: #808000; text-decoration-color: #808000">...</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-89.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-102.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-114</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-103.5</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-105</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-104.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99</span>. <span style="font-weight: bold">]]</span>
</pre>



```python
print(f'Formato da matriz com os níveis: {fluxo.levels.shape}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Formato da matriz com os níveis: <span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9060</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)</span>
</pre>



O nº de linhas da matriz nos dá o número de pontos medidos naquele dado fluxo e as colunas o número de traços no qual o Span ( Stop - Start ) foi dividido. O número de traços pode ser retornada também por meio da função `len`

```python
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9060</span>
</pre>



A classe `Spectrum` é iterável, ou seja, pode ser acessada como uma lista, é retornada uma tupla com o timestamp e os pontos daquele traço:

```python
for time, traço in fluxo:
    print(time)
    print(traço)
    break
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span>-<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">06</span>-30T<span style="color: #00ff00; text-decoration-color: #00ff00; font-weight: bold">09:46:11</span>.<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">447522</span>
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-88.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-84</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-101</span>.  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-107.5</span><span style="font-weight: bold">]</span>
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
      <th>2021-06-30 09:46:11.447522</th>
      <td>-88.5</td>
      <td>-86.0</td>
      <td>-84.0</td>
      <td>-80.5</td>
      <td>-82.5</td>
    </tr>
    <tr>
      <th>2021-06-30 09:47:00.736878</th>
      <td>-85.0</td>
      <td>-84.0</td>
      <td>-85.0</td>
      <td>-88.0</td>
      <td>-90.5</td>
    </tr>
    <tr>
      <th>2021-06-30 09:48:00.736849</th>
      <td>-83.0</td>
      <td>-83.0</td>
      <td>-84.5</td>
      <td>-92.0</td>
      <td>-87.0</td>
    </tr>
    <tr>
      <th>2021-06-30 09:49:00.736763</th>
      <td>-90.5</td>
      <td>-96.5</td>
      <td>-90.5</td>
      <td>-85.5</td>
      <td>-87.5</td>
    </tr>
    <tr>
      <th>2021-06-30 09:50:00.736788</th>
      <td>-86.5</td>
      <td>-86.0</td>
      <td>-86.5</td>
      <td>-84.5</td>
      <td>-85.0</td>
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
      <th>2021-07-06 16:41:00.741214</th>
      <td>-96.5</td>
      <td>-96.5</td>
      <td>-97.0</td>
      <td>-97.0</td>
      <td>-101.0</td>
    </tr>
    <tr>
      <th>2021-07-06 16:42:00.781447</th>
      <td>-111.0</td>
      <td>-103.0</td>
      <td>-102.0</td>
      <td>-102.0</td>
      <td>-105.0</td>
    </tr>
    <tr>
      <th>2021-07-06 16:43:00.751170</th>
      <td>-95.0</td>
      <td>-98.0</td>
      <td>-99.5</td>
      <td>-102.5</td>
      <td>-114.0</td>
    </tr>
    <tr>
      <th>2021-07-06 16:44:00.761445</th>
      <td>-98.0</td>
      <td>-100.0</td>
      <td>-99.5</td>
      <td>-103.5</td>
      <td>-105.0</td>
    </tr>
    <tr>
      <th>2021-07-06 16:45:00.862489</th>
      <td>-96.5</td>
      <td>-101.0</td>
      <td>-104.5</td>
      <td>-99.5</td>
      <td>-99.0</td>
    </tr>
  </tbody>
</table>
</div>



Novamente, caso desejado acessar todos os atributos de um fluxo no formato de dicionário, basta utilizar a função `getattrs`

```python
print(getattrs(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'antuid'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'dtype'</span>: <span style="color: #008000; text-decoration-color: #008000">'dBm'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'ndata'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
    <span style="color: #008000; text-decoration-color: #008000">'precision'</span>: <span style="font-weight: bold">&lt;</span><span style="color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold">class</span><span style="color: #000000; text-decoration-color: #000000"> </span><span style="color: #008000; text-decoration-color: #008000">'numpy.float32'</span><span style="font-weight: bold">&gt;</span>,
    <span style="color: #008000; text-decoration-color: #008000">'processing'</span>: <span style="color: #008000; text-decoration-color: #008000">'peak'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_dateidx'</span>: <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">datetime.datetime</span><span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">447522</span><span style="font-weight: bold">)</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_dateidx'</span>: <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">datetime.datetime</span><span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">16</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">45</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">862489</span><span style="font-weight: bold">)</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>
<span style="font-weight: bold">}</span>
</pre>



### CRFS Bin - Versão 5 - Arquivos Comprimidos
Vamos listar arquivos da última versão do script Logger, Versão 5, arquivos comprimidos onde o piso de ruído é suprimido.

```python
file = r'binfiles\Comprimidos\rfeye002290_210922_T204046_MaskBroken.bin'
```

```python
%%time
compressed = parse_bin(file)
```

    Wall time: 5.91 s
    

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
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.95765</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-46.37637</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">19.70</span> #Satellites:
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">321</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">3 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">301</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10). @ -80dBm, 10kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">137</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14848</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">341</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de </span>
<span style="color: #008000; text-decoration-color: #008000">10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1219</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">311</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10). @ -80dBm, 10kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">156</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">163</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">371</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 8 de </span>
<span style="color: #008000; text-decoration-color: #008000">10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2899</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">351</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 6 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1389</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1429</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">331</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 4 de </span>
<span style="color: #008000; text-decoration-color: #008000">10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">361</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1649</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```python
fluxo = compressed['spectrum'] ; fluxos
```




    (#20) [Spectrum(type=67, thread_id=300, description='PMEC 2021 (Faixa 1 de 10).', start_mega=105, stop_mega=140, dtype='dBm', ndata=3584, bw=18457, processing='peak', antuid=0),Spectrum(type=67, thread_id=310, description='PMEC 2021 (Faixa 2 de 10).', start_mega=155, stop_mega=165, dtype='dBm', ndata=1024, bw=18457, processing='peak', antuid=0),Spectrum(type=67, thread_id=100, description='PRD 2021 (Faixa principal 1 de 4).', start_mega=50, stop_mega=90, dtype='dBμV/m', ndata=1024, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=110, description='PRD 2021 (Faixa principal 2 de 4).', start_mega=70, stop_mega=110, dtype='dBμV/m', ndata=1024, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=120, description='PRD 2021 (Faixa principal 3 de 4).', start_mega=170, stop_mega=220, dtype='dBμV/m', ndata=1280, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=130, description='PRD 2021 (Faixa principal 4 de 4).', start_mega=470, stop_mega=700, dtype='dBμV/m', ndata=5888, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=200, description='PMEF 2021 (Faixa 1 de 6).', start_mega=700, stop_mega=960, dtype='dBm', ndata=6656, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=210, description='PMEF 2021 (Faixa 2 de 6).', start_mega=1710, stop_mega=1980, dtype='dBm', ndata=6912, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=220, description='PMEF 2021 (Faixa 3 de 6).', start_mega=2100, stop_mega=2169, dtype='dBm', ndata=1792, bw=73828, processing='peak', antuid=0),Spectrum(type=67, thread_id=230, description='PMEF 2021 (Faixa 4 de 6).', start_mega=2290, stop_mega=2390, dtype='dBm', ndata=2560, bw=73828, processing='peak', antuid=0)...]



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
      <th>105.000000</th>
      <th>105.009768</th>
      <th>105.019537</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-06-30 09:46:11.447522</th>
      <td>-88.5</td>
      <td>-86.0</td>
      <td>-84.0</td>
      <td>-100.0</td>
      <td>-101.0</td>
      <td>-107.5</td>
    </tr>
    <tr>
      <th>2021-06-30 09:47:00.736878</th>
      <td>-85.0</td>
      <td>-84.0</td>
      <td>-85.0</td>
      <td>-97.0</td>
      <td>-101.5</td>
      <td>-103.0</td>
    </tr>
    <tr>
      <th>2021-06-30 09:48:00.736849</th>
      <td>-83.0</td>
      <td>-83.0</td>
      <td>-84.5</td>
      <td>-103.5</td>
      <td>-100.0</td>
      <td>-99.0</td>
    </tr>
    <tr>
      <th>2021-06-30 09:49:00.736763</th>
      <td>-90.5</td>
      <td>-96.5</td>
      <td>-90.5</td>
      <td>-103.5</td>
      <td>-105.0</td>
      <td>-101.5</td>
    </tr>
    <tr>
      <th>2021-06-30 09:50:00.736788</th>
      <td>-86.5</td>
      <td>-86.0</td>
      <td>-86.5</td>
      <td>-104.5</td>
      <td>-101.5</td>
      <td>-99.5</td>
    </tr>
  </tbody>
</table>
</div>



```python
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9060</span>
</pre>



### CRFS Bin - Versão 4

```python
file = r'binfiles\v4\rfeye002292_210208_T202215_CRFSBINv.4.bin'
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
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.97163</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.48149</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">151.65</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">65</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)]</span>
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
file = r'binfiles\v3\rfeye002292_210208_T203238_CRFSBINv.3.bin'
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
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-12.97163</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-38.48149</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">150.60</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">61</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)]</span>
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
      <th>105.000000</th>
      <th>105.009768</th>
      <th>105.019537</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2021-02-08 20:32:39.548000</th>
      <td>-76.5</td>
      <td>-76.0</td>
      <td>-76.5</td>
      <td>-94.5</td>
      <td>-91.0</td>
      <td>-90.0</td>
    </tr>
    <tr>
      <th>2021-02-08 20:32:40.133600</th>
      <td>-79.5</td>
      <td>-80.5</td>
      <td>-79.5</td>
      <td>-99.0</td>
      <td>-94.5</td>
      <td>-92.5</td>
    </tr>
    <tr>
      <th>2021-02-08 20:32:41.858000</th>
      <td>-69.0</td>
      <td>-69.0</td>
      <td>-69.0</td>
      <td>-97.5</td>
      <td>-92.5</td>
      <td>-90.0</td>
    </tr>
    <tr>
      <th>2021-02-08 20:32:42.137500</th>
      <td>-70.5</td>
      <td>-71.0</td>
      <td>-71.5</td>
      <td>-97.0</td>
      <td>-98.0</td>
      <td>-94.5</td>
    </tr>
    <tr>
      <th>2021-02-08 20:32:43.716000</th>
      <td>-71.0</td>
      <td>-69.5</td>
      <td>-70.0</td>
      <td>-97.0</td>
      <td>-89.0</td>
      <td>-87.0</td>
    </tr>
  </tbody>
</table>
</div>



### CRFS Bin Versão 2

```python
from rfpye.parser import parse_bin
file = r'binfiles\v2\rfeye002092_210208_T203131_CRFSBINv.2.bin'
blocks = parse_bin(file)
print(blocks)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002092_210208_T203131_CRFSBINv.2.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00</span> #Satellites: 
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Average'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>,
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Average'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span><span style="font-weight: bold">)]</span>
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
      <th>NaN</th>
      <td>10.5</td>
      <td>11.5</td>
      <td>13.0</td>
      <td>31.0</td>
      <td>26.0</td>
      <td>22.5</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>18.0</td>
      <td>19.5</td>
      <td>16.5</td>
      <td>27.5</td>
      <td>29.5</td>
      <td>25.5</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>11.5</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>30.5</td>
      <td>28.5</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>4.5</td>
      <td>4.5</td>
      <td>13.5</td>
      <td>27.5</td>
      <td>31.0</td>
      <td>31.0</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>17.5</td>
      <td>15.5</td>
      <td>11.0</td>
      <td>33.5</td>
      <td>29.5</td>
      <td>30.0</td>
    </tr>
  </tbody>
</table>
</div>



### Fluxo de Ocupação

```python
from rfpye.parser import parse_bin
file = r'binfiles\occ\rfeye002090-VCP_FM_occ15min_191221_085803.bin'
blocks = parse_bin(file)
print(blocks)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002090-VCP_FM_occ15min_191221_085803.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">22</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V022'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002090-VCP'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS default method'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'RFeye002090'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'LOGGER_VERSION'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'Ocupacao em 15 minutos na faixa FM'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00</span> #Satellites: 
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">Spectrum</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">65</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">121</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">80</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1536</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```python
blocks['spectrum'][-1].matrix().iloc[:5, 1003:1010]
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
      <th>99.602606</th>
      <th>99.622150</th>
      <th>99.641694</th>
      <th>99.661238</th>
      <th>99.680782</th>
      <th>99.700326</th>
      <th>99.719870</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2019-12-21 09:00:01.367337</th>
      <td>17.5</td>
      <td>36.0</td>
      <td>53.5</td>
      <td>62.5</td>
      <td>76.5</td>
      <td>80.0</td>
      <td>72.5</td>
    </tr>
    <tr>
      <th>2019-12-21 09:15:01.357259</th>
      <td>15.0</td>
      <td>29.5</td>
      <td>48.0</td>
      <td>61.0</td>
      <td>76.5</td>
      <td>78.5</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>2019-12-21 09:30:01.357357</th>
      <td>16.0</td>
      <td>28.5</td>
      <td>46.5</td>
      <td>61.0</td>
      <td>76.5</td>
      <td>77.5</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>2019-12-21 09:45:01.357273</th>
      <td>15.0</td>
      <td>33.0</td>
      <td>49.0</td>
      <td>66.0</td>
      <td>76.0</td>
      <td>78.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>2019-12-21 10:00:01.419225</th>
      <td>15.5</td>
      <td>35.0</td>
      <td>50.0</td>
      <td>62.0</td>
      <td>74.0</td>
      <td>77.0</td>
      <td>67.5</td>
    </tr>
  </tbody>
</table>
</div>


