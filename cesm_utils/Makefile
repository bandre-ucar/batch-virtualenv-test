all : develop

test : FORCE
	python -m unittest discover --start-directory cesm_utils/tests

develop : FORCE
	python setup.py $@

install : FORCE
	python setup.py $@


FORCE :
