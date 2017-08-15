#!/usr/bin/env python

# Copyright 2017, RadiantBlue Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from codecs import open
from setuptools import setup, find_packages
import imp

here = os.path.abspath(os.path.dirname(__file__))
__version__ = imp.load_source('bfalg_shape.version', 'bfalg_shape/version.py').__version__


install_requires = ['pillow==4.2.1', 'pyproj==1.9.5.1', 'gdal==2.1.3', 'requests==2.18.1']

setup(
    name='bfalg-shape',
    version=__version__,
    description='Test Shape Algorithm',
    author='',
    license='Apache License 2.0',
    url='https://github.com/venicegeo/bfalg-shape',
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points = {
        'console_scripts': ['bfalg-shape=bfalg_shape.shape:cli'],
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
