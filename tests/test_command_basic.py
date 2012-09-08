import unittest
import cmdr

## Test Data  ##

#Test callback functions
def func_w_args(*args):
    pass

def func_no_args():
    pass

#Test Command subclasses
class TestCmd1(cmdr.Command):
    pass

class TestCmd2(cmdr.Command):
    def execute(self, *args):
        return "override execute"

class TestCmd3(cmdr.Command):
    def sub1(self, *args):
        pass

    def sub2(self):
        pass

## End Test Data ##


## Test Classes ##

class TestCommandBasic(unittest.TestCase):
    def load_data():
        self.data={}
        self.data['name'] = self.__class__.__name__
        self.data['alt']= u'alt'
        self.data['exec_func'] = func_w_args
        self.data['description'] = u"Test description"

    def test_args():
        pass

    def test_cmd_name():   
        pass

    def test_cmd_dict():
        pass

    def test_cmd_strs():
        pass

    def test_execution_default():
        pass

    def test_execution_callback():
        pass


class TestDirectCommand(unittest.TestCase):
    pass

class TestSubclassCommand(unittest.TestCase):
    pass

class TestSubclassWithSubCmds(unittest.TestCase):
    pass

class TestDirectWithSubCmds(unittest.TestCase):
    pass
