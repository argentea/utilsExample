#!/bin/zsh
#

_oneDalHome=$HOME/test/oneDAL

_oneDalHome:=$HOME/project/oneDAL
_sampleHome=$_oneDalHome/samples/oneapi/dpc/ccl

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

#find dpcc 
source /opt/intel/oneapi/compiler/latest/env/vars.sh
#find daal interface
export CPATH=$_oneDalHome/__release_lnx_gnu/daal/latest/include:$CPATH
export CPATH=$_oneDalHome/__release_lnx_gnu/tbb/latest/include:$CPATH

#find mpi
source /opt/intel/oneapi/mpi/2021.6.0/env/vars.sh

#find ccl
source /opt/intel/oneapi/ccl/2021.6.0/env/vars.sh
#export CPATH=/opt/intel/oneapi/mpi/2021.6.0/include:$CPATH

#export CPATH=$_oneDalHome/__deps/mklgpufpk/lnx/include:$CPATH
#export CPATH=$HOME/anaconda3/envs/oneDal/include/linux:$HOME/anaconda3/envs/oneDal/include:$CPATH

echo $CPATH


cd $_sampleHome

make sointel64
