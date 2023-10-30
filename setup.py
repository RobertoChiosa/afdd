from pathlib import Path

from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='afdd',
    version='0.0.1',
    description='A python package for automated fault detection and diagnosis',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shuds13/pyexample',
    author='Roberto Chiosa',
    author_email='roberto.chiosa@polito.it',
    license='BSD 2-clause',
    packages=['afdd'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
