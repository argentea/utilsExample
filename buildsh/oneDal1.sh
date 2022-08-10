#!/bin/zsh

__conda_setup="$('/home/kp/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kp/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kp/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kp/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
conda activate oneDal
#conda list

#source /opt/intel/oneapi/tbb/latest/env/vars.sh intel64
source /opt/intel/oneapi/compiler/latest/env/vars.sh
export CPATH=~/project/oneDAL/__deps/mklgpufpk/lnx/include:$CPATH
export CPATH=/home/kp/anaconda3/envs/oneDal/include/linux:/home/kp/anaconda3/envs/oneDal/include:$CPATH


make onedal -j7 PLAT=lnx32e COMPILER=gnu
