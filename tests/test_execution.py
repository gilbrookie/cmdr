import os
import pexpect
import re
import unittest

import data

PYTHON = "python"
APP1 = os.path.join(os.getcwd(), "tests/app1.py")
APP2 = os.path.join(os.getcwd(), "tests/app2.py")
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
        
        if not self.child.isalive:
            raise Exception("Problem starting child process") 

        # we can only read the welcome message once, so do it
        # immediately after spawning the process
        self.welcome = self._read_welcome()

    def _read_welcome(self):
        self.child.expect(self.ex_str)
        return self.child.match.group(0).rstrip(self.prompt)

    def send(self, s):
        self.child.sendline(s)
        self.child.expect(self.ex_str)
        return self.child.match.group(0).rstrip(self.prompt)

    def send_exit(self):
        self.child.sendline("exit")
        self.child.expect(pexpect.EOF)
        return self.child.before.lstrip("exit")

    def terminate(self):
        del self.child

# This is a basic test function for the CLICommon class
#def CLICommon_tester()
#    c = CLICommon(APP1, "->")
#    print c.welcome
#    print c.send("help")
#    print c.send_exit()


## Execution Test cases start here: ##


class TestCmdrWelcome(unittest.TestCase):

    def test_default_welcome(self):
        app = CLICommon(APP1, "->")
        self.assertEqual(app.welcome.replace("\r\n", ""),
                         data.CmdrSimple.welcome_msg.replace("\n", ""))
        
        app.terminate()
        del app

    def test_override_welcome(self):
        app = CLICommon(APP2,">>>") 
        self.assertEqual(app.welcome.replace("\r\n", ""),
                         data.CmdrOverrideParams.welcome_msg.replace("\n", ""))

        app.terminate()
        del app


class TestCmdrExit(unittest.TestCase):
    def test_default_exit(self):
        app = CLICommon(APP1, "->")
        self.assertEqual(app.send_exit().replace("\r\n", ""),
                         data.CmdrSimple.exit_msg.replace("\n", ""))
        
        app.terminate()
        del app

    def test_override_exit(self):
        app = CLICommon(APP2,">>>") 
        self.assertEqual(app.send_exit().replace("\r\n", ""),
                         data.CmdrOverrideParams.exit_msg.replace("\n", ""))
        
        app.terminate()
        del app


class TestHelpCmd(unittest.TestCase):
    def setUp(self):
        self.pattern = re.compile(r"^\s+(\w+)\s+([ \w]+)\s",
                                  re.MULTILINE|re.DOTALL)

    def test_only_builtins(self):
        app = CLICommon(APP1, "->")
        help_str = app.send("help") 
        print help_str

        res = self.pattern.findall(help_str)
        if not res:
            self.fail("Failed to match help string")
        else:
            print res

        self.assertEqual(len(res), 2)

        self.assertEqual(res[0], ("help", "Shows this menu"))
        self.assertEqual(res[1], ("exit", "Exits the app"))
    
        app.terminate()
        del app

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
