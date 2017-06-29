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