```
pyenv virtualenv 3.9.12 wham
pyenv virtualenv 3.10.11 wham_3.10
pyenv activate wham_3.10

python -m pip install --upgrade pip
python -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113

python -m pip install fvcore iopath
python -m pip install pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py39_cu113_pyt1110/download.html


python -m pip install pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/py310_cu113_pyt1110/download.html

# If missing setuptools at any point, re-run
python -m pip uninstall setuptools
python -m pip install setuptools

python -m pip install wheel
python -m pip install -r requirements.txt
python -m pip install -v -e third-party/ViTPose

cd third-party/DPVO
wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip
unzip eigen-3.4.0.zip -d thirdparty && rm -rf eigen-3.4.0.zip

# Andrea Notes: make sure using cuda 11 (not 12)
# in /usr/local


pip install torch-scatter -f https://data.pyg.org/whl/torch-1.11.0%2Bcu113.html
pip install .
```