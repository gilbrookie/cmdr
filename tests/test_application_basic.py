
import unittest
import cmdr


class TestCmdrDefaultAttrs(unittest.TestCase):
    def load_data(self):
        self.data = {}
        self.data['name'] = self.__class__.__name__
        self.data['intro_msg'] = cmdr.Cmdr.DEFAULT_WELCOME
        self.data['exit_msg'] = cmdr.Cmdr.DEFAULT_EXIT
        self.data['prompt'] = cmdr.Cmdr.DEFAULT_PROMPT

    def setUp(self):
        self.load_data()
        self.app = cmdr.Cmdr(self.data['name'])

    def tearDown(self):
        self.app = None

    def test_app_name(self):
        self.assertEqual(self.app.app_name, self.data['name'])

    def test_app_prompt(self):
        self.assertEqual(self.app.prompt, self.data['prompt'])

    def test_intro_msg(self):
        self.assertEqual(self.app.welcome_msg,
                         self.data['intro_msg'] % self.__class__.__name__)

    def test_exit_msg(self):
        self.assertEqual(self.app.exit_msg, self.data['exit_msg'])


class TestCmdrOverrideAttrs(unittest.TestCase):
    def load_data(self):
        self.data = {}
        self.data['name'] = self.__class__.__name__
        self.data['prompt'] = u">!@#"
        self.data['intro_msg'] = u"Hello World"
        self.data['exit_msg'] = u"\nByeBYE!"

    def setUp(self):
        self.load_data()
        self.app = cmdr.Cmdr(self.data['name'],
                             prompt_str=self.data['prompt'],
                             intro_msg=self.data['intro_msg'],
                             exit_msg=self.data['exit_msg'])

    def tearDown(self):
        self.app = None

    def test_app_name(self):
        self.assertEqual(self.app.app_name, self.data['name'])

    def test_app_prompt(self):
        self.assertEqual(self.app.prompt, self.data['prompt'])

    def test_intro_msg(self):
        self.assertEqual(self.app.welcome_msg, self.data['intro_msg'])

    def test_exit_msg(self):
        self.assertEqual(self.app.exit_msg, self.data['exit_msg'])


class TestCmdrCommandRegistration(unittest.TestCase):
    def test_register_as_args(self):

        num_cmds = 10
        cmd_list = generate_cmd_helper(num_cmds)
        app = cmdr.Cmdr(__name__, registered_commands=cmd_list)

        # Consider the builting commands
        self.assertEqual(len(app.registered_cmds), num_cmds + 2)

        del cmd_list
        del app

    def test_builtin_cmds(self):

        app = cmdr.Cmdr(__name__)

        self.assertEqual(len(app.registered_cmds), 2)

        cmd_names = [c.name for c in app.registered_cmds]
        self.assertIn("help", cmd_names)
        self.assertIn("exit", cmd_names)

        del app

    def test_register_func(self):

        num_cmds = 50
        c_list = generate_cmd_helper(num_cmds)
        app = cmdr.Cmdr(__name__)

        for c in c_list:
            app.register_cmd(c)

        self.assertEqual(len(app.registered_cmds), num_cmds + 2)

        del c_list
        del app

    def test_register_decorator(self):

        app = cmdr.Cmdr(__name__)

        @app.cmd("test")
        def test():
            pass

        self.assertEqual(len(app.registered_cmds), 3)

        del app


# Helper functions
def generate_cmd_helper(num):

    c_list = []
    name_prefix = "TestCmd%s"
    for i in xrange(num):
        name = name_prefix % i
        c_list.append(cmdr.Command(name))

    return c_list


if __name__ == '__main__':
    unittest.main()
