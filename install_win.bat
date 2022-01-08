call conda create -n rfpye -c intel pip -y

call conda activate rfpye

call conda install -c intel libpython m2w64-toolchain -y

echo [build_ext] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo define=MS_WIN64 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg

call python -m pip install rfpeye