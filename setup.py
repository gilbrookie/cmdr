#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmdr

setup(name="cmdr",
      version=cmdr.__version__,
      description="cmdr is a line based command interpreter framework/toolkit",
      long_description=open('Readme.rst').read(),
      author="James Gilbrook",
      author_email="james@gilbrook.ca",
      url="http://github.com/jamesgilbrook/cmdr",
      packages=['cmdr'],
      license=open('LICENSE.txt').read()
      )

