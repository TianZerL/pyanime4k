#!/bin/bash -e
# Name: PyAnime4K setup script for ubuntu
# Author: TianZerL

if [ ! -z "$1" ]; then
    export INSTALLATION_PATH=$1
else
    export INSTALLATION_PATH="$HOME/pyanime4k_wheel/"
fi

TEMP="/tmp/pyanime4k"

git clone https://github.com/TianZerL/pyanime4k.git $TEMP/pyanime4k

apt-get update
apt install -y --no-install-recommends libopencv-dev ocl-icd-opencl-dev cmake python3-pip

git clone https://github.com/TianZerL/Anime4KCPP.git $TEMP/anime4kcpp

mkdir -v $TEMP/anime4kcpp/build
cd $TEMP/anime4kcpp/build
cmake -DBuild_CLI=OFF -DBuild_C_wrapper=ON -DBuild_C_wrapper_with_core=ON ..
make -j$(nproc)

mv -v $TEMP/anime4kcpp/build/bin/libac.so $TEMP/pyanime4k/pyanime4k/wrapper

cd $TEMP/pyanime4k

<<<<<<< HEAD
pip install -r requirements.txt

=======
>>>>>>> 3e3009f89feae80fb7e2f29bee5af13b68f2e8a7
pip3 install setuptools
pip3 install wheel

python3 $TEMP/pyanime4k/setup.py bdist_wheel

mv -v $TEMP/pyanime4k/dist $INSTALLATION_PATH

rm -rf $TEMP

echo "All finished."
echo "Your wheel file of pyanime4k was stored in $INSTALLATION_PATH"
echo "Use pip install $INSTALLATION_PATH$(ls $INSTALLATION_PATH) to install it"
