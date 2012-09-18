import unittest


class SanityTest(unittest.TestCase):
    def test_module_import(self):
        try:
            import cmdr
        except ImportError, ex:
            self.fail("ImportError", ex)

        try:
            import cmdr.application
        except ImportError, ex:
            self.fail("ImportError", ex)

        try:
            import cmdr.command
        except ImportError, ex:
            self.fail("ImportError", ex)

        self.assertTrue(cmdr.__version__)

    def test_symbol_import(self):

        try:
            from cmdr import Cmdr
        except ImportError, ex:
            self.fail("ImportError", ex)

        try:
            from cmdr import Command
        except ImportError, ex:
            self.fail("ImportError", ex)

        try:
            from cmdr import subcmd
        except ImportError, ex:
            self.fail("ImportError", ex)

        self.assertTrue(Cmdr)
        self.assertTrue(Command)
        self.assertTrue(subcmd)

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
