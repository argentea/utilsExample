#!/bin/zsh

_oneDalHome=$HOME/test/oneDAL
_oneDalHome:=$HOME/project/oneDAL

__conda_setup="$('$HOME/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$HOME/anaconda3/etc/profile.d/conda.sh" ]; then
        . "$HOME/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="$HOME/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
conda activate oneDal
#conda list

#source /opt/intel/oneapi/tbb/latest/env/vars.sh intel64
source /opt/intel/oneapi/compiler/latest/env/vars.sh
export CPATH=$HOME/project/oneDAL/__deps/mklgpufpk/lnx/include:$CPATH
export CPATH=$HOME/anaconda3/envs/oneDal/include/linux:$HOME/anaconda3/envs/oneDal/include:$CPATH


cd $_oneDalHome;
make oneapi -j7 PLAT=lnx32e COMPILER=gnu
make daal -j7  PLAT=lnx32e COMPILER=gnu

