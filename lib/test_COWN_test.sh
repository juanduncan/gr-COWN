#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/juan/cognitive/gr-COWN/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/juan/cognitive/gr-COWN/lib:$PATH
export LD_LIBRARY_PATH=/home/juan/cognitive/gr-COWN/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-COWN 
