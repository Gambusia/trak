"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject

This document is based on setup.py from the github.com URL given above.
For explanations of each directive, instructions are provided in the original.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='trak',  # Required
    version='0.0.1',  # Required
    description='A simple tool for tracking writing progress',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/Gambusia/trak',  # Optional
    author='Greg Pyle',  # Optional
    author_email='chaoborid@gmail.com',  # Optional

    classifiers=[  # Optional
        'Development Status :: 4 - Beta',
        'Intended Audience :: Writers',
        'Topic :: writing :: progress tracking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    keywords='writing, progress tracking, utility',  # Optional
    package_dir={'': 'src'},  # Optional
    packages=find_packages(where='src'),  # Required
    python_requires='>=3.8, <4',
    install_requires=['tabulate'],  # Optional
    package_data={  # Optional
        'sample': ['data/'],
    },

    entry_points={  # Optional
        'console_scripts': [
            'trak=trakr:main',
        ],
    },

    project_urls={  # Optional
        'Source': 'https://github.com/Gambusia/trak',
    },
) 
