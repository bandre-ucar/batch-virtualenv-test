from setuptools import setup, find_packages


def get_requires():
    with open('requirements.txt', 'r') as f:
        data = f.read().strip()
    return data

setup(name='diagnostics',
      version='2.3.4+alpha1',
      packages=find_packages(),
      description="dummy diagnostics generator app",
      install_requires=get_requires(),
      scripts=['diagnostics/diags_generator.py'],
      package_data={'diagnostics': ['Templates/*.tmpl'],
                    'diagnostics': ['Config/*'],
                    }
      )
