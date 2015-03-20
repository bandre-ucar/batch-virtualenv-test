proof of concept project to put together a python mpi application that can be run in the batch system of an HPC machine. 

* relies on system installed python packages like mpi4py and numpy.
* uses pip to install a dependency into a virtual environment
* installs itself into (libraries and application) into a virtual environment
* runs on the compute nodes of an hpc machine.


Dependencies
============

required bootstrap:

* python2
* pip
* virtualenv

required compiled libraries:

* numpy
* scipy 
* matplotlib & basemap
* mpi4py
* netcdf4-python (?)
* PythonMagick (maybe http://docs.wand-py.org/en/0.4.0/)


Bootstrap
=========

Mac homebrew system
-------------------

```bash
brew install mpich2
brew tap homebrew/science
brew tap homebrew/python
brew install numpy scipy matplotlib matplotlib-basemap 
```

Yellowstone
-----------

Note, yellowstone doesn't have virtualenv installed yet. You need to
bootstrap it with:

```bash

    pip install --user virtualenv
    export PATH=$PATH:$HOME/.local/bin

```


Workflow
========

Users
-----

```bash

    cd $(POSTPROCESSING_DIR)
    ./create_diags.sh
    # ./test-app-osx.run
    # or
    # bsub ./test-app-yellowstone.run
    
```


Developers
----------


```bash

    # load modules if necessary
    module load python/2.7.7
    module load numpy/1.8.1
    module load scipy/0.15.1

    make clobber-env
    make env
    . test-env/bin/activate
    make all
    make test
    # do development stuff....
    diag_util_test.py
    # mpiexect -np 4 diags_generator.py
    # DAV_CORES=4 execca mpirun.lsf diags_generator.py
    deactivate

```
