# RFPYE
> Este módulo tem como objetivo o processamento e extração otimizada de dados dos arquivos `.bin` de monitoramento do espectro provenientes do script Logger executados nas estações de Monitoramento CRFS RFeye Node. Para tal utilizamos as várias funcionalidades da biblioteca <a href='https://fastcore.fast.ai/basics.html'>fastcore</a>, que expande e otimiza as estruturas de dados da linguagem python. 


## Instalação

Como parte dessa lib utiliza código c compilado com `Cython`, é preciso que um compilador `C` esteja instalado. No entanto é recomendado a criação de um ambiente virtual para que a instalação das dependências não interfira com o a instalação base do python. Para tal é recomendamos o uso do conda. A seguir é mostrado instruções para a criação do ambiente virtual, com todas as dependências, inclusive o compilador C, utilizando o conda.

Instale o [miniconda](https://docs.conda.io/en/latest/miniconda.html). Com o conda instalado e disponível no seu `PATH` ou através do `Anaconda Prompt`, execute os comando:

### Linux:

```bash
conda create -n rfpye pip python=3.7 gcc -c intel -c conda-forge -y
conda activate rfpye
python -m pip install rfpye
```

### Windows

```bash
conda create -n rfpye pip python=3.7 libpython m2w64-toolchain -c intel -y
conda activate rfpye
echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg
echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg
python -m pip install rfpye
```

O comando acima cria um ambiente virtual com o mesmo nome da biblioteca `rfpye`, instala as dependências básicas necessárias para a compilação, em seguida ativa o ambiente virtual e instala o módulo.
As duas linhas adicionais em Windows cria um arquivo de configuração `distutils.cfg` para o compilador `m2w64`, que é utilizado pelo conda para compilar o código.

Depois disso basta instalar normalmente a lib:
`python -m pip install rfpye`

Em Linux normalmente o sistema já possui o compilador `gcc` instalado então basta executar o comando `pip install` acima.

## Como utilizar
Abaixo mostramos as funcionalidades principais dos módulos, utilizando-os dentro de algum outro script ou `REPL`

Precisamos necessariamente de um diretório de entrada, contendo um ou mais arquivos `.bin`
> Mude os caminhos abaixo para suas pastas locais

```
from fastcore.xtras import Path
from rfpye.utils import get_files
from rich import print
```

A função abaixo baixa alguns arquivos de exemplo:

```
path = Path(r'binfiles')
if not path.exists() or not len(get_files(path, extensions=['.bin'])):
    path = Path('.')
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T202310_CRFSBINv.5.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T202310_CRFSBINv.5.bin' --output-document 'rfeye002092_210208_T202310_CRFSBINv.5.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T203131_CRFSBINv.2.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002092_210208_T203131_CRFSBINv.2.bin' --output-document 'rfeye002092_210208_T203131_CRFSBINv.2.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T202215_CRFSBINv.4.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T202215_CRFSBINv.4.bin' --output-document 'rfeye002292_210208_T202215_CRFSBINv.4.bin'
    !wget --header 'Host: raw.githubusercontent.com' --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0' --header 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' --header 'Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3' --referer 'https://github.com/EricMagalhaesDelgado/SpecFiles/blob/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T203238_CRFSBINv.3.bin' --header 'DNT: 1' --header 'Upgrade-Insecure-Requests: 1' 'https://raw.githubusercontent.com/EricMagalhaesDelgado/SpecFiles/main/Combo3%20(CRFS%20Bin%20-%20DataTypes%204%2C%207%2C%208%2C%2060-65%20e%2067-69)/rfeye002292_210208_T203238_CRFSBINv.3.bin' --output-document 'rfeye002292_210208_T203238_CRFSBINv.3.bin'

```

A função `parse_bin` é a função principal que encapsula o processamento dos arquivos bin.


<h4 id="parse_bin" class="doc_header"><code>parse_bin</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/parser.py#L42" class="source_link" style="float:right">[source]</a></h4>

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

```
files = get_files(r'D:\OneDrive - ANATEL\Sensores', extensions=['.bin'])
file = files.shuffle()[0]
```

```
%%time
dados = parse_bin(file)
```

    Wall time: 15.1 s
    

```
print(dados)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002263_210618_T210255.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">23</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V023'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'hostname'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002263'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'method'</span>: <span style="color: #008000; text-decoration-color: #008000">'ScriptRFeye2021_v.1'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'unit_info'</span>: <span style="color: #008000; text-decoration-color: #008000">'Stationary'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_number'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'identifier'</span>: <span style="color: #008000; text-decoration-color: #008000">'INFO'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.32905</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-51.13701</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">591.30</span> 
#Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">310</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC </span>
<span style="color: #008000; text-decoration-color: #008000">2021 (Faixa 2 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">155.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">165.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>,
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">100</span>,
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 1 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">90.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-45.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-45.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 2 de </span>
<span style="color: #008000; text-decoration-color: #008000">4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-29.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-29.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">120</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 3 de 4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">170.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-51.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-51.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">130</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PRD 2021 (Faixa principal 4 de </span>
<span style="color: #008000; text-decoration-color: #008000">4).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">470.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBμV/m'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5888</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">200</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 1 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">700.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 2 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1710.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1980.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6912</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 3 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2100.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002168.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1792</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">230</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 4 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2290.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2390.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2560</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">240</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 5 de 6).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2500.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4864</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC </span>
<span style="color: #008000; text-decoration-color: #008000">2021 (Faixa 3 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">330</span>,
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 4 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001218.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">350</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 6 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001388.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001428.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">360</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001648.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">370</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 </span>
<span style="color: #008000; text-decoration-color: #008000">(Faixa 8 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002898.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">380</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 9 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5000.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5160.0</span>,
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4096</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">390</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 10 de 10).'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005338.999</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1005458.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3328</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">250</span>,
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEF 2021 (Faixa 6 de 6).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3290.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3700.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10496</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



A saída da função é um dicionário, com os metadados do arquivo.

## GPS
No entanto as duas chaves mais importantes do dicionário retornado são `gps` e `spectrum`

Se você imprimir a classe retornada pela chave `gps` é retornado um resumo dos seus atributos:

```
print(dados['gps'])
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.32905</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-51.13701</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">591.30</span> #Satellites: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>
</pre>



> Para extrair os atributos em si de dado objeto e retorná-los todos num dicionário, o módulo utils tem a função auxiliar `getattrs`


<h4 id="getattrs" class="doc_header"><code>getattrs</code><a href="https://github.com/ronaldokun/rfpye/tree/master/rfpye/utils.py#L146" class="source_link" style="float:right">[source]</a></h4>

> <code>getattrs</code>(**`obj`**:`Any`, **`attrs`**:`Iterable`\[`T_co`\]=*`None`*)

Receives an object and return the atributes listed in `attrs`, if attrs is None return its public attributes


```
print(getattrs(dados['gps']))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span><span style="color: #008000; text-decoration-color: #008000">'altitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">807.8</span>, <span style="color: #008000; text-decoration-color: #008000">'latitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-23.44242</span>, <span style="color: #008000; text-decoration-color: #008000">'longitude'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-46.472522</span>, <span style="color: #008000; text-decoration-color: #008000">'num_satellites'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span><span style="font-weight: bold">}</span>
</pre>



Os atributos listados são os valores consolidados por meio da __mediana__ dos diversos blocos de GPS do arquivo. 

### Dados Brutos de GPS
> Caso desejar a lista original de valores, os atributos são os mesmos mas precedidos de `_`, o que os torna __atributos privados__ em python, isso somente quer dizer que não são explicitados em algus métodos como `getattrs`, pois normalmente não são acessíveis diretamente, mas nada impede que sejam acessados.

```
dados['gps']._latitude
```




    (#9058) [-23.329051,-23.329054,-23.329058,-23.329051,-23.329052,-23.329054,-23.32904,-23.329055,-23.329057,-23.32906...]



```
dados['gps']._longitude
```




    (#9058) [-51.137013,-51.137008,-51.137002,-51.137009,-51.137008,-51.137005,-51.137015,-51.137019,-51.137025,-51.13702...]



```
dados['gps']._altitude
```




    (#9058) [590.8,589.9,589.9,590.6,590.7,589.8,590.3,589.7,589.0,589.5...]



```
dados['gps']._num_satellites 
```




    (#9058) [11,11,11,11,11,11,11,11,11,11...]



## Dados de Nível Espectral
Cada arquivo bin normalmente possui vários fluxos de espectro distintos, cada fluxo espectral é uma classe Python, na chave `spectrum` é retornado uma lista com todos os fluxos de espectro.

```
fluxos = dados['spectrum']
print(len(fluxos))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>
</pre>



Vamos investigar um deles:

```
fluxo = fluxos[0]
```

Ao imprimir um fluxo é mostrado informações mínimas sobre o seu conteúdo:

```
print(fluxo)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Blocks of Type: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, Thread_id: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, Start: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span> MHz, Stop: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span> MHz
</pre>



A função `repr` retorna uma representação com todos os metadados do fluxo:

```
print(repr(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>
</pre>



Qualquer um dos atributos listados podem ser acessados diretamente:

```
print(fluxo.description) , print(fluxo.bw)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">PMEC <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2021</span> <span style="font-weight: bold">(</span>Faixa <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span> de <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span><span style="font-weight: bold">)</span>.
</pre>




<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>
</pre>






    (None, None)



No entanto o principal atributo de um fluxo de espectro são os valores de nível medidos, os valores medidos são retornados por meio do atributo `levels`:

```
print(fluxo.levels)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">[[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-95</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-87</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-96</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-86</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-95.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91.5</span><span style="font-weight: bold">]</span>
 <span style="color: #808000; text-decoration-color: #808000">...</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-89.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-85.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-96.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>. <span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-94</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-92.5</span> <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-96.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-98.5</span><span style="font-weight: bold">]</span>
 <span style="font-weight: bold">[</span> <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-83</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-83.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-91</span>.  <span style="color: #808000; text-decoration-color: #808000">...</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99</span>.   <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-99.5</span>  <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-95.5</span><span style="font-weight: bold">]]</span>
</pre>



```
print(f'Formato da matriz com os níveis: {fluxo.levels.shape}')
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Formato da matriz com os níveis: <span style="font-weight: bold">(</span><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2576</span>, <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span><span style="font-weight: bold">)</span>
</pre>



O nº de linhas da matriz nos dá o número de pontos medidos naquele dado fluxo e as colunas o número de traços no qual o Span ( Stop - Start ) foi dividido. O número de traços pode ser retornada também por meio da função `len`

```
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9058</span>
</pre>



O atributo anterior retorna uma `numpy.ndarray`, que é um formato eficiente para processamento. 

### Medidas de nível como pandas dataframe
No entanto temos adicionalmente o método `.matrix()` que retorna a matriz de dados como um _Pandas Dataframe_ formatada com o tempo da medição de cada traço como índice das linhas e as frequências de cada traço como coluna.

Vamos mostrar as cinco primeiras e cinco últimas linhas e colunas. 

```
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
      <th>2021-06-18 21:03:00.762503</th>
      <td>-95.0</td>
      <td>-87.5</td>
      <td>-86.0</td>
      <td>-90.0</td>
      <td>-92.5</td>
    </tr>
    <tr>
      <th>2021-06-18 21:04:01.432664</th>
      <td>-85.5</td>
      <td>-86.0</td>
      <td>-87.0</td>
      <td>-84.0</td>
      <td>-77.5</td>
    </tr>
    <tr>
      <th>2021-06-18 21:05:01.182570</th>
      <td>-86.0</td>
      <td>-90.0</td>
      <td>-95.5</td>
      <td>-85.0</td>
      <td>-84.5</td>
    </tr>
    <tr>
      <th>2021-06-18 21:06:00.812513</th>
      <td>-86.0</td>
      <td>-87.5</td>
      <td>-91.5</td>
      <td>-96.5</td>
      <td>-93.5</td>
    </tr>
    <tr>
      <th>2021-06-18 21:07:01.402635</th>
      <td>-90.0</td>
      <td>-83.0</td>
      <td>-84.5</td>
      <td>-88.5</td>
      <td>-85.5</td>
    </tr>
  </tbody>
</table>
</div>



```
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
      <th>2021-07-02 18:56:00.731317</th>
      <td>-96.0</td>
      <td>-97.0</td>
      <td>-104.0</td>
      <td>-100.5</td>
      <td>-102.5</td>
    </tr>
    <tr>
      <th>2021-07-02 18:57:00.731239</th>
      <td>-99.5</td>
      <td>-99.5</td>
      <td>-101.0</td>
      <td>-101.0</td>
      <td>-98.5</td>
    </tr>
    <tr>
      <th>2021-07-02 18:58:00.731138</th>
      <td>-95.0</td>
      <td>-99.5</td>
      <td>-99.5</td>
      <td>-101.5</td>
      <td>-98.5</td>
    </tr>
    <tr>
      <th>2021-07-02 18:59:00.731242</th>
      <td>-99.5</td>
      <td>-99.5</td>
      <td>-97.0</td>
      <td>-97.5</td>
      <td>-98.5</td>
    </tr>
    <tr>
      <th>2021-07-02 19:00:00.732413</th>
      <td>-95.5</td>
      <td>-99.5</td>
      <td>-98.0</td>
      <td>-97.5</td>
      <td>-103.5</td>
    </tr>
  </tbody>
</table>
</div>



Novamente, caso desejado acessar todos os atributos de um fluxo no formato de dicionário, basta utilizar a função `getattrs`

```
print(getattrs(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'antuid'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'bw'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">18457</span>,
    <span style="color: #008000; text-decoration-color: #008000">'description'</span>: <span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10).'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'dtype'</span>: <span style="color: #008000; text-decoration-color: #008000">'dBm'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'minimum'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>,
    <span style="color: #008000; text-decoration-color: #008000">'ndata'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
    <span style="color: #008000; text-decoration-color: #008000">'processing'</span>: <span style="color: #008000; text-decoration-color: #008000">'peak'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'start_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'stop_mega'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">300</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thresh'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">67</span>
<span style="font-weight: bold">}</span>
</pre>



### CRFS Bin - Versão 5 - Arquivos Comprimidos
Vamos listar arquivos da última versão do script Logger, Versão 5, arquivos comprimidos onde o piso de ruído é suprimido.

```
file = r'binfiles\compressed\rfeye002290_210922_T204046_MaskBroken.bin'
```

```
%%time
compressed = parse_bin(file)
```

    Wall time: 8.76 s
    

```
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
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-14.81416</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.03184</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15.50</span> #Satellites:
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">321</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 3 de 10). @ </span>
<span style="color: #008000; text-decoration-color: #008000">-80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">320.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">340.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">512</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">301</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 1 de 10). @ -80dBm, 10kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">137.0</span>,
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14848</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>,
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">341</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 5 de 10). @ -80dBm, 100kHz.'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">960.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001218.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">6656</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">311</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 2 de 10). @ -80dBm, 10kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">156.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">163.0</span>,
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3690</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">371</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 8 de 10). @ -80dBm, 100kHz.'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">2690.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1002898.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">5376</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">351</span>, 
<span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 6 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001388.999</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001428.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1280</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">331</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa </span>
<span style="color: #008000; text-decoration-color: #008000">4 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">400.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">410.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">256</span>, 
<span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">68</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">361</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'PMEC 2021 (Faixa 7 de 10). @ -80dBm, 100kHz.'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1530.0</span>,
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1001648.999</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3072</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">73828</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-100</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```
fluxo = compressed['spectrum'] ; fluxos
```




    (#20) [SpecData(type=67, thread_id=300, description='PMEC 2021 (Faixa 1 de 10).', start_mega=105.0, stop_mega=140.0, dtype='dBm', ndata=3584, bw=18457, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5),SpecData(type=67, thread_id=310, description='PMEC 2021 (Faixa 2 de 10).', start_mega=155.0, stop_mega=165.0, dtype='dBm', ndata=1024, bw=18457, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5),SpecData(type=67, thread_id=100, description='PRD 2021 (Faixa principal 1 de 4).', start_mega=50.0, stop_mega=90.0, dtype='dBμV/m', ndata=1024, bw=73828, processing='peak', antuid=0, thresh=-90.5, minimum=-90.5),SpecData(type=67, thread_id=110, description='PRD 2021 (Faixa principal 2 de 4).', start_mega=70.0, stop_mega=110.0, dtype='dBμV/m', ndata=1024, bw=73828, processing='peak', antuid=0, thresh=-67.5, minimum=-67.5),SpecData(type=67, thread_id=120, description='PRD 2021 (Faixa principal 3 de 4).', start_mega=170.0, stop_mega=220.0, dtype='dBμV/m', ndata=1280, bw=73828, processing='peak', antuid=0, thresh=-37.5, minimum=-37.5),SpecData(type=67, thread_id=130, description='PRD 2021 (Faixa principal 4 de 4).', start_mega=470.0, stop_mega=700.0, dtype='dBμV/m', ndata=5888, bw=73828, processing='peak', antuid=0, thresh=-41.5, minimum=-41.5),SpecData(type=67, thread_id=200, description='PMEF 2021 (Faixa 1 de 6).', start_mega=700.0, stop_mega=960.0, dtype='dBm', ndata=6656, bw=73828, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5),SpecData(type=67, thread_id=210, description='PMEF 2021 (Faixa 2 de 6).', start_mega=1710.0, stop_mega=1980.0, dtype='dBm', ndata=6912, bw=73828, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5),SpecData(type=67, thread_id=220, description='PMEF 2021 (Faixa 3 de 6).', start_mega=2100.0, stop_mega=1002168.999, dtype='dBm', ndata=1792, bw=73828, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5),SpecData(type=67, thread_id=230, description='PMEF 2021 (Faixa 4 de 6).', start_mega=2290.0, stop_mega=2390.0, dtype='dBm', ndata=2560, bw=73828, processing='peak', antuid=0, thresh=-147.5, minimum=-147.5)...]



```
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
      <th>2021-06-26 12:01:00.731405</th>
      <td>-112.5</td>
      <td>-117.0</td>
      <td>-111.0</td>
      <td>-106.0</td>
      <td>-105.0</td>
      <td>-99.5</td>
    </tr>
    <tr>
      <th>2021-06-26 12:02:00.731287</th>
      <td>-111.5</td>
      <td>-115.5</td>
      <td>-116.5</td>
      <td>-103.0</td>
      <td>-101.5</td>
      <td>-101.0</td>
    </tr>
    <tr>
      <th>2021-06-26 12:03:00.731107</th>
      <td>-116.5</td>
      <td>-113.0</td>
      <td>-113.5</td>
      <td>-105.5</td>
      <td>-103.5</td>
      <td>-105.0</td>
    </tr>
    <tr>
      <th>2021-06-26 12:04:00.731401</th>
      <td>-111.5</td>
      <td>-112.0</td>
      <td>-110.0</td>
      <td>-109.5</td>
      <td>-114.5</td>
      <td>-106.5</td>
    </tr>
    <tr>
      <th>2021-06-26 12:05:00.731532</th>
      <td>-113.0</td>
      <td>-115.0</td>
      <td>-117.5</td>
      <td>-101.5</td>
      <td>-101.0</td>
      <td>-99.5</td>
    </tr>
  </tbody>
