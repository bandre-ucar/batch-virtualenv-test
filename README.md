proof of concept project to put together a python mpi application that can be run in the batch system of an HPC machine. 

* relies on system installed python packages like mpi4py and numpy.
* uses pip to install a dependency into a virtual environment
* installs itself into (libraries and application) into a virtual environment
* runs on the compute nodes of an hpc machine.


Dependencies
------------

required compiled libraries

* numpy
* scipy 
* matplotlib & basemap
* mpi4py
* netcdf4-python (?)
* PythonMagick (maybe http://docs.wand-py.org/en/0.4.0/)


On mac homebrew system:

brew install mpich2
brew tap homebrew/science
brew tap homebrew/python
brew install numpy scipy matplotlib matplotlib-basemap 


on 
