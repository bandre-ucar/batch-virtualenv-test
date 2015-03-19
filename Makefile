# -*- mode: Makefile -*-
#
# To use virtualenv in a make file:
#
#	. test-env/bin/activate; pip install grako
#

VIRTUALENV=test-env

env : $(VIRTUALENV)/bin/activate install-packages

$(VIRTUALENV)/bin/activate : 
	$(HOME)/.local/bin/virtualenv test-env


install-packages :
	. test-env/bin/activate; pip install sympy












clean : FORCE
	-rm *~ *.pyc


clobber-env : clean
	-rm -rf test-env



FORCE :
