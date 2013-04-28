import unittest

class SanityTest(unittest.TestCase):
    def test_module_import_cmdr(self):
        try:
            import cmdr
        except ImportError as ex:
            self.fail()

    def test_module_import_cmdr_application(self):
        try:
            import cmdr.application
        except ImportError as ex:
            self.fail()

    def test_module_import_cmdr_command(self):
        try:
            import cmdr.command
        except ImportError as ex:
            self.fail()

    def test_module_import_cmdr_state(self):
        try:
            import cmdr.state
        except ImportError as ex:
            self.fail()

    def test_module_import_cmdr_version(self):
        import cmdr
        self.assertTrue(cmdr.__version__)

    def test_symbol_import_cmdr(self):

        try:
            from cmdr import Cmdr
        except ImportError as ex:
            self.fail()
        self.assertTrue(Cmdr)

    def test_symbol_import_cmdr_command(self):
        try:
            from cmdr import Command
        except ImportError as ex:
            self.fail()
        self.assertTrue(Command)

    def test_symbol_import_cmdr_subcmd(self):
        try:
            from cmdr import subcmd
        except ImportError as ex:
            self.fail()
        self.assertTrue(subcmd)
    
    def test_symbol_import_cmdr_state(self):
        try:
            from cmdr import state
        except ImportError as ex:
            self.fail()
        self.assertTrue(state)

    def test_Cmdr_create(self):
        import cmdr
        c = cmdr.Cmdr(__name__)
        self.assertIsInstance(c, cmdr.Cmdr)

    def test_Command_create(self):
        import cmdr
        c = cmdr.Command()
        self.assertIsInstance(c, cmdr.Command)


if __name__ == '__main__':
    unittest.main()
