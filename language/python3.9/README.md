# Tensorflow env setup

> brew list | grep python
python-packaging
python-setuptools
python@3.10
python@3.11
python@3.12
python@3.13
python@3.9

> file $(which python3)
/usr/local/bin/python3: Mach-O 64-bit executable x86_64
<!-- Since your MacBook Pro uses an x86_64 architecture (Intel processor) 
and you have an x86_64 version of Python, 
you should install the standard TensorFlow package for CPU-only support. -->

<!-- https://conda-forge.org/miniforge -->
> chmod +x ~/Downloads/Miniforge3-24.7.1-2-MacOSX-arm64.sh
> sh ~/Downloads/Miniforge3-24.7.1-2-MacOSX-arm64.sh

export PATH=$PATH:"/Users/yangjiang/miniforge3/bin"
> conda init zsh

> conda info --envs
> conda list | grep python
brotli-python             1.1.0            py39hfa9831e_2    conda-forge
python                    3.9.20          h9e33284_1_cpython    conda-forge
python_abi                3.9                      5_cp39    conda-forge

> conda create -p tensorflow_env python=3.9
> conda activate /Users/yangjiang/tensorflow_env
> conda list | grep python
python                    3.9.20          h9e33284_1_cpython    conda-forge

> file /Users/yangjiang/miniforge3/bin/python
/Users/yangjiang/miniforge3/bin/python: Mach-O 64-bit executable arm64

> conda install -c apple tensorflow-deps
> conda list | grep python
python                    3.9.19          hd7ebdb9_0_cpython    conda-forge
python_abi                3.9                      5_cp39    conda-forge

> pip install tensorflow-macos==2.14
> pip install tensorflow-metal==1.1.0
> conda list | grep tensorflow
tensorflow-deps           2.10.0                        0    apple
tensorflow-estimator      2.14.0                   pypi_0    pypi
tensorflow-io-gcs-filesystem 0.37.1                   pypi_0    pypi
tensorflow-macos          2.14.0                   pypi_0    pypi
tensorflow-metal          1.1.0                    pypi_0    pypi

> python -c 'import tensorflow as tf; print(tf.__version__); print(tf.config.list_physical_devices("GPU"))'
2.14.0
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.0.2 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.
> pip install "numpy<2" 

# Active / deactivate / remove env

> conda activate /Users/yangjiang/tensorflow_env
> conda deactivate
> conda env remove -p /Users/yangjiang/tensorflow_env

# Others

> pip install python-binance ta pandas tqdm matplotlib scikit-learn

> python motion.py
