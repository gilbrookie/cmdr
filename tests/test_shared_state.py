import unittest
from cmdr import state
import cmdr
from data import TestCmd1, CmdrSimple

class TestBasicSharedState(unittest.TestCase):
    def setUp(self):
        self.app = cmdr.Cmdr("state_test")
        self.cmd = TestCmd1()
        self.app.register_cmd(self.cmd)
        self.st = state.StateController("Monitor")

    def testDown(self):
        self.app = None # cleanup app and commands 
        self.cmd = None
        self.st = None
        pass

    def test_default_state(self):
        self.assertEqual(self.st._app_state, {})

    def test_state_vars_created_by_app(self):
        key = "app_v1"
        val = "created_by_app"
        self.app.app_state[key] = val
        self.assertEqual(self.st[key], val )

    def test_state_vars_created_by_cmds(self):
        key = "cmd_v1"
        val = "created_by_cmd"
        self.cmd.app_state[key] = val
        self.assertEqual(self.st[key], val )

    def test_state_vars_read_by_app(self):
        key = "cmd_v2"
        val = "created_by_cmd"
        self.cmd.app_state[key] = val
        self.assertEqual(self.app.app_state[key], val )

    def test_state_vars_read_by_cmds(self):
        key = "cmd_v2"
        val = "created_by_cmd"
        self.app.app_state[key] = val
        self.assertEqual(self.cmd.app_state[key], val )

    def test_state_vars_modified_by_app(self):
        key = "cmd_v3"
        val1 = "val1"
        val2 = "modified"
        self.cmd.app_state[key] = val1
        self.assertEqual(self.app.app_state[key], val1 )
        self.app.app_state[key] = val2
        self.assertEqual(self.cmd.app_state[key], val2 )


    def test_stats_vars_modified_by_cmds(self):
        key = "app_v2"
        val1 = "v2"
        val2 = "modified"
        self.app.app_state[key] = val1
        self.assertEqual(self.cmd.app_state[key], val1)
        self.cmd.app_state[key] = val2
        self.assertEqual(self.app.app_state[key], val2)

if __name__ == '__main__':
    unittest.main()
