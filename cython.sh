conda deactivate
conda activate rfpy
conda install libpython m2w64-toolchain cython
echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg
echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg