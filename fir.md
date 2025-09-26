
# Interactive Session on Fir 
(can experiment with CPU/memory if needed but likely don't want to go lower than this)

```salloc --time=3:0:0 --mem-per-cpu=16G --ntasks=1 --account=def-btaati_gpu --gpus=nvidia_h100_80gb_hbm3_1g.10gb:1```

# Installation Instructions
## Load modules
```
module load StdEnv/2023 cuda/12.2 gcc/12.3
module load python/3.12.4
module load opencv/4.12.0
```

## Only create the environment once
```
python -m venv env_3.12.4
```

## Use virtualenv
```
source ~/projects/def-btaati/shared/WHAM/env_3.12.4/bin/activate
```

## Install Dependencies
```
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --no-index

pip install fvcore iopath wheel --no-index
pip install pytorch3d==0.7.8 --no-index

pip install -r requirements.txt

pip install -v -e third-party/ViTPose
```

<!-- # Install DPVO (optional - didn't get this working as not a priority)
cd third-party/DPVO
wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip
unzip eigen-3.4.0.zip -d thirdparty && rm -rf eigen-3.4.0.zip
pip install torch-scatter==2.0.9

pip install . -->
