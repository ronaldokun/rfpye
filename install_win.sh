mamba create -n rfpye39 -c intel pip -y

mamba activate rfpye39

mamba install libpython m2w64-toolchain python=3.9 -c conda-forge -y

echo [build_ext] > $CONDA_PREFIX\Lib\distutils\distutils.cfg

echo define=MS_WIN64 >> $CONDA_PREFIX\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> $CONDA_PREFIX\Lib\distutils\distutils.cfg

python -m pip install rfpye39