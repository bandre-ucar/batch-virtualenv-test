from setuptools import setup, find_packages

setup(name='cesm_utils',
      version='0.1.2',
      packages=find_packages(),
      test_suite='cesm_utils.tests',
      description="pseudo cesm_utils library")
