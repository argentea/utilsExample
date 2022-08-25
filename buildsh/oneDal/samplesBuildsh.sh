#!/bin/zsh

## Copyright 2022 Intel Corporation
##
##  Content:
##     scripts for oneAPI Data Analytics Library building
##
##                                           by kunpeng: kunpeng.jiang@intel.com
##******************************************************************************


#Please set your oneDal source home intel oneapi toolkit home and 
#sampleHome properly

_oneDalHome=$HOME/project/oneDAL
_intelOneapiHome=$HOME/intel/oneapi
_sampleHome=$_oneDalHome/__release_lnx_gnu/daal/latest/samples/oneapi/dpc/ccl/

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

#find dpcpp 
source $_intelOneapiHome/compiler/latest/env/vars.sh
#find mpi
source $_intelOneapiHome/mpi/latest/env/vars.sh
#find ccl
source $_intelOneapiHome/ccl/latest/env/vars.sh
#find tbb
source $_intelOneapiHome/tbb/latest/env/vars.sh
#Setup openjdk path
#Which is necessary for daal
export CPATH=$HOME/anaconda3/envs/oneDal/include/linux:$HOME/anaconda3/envs/oneDal/include:$CPATH

#Setup shared library location
export LD_LIBRARY_PATH=$HOME/project/oneDAL/__release_lnx_gnu/tbb/latest/lib/intel64:$LD_LIBRARY_PATH

#build
cd $_sampleHome
make sointel64
