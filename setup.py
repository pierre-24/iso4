# adapted over https://github.com/pypa/sampleproject/blob/master/setup.py

from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.readlines()

setup(
    name='iso4',
    version=0.1,

    # Description
    description='Implementation of ISO 4',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='adlpr',

    # Classifiers
    classifiers=[
        'Environment :: Scientific',
        'Operating System :: OS Independent',
        
        # Specify the Python versions:
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(),
    python_requires='>=3.5',

    # requirements
    install_requires=requirements,
)
