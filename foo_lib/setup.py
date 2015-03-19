from setuptools import setup, find_packages

setup(name='foolib',
      version='0.1',
      packages=find_packages(),
      description="foo library",
      scripts=['foolib/fooy.py'],
      url='url')
