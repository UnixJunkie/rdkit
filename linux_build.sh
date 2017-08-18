#!/bin/bash

#set -x # DEBUG
set -e

export RDBASE=$PWD
export LD_LIBRARY_PATH=$RDBASE/lib
export PYTHONPATH=$PYTHONPATH:$RDBASE

mkdir -p build
cd build
cmake ..
make
