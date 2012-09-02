"""
aclip2 - Another command line interface powered with Python.

This module sets up the main interface for the public API.

"""

__title__ = "aclip2"
__version__ = "0.0.2"
__author__ = "James Gilbrook"
__licence__ = "ISC"
__copyright__ = "Copyright 2012 James Gilbrook"

# Expose the public api via imports of submodules

from command import Command, subcmd
from application import Application

