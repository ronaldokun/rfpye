#!/bin/bash
source deactivate
conda create -n rfpy -c intel pip -y
conda activate rfpy
python -m pip install -e .