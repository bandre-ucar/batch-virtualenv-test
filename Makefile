# -*- mode: Makefile -*-
#
# NOTES:
#
# - To use virtualenv in a make file:
#
#	. test-env/bin/activate; pip install grako
#
#   I don't think we want to do that because we want to use a
#   requirements.txt file.
#
# - On machine without virtualenv
#
#   pip install --user virtualenv
#   export PATH=$(PATH):$(HOME)/.local/bin
#   virtualenv --system-site-packages ENVNAME
#
ENVNAME=test-env

SUBDIRS = \
	cesm_utils \
	diag_utils \
	mpi_app_diags

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

test : $(SUBDIRS)

env : $(VIRTUALENV)/bin/activate

$(VIRTUALENV)/bin/activate : 
	virtualenv --system-site-packages $(ENVNAME)


#
# cleanup 
#
clean : FORCE
	-rm *~ *.pyc


clobber-env : clean
	-rm -rf $(ENVNAME)



FORCE :
