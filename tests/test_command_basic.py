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
    @cmdr.subcmd
    def sub1(self, *args):
        pass

    @cmdr.subcmd
    def sub2(self):
        pass

class TestCmd4(cmdr.Command):
    @cmdr.subcmd
    def sub1(self):
        pass

    def execute(self):
        pass

## End Test Data ##


## Test Classes ##

class TestCommandBasic(unittest.TestCase):
    def load_data(self):
        self.data={}
        self.data['name'] = self.__class__.__name__
        self.data['alt']= u'alt'
        self.data['exec_func'] = func_w_args
        self.data['description'] = u"Test description"

    def setUp(self):
        self.load_data()
        self.cmd = cmdr.Command(cmd=self.data['name'],
                                alt=self.data['alt'],
                                exec_func=self.data['exec_func'],
                                description=self.data['description'])

    def tearDown(self):
        self.cmd = None

    #def test_args(self):
    #    self.assertEqual(self.cmd.alt, self.data['alt'])

    def test_cmd_name(self):   
        self.assertEqual(self.cmd.name, self.data['name'])

    def test_cmd_description(self):
        self.assertEqual(self.cmd.description, self.data['description'])

    def test_cmd_exec_func(self):
        self.assertEqual(self.cmd.exec_func, self.data['exec_func'])

    def test_cmd_dict(self):
        c_dict = self.cmd.cmd_dict
        self.assertIn(self.data['name'], c_dict)
        self.assertEqual(self.data['description'],
                         c_dict[self.data['name']]['help'])
        self.assertEqual(self.data['alt'],
                         c_dict[self.data['name']]['alt'])
        self.assertEqual(self.data['exec_func'],
                         c_dict[self.data['name']]['exec_func'])

        self.assertEqual(None,
                         c_dict[self.data['name']]['comp_dict'])
        self.assertEqual({},
                         c_dict[self.data['name']]['subcmds'])

    def test_cmd_strs(self):
        self.assertEqual([self.data['name']],
                         self.cmd.cmd_strs)

        
class TestDirectCommand(unittest.TestCase):
    def setUp(self):
        self.cmd1 = cmdr.Command(cmd="Test")
        self.cmd2 = cmdr.Command(cmd="Test sub")
        self.cmd3 = cmdr.Command(cmd="Test", exec_func=func_w_args)
        self.cmd4 = cmdr.Command(cmd="Test sub", exec_func=func_no_args)

    def tearDown(self):
        self.cmd1 = None
        self.cmd2 = None
        self.cmd3 = None
        self.cmd4 = None

    def test_cmd_name(self):
        # the case for cmd1 covered in TestCommandBasic
        self.assertEqual("Test", self.cmd1.name)
        self.assertEqual("Test", self.cmd2.name)
        self.assertEqual("Test", self.cmd3.name)
        self.assertEqual("Test", self.cmd4.name)
    
    def test_subcmd_name(self):
        self.assertEqual({}, self.cmd1.subcmds)
        self.assertIn("sub", self.cmd2.subcmds)
        self.assertEqual({}, self.cmd3.subcmds)
        self.assertIn("sub", self.cmd4.subcmds)

    def test_exec_func(self):
        self.assertEqual(self.cmd1.exec_func,
                         self.cmd1.execute)
        self.assertEqual(self.cmd2.exec_func,
                         self.cmd2.execute)
        self.assertEqual(func_w_args,
                         self.cmd3.exec_func)

        self.assertEqual(self.cmd4.exec_func,
                         self.cmd4.execute)

        # Test the subcmd got assigned the exec_func
        self.assertEqual(func_no_args,
                         self.cmd4.subcmds["sub"]['exec_func'])


class TestSubclassCommand(unittest.TestCase):
    pass

class TestSubclassWithSubCmds(unittest.TestCase):
    pass

class TestDirectWithSubCmds(unittest.TestCase):
    pass