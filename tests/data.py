"""
data.py - a collection of test data used by the unitests

This includes:

    * Callback functions (for Commands)
    * Command Subclasses
    * Cmdr Instances


"""

import cmdr


def func_w_args(*args):
    pass


def func_no_args():
    pass


#Test Command subclasses
class TestCmd1(cmdr.Command):
    """TestCmd1 help str"""
    pass


class TestCmd2(cmdr.Command):
    """TestCmd2 help str"""
    def execute(self, *args):
        return "override execute"


class TestCmd3(cmdr.Command):
    """TestCmd3 help str"""

    @cmdr.subcmd
    def sub1(self, *args):
        """Test sub1"""
        pass

    @cmdr.subcmd
    def sub2(self):
        """Test sub2"""
        pass


class TestCmd4(cmdr.Command):
    @cmdr.subcmd
    def sub1(self):
        pass

    def execute(self):
        pass


### Cmdr Instances ###
CmdrSimple = cmdr.Cmdr("CmdrSimple")
CmdrOverrideParams = cmdr.Cmdr("CmdrOverrideParams",
                               intro_msg="Override Welcome Message",
                               exit_msg="Override Exit Message",
                               prompt_str="$>")

CmdrBasicCmds = cmdr.Cmdr("CmdrBasicCmds")
CmdrBasicCmds.register_cmd(TestCmd1())
CmdrBasicCmds.register_cmd(TestCmd2())

CmdrSubCmds = cmdr.Cmdr("CmdrSubCmds")
CmdrBasicCmds.register_cmd(TestCmd3())
CmdrBasicCmds.register_cmd(TestCmd4())

# Use decorated commands (app name is short for convenience.
app = cmdr.Cmdr("CmdrDecoratedCmds")


@app.cmd
def decorated_no_args():
    return "decorated_no_args"


@app.cmd
def decorated_w_args(args):
    return "decorated_w_args"

# rename the app to a more descriptive name
CmdrDecoratedCmds = app
del app
