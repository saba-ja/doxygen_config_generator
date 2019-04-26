# Doxygen Config Generator
The python package is a simple Doxygen config generator tailored for C code document generation. The config generates both the html and xml version of the doc. All the Doxygen config parameters can be set with the Python program. The package uses a custom CSS and DoxygenLayout file to improve Doxygen appearance.

## Installation
Download or clone the repo. After activating the Pyhton virtual environment go to the top level folder containing the setup.py file. Run the following command to install the package in the virtual environment.

```python
pip install .

```


The package also can be installed directly from the repo using the following command:
```python
pip install git+https://github.com/saba-ja/doxygen_config_generator.git
```

The Git might ask for username and password since the repo.

## Getting started
To run the program use the following commands:
```python
from doxygen_config_generator import doxy_generator

doxy_generator.run(project_name='My Project', input_directory_or_files=['.', 'any other folder'], output_directory='path/to/output/folder/')

```
