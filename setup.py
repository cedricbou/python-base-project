"""Conventional Setup.py file"""
from setuptools import setup

setup(name='fiddlewith',
      version='1.0',
      py_modules=['fiddlewith'],
      package_dir={'': 'src'},
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
     )
