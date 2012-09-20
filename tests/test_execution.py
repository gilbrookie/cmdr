import os
import subprocess
import unittest

import pexpect

PYTHON = "python"
APP1 = os.path.join(os.getcwd(), "app1.py")
#APP1 = "app1.py"


class CLICommon(object):
    """
    CLICommon is a helper class that spawns the test apps and allows 
    interaction between the app and the test cases

    Uses pexpect to search for responses from commands

    Special cases:

    #. welcome message - this can only be read once (at the start of the script)
        so it is done automatically on __init__ and store as :attr:`welcome` 
        attribute

    #. exit - In this case the regex used for the regular commmand breaks because
        it needs to look specifically for EOF.  If you are testing the exit
        command, used :meth:`send_exit()`


    """
    def __init__(self, mod, prompt_str):
        self.child = pexpect.spawn("python %s" % mod)
        self.prompt = prompt_str
        self.ex_str = "(.*?)%s" % self.prompt

        # we can only read the welcome message once, so do it 
        # immediately after spawning the process
        self.welcome = self._read_welcome()

    def _read_welcome(self):
        self.child.readline()
        self.child.expect(self.ex_str)
        return self.child.match.group(0)

    def send(self, s):
        self.child.sendline(s)
        self.child.expect(self.ex_str)
        return self.child.match.group(0)

    def send_exit(self):
        self.child.sendline("exit")
        self.child.expect(pexpect.EOF)
        return self.child.before

    def terminate(self):
        self.child.kill()

# This is a basic test function for the CLICommon class
#def CLICommon_tester()
#    c = CLICommon(APP1, "->")
#    print c.welcome
#    print c.send("help")
#    print c.send_exit()


## Execution Test cases start here: ##


class TestCmdrExec(unittest.TestCase):
    def setUp(self):
        #self.app = CLICommon(APP1, "->")
        pass

    def tearDown(self):
        #self.app.terminate()
        pass

class TestCmdrWelcome(unittest.TestCase):

    def test_default_welcome(self):
        pass

    def test_override_welcome(self):
        pass

class TestCmdrExit(unittest.TestCase):
    def test_default_exit(self):
        pass

    def test_override_exit(self):
        pass

class TestHelpCmd(unittest.TestCase):
    def test_only_builtins(self):
        pass

    def test_registered_commands(self):
        pass


class TestSimpleCmds(unittest.TestCase):
    def test_single_cmd_no_args(self):
        pass

    def test_single_cmd_w_args(self):
        pass

    def test_subcmd_no_args(self):
        pass

    def test_subcmd_w_args(self):
        pass

class TestCmdErrors(unittest.TestCase):
    def test_unknown_cmd(self):
        pass

    def test_args_mismatch(self):
        pass


