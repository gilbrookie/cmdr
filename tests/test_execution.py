import os
import pexpect
import re
import unittest

import data

PYTHON = "python"
APP1 = os.path.join(os.getcwd(), "tests/app1.py")
APP2 = os.path.join(os.getcwd(), "tests/app2.py")
APP3 = os.path.join(os.getcwd(), "tests/app3.py")


class CLICommon(object):
    """
    CLICommon is a helper class that spawns the test apps and allows
    interaction between the app and the test cases

    Uses pexpect to handle spawning and interacting with the processes

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
        app = CLICommon(APP2, ">>>")
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
        app = CLICommon(APP2, ">>>")
        self.assertEqual(app.send_exit().replace("\r\n", ""),
                         data.CmdrOverrideParams.exit_msg.replace("\n", ""))

        app.terminate()
        del app

    def test_exit_shortcut(self):
        pass

    def test_ctrl_c_exit(self):
        pass

    def test_ctrl_d_exit(self):
        pass


class TestHelpCmd(unittest.TestCase):

    def setUp(self):
        self.pattern = re.compile(r"^\s+(\w+)\s+([ \w]+)\s",
                                  re.MULTILINE | re.DOTALL)

    def test_only_builtins(self):
        app = CLICommon(APP1, "->")
        help_str = app.send("help")

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
        app = CLICommon(APP2, ">>>")
        help_str = app.send("help")

        res = self.pattern.findall(help_str)
        if not res:
            self.fail("Failed to match help string")
        else:
            print res

        self.assertEqual(len(res), 4)

        self.assertEqual(res[0], ("help", "Shows this menu"))
        self.assertEqual(res[1], ("exit", "Exits the app"))
        self.assertEqual(res[2], ("testcmd1", "TestCmd1 help str"))
        self.assertEqual(res[3], ("testcmd2", "TestCmd2 help str"))

        app.terminate()
        del app

    def test_registered_subcmds(self):
        app = CLICommon(APP3, "->")
        help_str = app.send("help")

        res = self.pattern.findall(help_str)
        if not res:
            self.fail("Failed to match help string")
        else:
            print res

        self.assertEqual(len(res), 6)

        self.assertEqual(res[0], ("help", "Shows this menu"))
        self.assertEqual(res[1], ("exit", "Exits the app"))
        self.assertEqual(res[2],
                         ("no_args", "Decorated command with no arguments"))
        self.assertEqual(res[3],
                         ("with_args", "Decorated command with arguments"))
        self.assertEqual(res[4], ("testcmd3", "TestCmd3 help str"))
        self.assertEqual(res[5], ("testcmd4", "None"))

        app.terminate()
        del app

    def test_help_shortcut(self):
        pass


class TestSimpleCmds(unittest.TestCase):

    def setUp(self):
        self.app = CLICommon(APP3, "->")

    def tearDown(self):
        self.app.terminate()

    def test_single_cmd_no_args(self):
        res = self.app.send("no_args")
        self.assertEqual(re.findall("decorated_no_args", res)[0],
                         "decorated_no_args")

    def test_single_cmd_w_args(self):
        res = self.app.send("with_args 1")
        self.assertEqual(re.findall("decorated_w_args 1", res)[0],
                         "decorated_w_args 1")

    def test_subcmd_no_args(self):
        res = self.app.send("testcmd3 sub2")
        self.assertEqual(re.findall("Test sub2", res)[0],
                         "Test sub2")

    def test_subcmd_w_args(self):
        res = self.app.send("testcmd3 sub1 1")
        self.assertEqual(re.findall("Test sub1 1", res)[0],
                         "Test sub1 1")


class TestCmdErrors(unittest.TestCase):
    def test_unknown_cmd(self):
        pass

    def test_args_mismatch(self):
        pass
