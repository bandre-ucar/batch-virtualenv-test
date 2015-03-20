#!/usr/bin/env bash
#
# script to show how to setup environment during diagnostrics workflow 
#


echo "load modules for hpc machine here"

# create the virtual environment. Makefile checks to see if it is
# already setup, so only done once per case.
make env

# activate it for this script
. test-env/bin/activate

# install post processing packages
make all

#
echo "Testing post processing install"
diag_util_test.py


# cleanup and deactivate the virtualenv. probably not strictly necessary
deactivate