</table>
</div>



```
print(len(fluxo))
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8715</span>
</pre>



### CRFS Bin - Versão 4

```
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
    <span style="color: #008000; text-decoration-color: #008000">'group_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'text'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-14.81416</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.03184</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15.50</span> #Satellites:
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">39</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">63</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>,
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">48</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, 
<span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">65</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, <span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">51</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">47</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">46</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">59</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">44</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">50</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">49</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">43</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">52</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">54</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">42</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">37</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">53</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">45</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">55</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">58</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">64</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">description</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">bw</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">39</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```
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

```
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
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-14.81416</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.03184</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15.50</span> #Satellites:
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">60</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">61</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">nloops</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'average'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span>, <span style="color: #808000; text-decoration-color: #808000">minimum</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-147.5</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105000000</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140000000</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">62</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105000000</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140000000</span>, 
<span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```
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

```
from rfpye.parser import parse_bin
file = r'binfiles\v2\rfeye002092_210208_T203131_CRFSBINv.2.bin'
blocks = parse_bin(file)
print(blocks)
```


<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="font-weight: bold">{</span>
    <span style="color: #008000; text-decoration-color: #008000">'filename'</span>: <span style="color: #008000; text-decoration-color: #008000">'rfeye002092_210208_T203131_CRFSBINv.2.bin'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'file_version'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">21</span>,
    <span style="color: #008000; text-decoration-color: #008000">'string'</span>: <span style="color: #008000; text-decoration-color: #008000">'CRFS DATA FILE V021'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'size'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">24</span>,
    <span style="color: #008000; text-decoration-color: #008000">'text'</span>: <span style="color: #008000; text-decoration-color: #008000">'ClearWrite. Peak.'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'textlen'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>,
    <span style="color: #008000; text-decoration-color: #008000">'thread_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>,
    <span style="color: #008000; text-decoration-color: #008000">'type'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-14.81416</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-39.03184</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15.50</span> #Satellites:
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">20</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">76</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">108</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8192</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">30</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">70</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1024</span>, 
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">11</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>,
<span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Average'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">12</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Peak'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">4</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">13</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>,
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'Average'</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">203</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">9</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">204</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">8</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">15</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">sampling</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, 
<span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">10</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">221</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">206</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">207</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">213</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">209</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">226</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">212</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">215</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">208</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">210</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">201</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">219</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">202</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">222</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">220</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">216</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">224</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">229</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">218</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, 
<span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">211</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, 
<span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">223</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, 
<span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">205</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, 
<span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">214</span>, 
<span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, 
<span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">228</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)</span>, <span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">7</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">14</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">105</span>, 
<span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">140</span>, <span style="color: #808000; text-decoration-color: #808000">namal</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">230</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">3584</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-90</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```
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
      <th>0</th>
      <td>10.5</td>
      <td>11.5</td>
      <td>13.0</td>
      <td>31.0</td>
      <td>26.0</td>
      <td>22.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>18.0</td>
      <td>19.5</td>
      <td>16.5</td>
      <td>27.5</td>
      <td>29.5</td>
      <td>25.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11.5</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>30.5</td>
      <td>28.5</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17.5</td>
      <td>15.5</td>
      <td>11.0</td>
      <td>33.5</td>
      <td>29.5</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13.0</td>
      <td>12.5</td>
      <td>14.0</td>
      <td>30.0</td>
      <td>29.5</td>
      <td>28.5</td>
    </tr>
  </tbody>
</table>
</div>



### Fluxo de Ocupação

```
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
    <span style="color: #008000; text-decoration-color: #008000">'group_id'</span>: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'text'</span>: <span style="color: #008000; text-decoration-color: #008000">'Ocupacao em 15 minutos na faixa FM'</span>,
    <span style="color: #008000; text-decoration-color: #008000">'gps'</span>: GPS Data - Median of Coordinates: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span>:<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00000</span> Altitude: <span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-1.00</span> #Satellites: 
<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0.0</span>,
    <span style="color: #008000; text-decoration-color: #008000">'spectrum'</span>: <span style="font-weight: bold">[</span><span style="color: #800080; text-decoration-color: #800080; font-weight: bold">SpecData</span><span style="font-weight: bold">(</span><span style="color: #808000; text-decoration-color: #808000">type</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">65</span>, <span style="color: #808000; text-decoration-color: #808000">thread_id</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">121</span>, <span style="color: #808000; text-decoration-color: #808000">start_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">80.0</span>, <span style="color: #808000; text-decoration-color: #808000">stop_mega</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">110.0</span>, 
<span style="color: #808000; text-decoration-color: #808000">dtype</span>=<span style="color: #008000; text-decoration-color: #008000">'dBm'</span>, <span style="color: #808000; text-decoration-color: #808000">ndata</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">1536</span>, <span style="color: #808000; text-decoration-color: #808000">processing</span>=<span style="color: #008000; text-decoration-color: #008000">'peak'</span>, <span style="color: #808000; text-decoration-color: #808000">antuid</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">0</span>, <span style="color: #808000; text-decoration-color: #808000">thresh</span>=<span style="color: #008080; text-decoration-color: #008080; font-weight: bold">-60</span><span style="font-weight: bold">)]</span>
<span style="font-weight: bold">}</span>
</pre>



```
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


