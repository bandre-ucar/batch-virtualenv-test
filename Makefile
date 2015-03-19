# -*- mode: Makefile -*-
#
# To use virtualenv in a make file:
#
#	. test-env/bin/activate; pip install grako
#
# On machine without virtualenv
#
# pip install --user virtualenv
# PATH=$(PATH):$(HOME)/.local/bin
#
ENVNAME=test-env

SUBDIRS = \
	foo_lib \
	bar_lib \
#	app_mpi

# MAKECMDGOALS is the make option: make 'clobber' or 'all'
TARGET = $(MAKECMDGOALS)

# if target is undefined (i.e. MAKECMDGOALS is undefined), target = all
ifeq (,$(TARGET))
	TARGET = all
endif

#
# macro for executing TARGET in all SUBDIRS
#
ifdef SUBDIRS
$(SUBDIRS) : FORCE
	@if [ -d $@ ]; then \
		$(MAKE) --directory=$@ $(TARGET); \
	fi	
	@echo Build complete: $@ : $(TARGET) : $(shell date)
endif	


all : $(SUBDIRS)

env : $(VIRTUALENV)/bin/activate install-packages

$(VIRTUALENV)/bin/activate : 
	virtualenv --system-site-packages $(ENVNAME)


install-packages :
	. $(ENVNAME)/bin/activate; pip install sympy
	. $(ENVNAME)/bin/activate; pip install mpi4py











clean : FORCE
	-rm *~ *.pyc


clobber-env : clean
	-rm -rf $(ENVNAME)



FORCE :
