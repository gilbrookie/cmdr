#!/usr/bin/python
from data import CmdrOverrideParams, TestCmd1, TestCmd2

CmdrOverrideParams.register_cmd(TestCmd1())
CmdrOverrideParams.register_cmd(TestCmd2())

CmdrOverrideParams.start()
