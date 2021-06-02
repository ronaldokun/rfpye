conda create -n rfpye -c intel pip -y

conda activate rfpye

conda install -c intel libpython m2w64-toolchain -y

echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg

python -m pip install rfpye