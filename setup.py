from setuptools import setup

setup(
    name='doxygen_config_generator',
    version='1.2',
    packages=['doxygen_config_generator'],
    url='http://github.jpl.nasa.gov/janamian/doxygen_config_generator',
    license='MIT',
    author='Saba janamian',
    author_email='saba.janamian@jpl.nasa.gov',
    Description='Generate Doxygen config file tailored for C source code documentation and custom CSS and layout.',
    install_requires=[],
    include_package_data=True,
    Platform='Linux',
    package_data={
        '': ['customdoxygen.css', 'DoxygenLayout.xml']
    }
)
