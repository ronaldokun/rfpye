call conda deactivate

call conda create -n rfpy -c intel pip -y

call conda activate rfpy

call conda install -c intel libpython m2w64-toolchain -y

echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg

call python -m pip install Cython numpy

call python -m pip install -e .