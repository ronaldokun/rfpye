#!/bin/bash
conda deactivate
conda create -n rfpy_teste -c intel pip -y
conda activate rfpy_teste
conda install -c intel cython numpy -y
python -m pip install -e .