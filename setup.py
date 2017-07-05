// Copyright 2016, RadiantBlue Technologies, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import imp
from codecs import open
from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
__version__ = imp.load_source('shape.version', 'SHAPE/version.py').__version__

with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]

setup(
    name='shape',
    version=__version__,
    description='Draw a random shape on top of your satellite image.',
    author='Brady Madden (bradymadden97)',
    url='https://github.com/bradymadden97/bfalg-shape',
    scripts=['SHAPE/shape.py'],
    install_requires=install_requires,
)