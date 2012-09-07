
import unittest
import cmdr

       
class TestCmdrAttrs(unittest.TestCase):
    def load_data(self):
        self.data = {}
        self.data['name'] = self.__class__.__name__
        self.data['prompt'] = u">!@#"
        self.data['intro_msg'] = u"Hello World"
        self.data['exit_msg'] = u"\nBye!"

    def setUp(self):
        self.load_data()
        self.app = cmdr.Cmdr(self.data['name'], 
                             prompt_str=self.data['prompt'], 
                             intro_msg=self.data['intro_msg'])
            
    
    def tearDown(self):
        self.app = None

    def test_app_name(self):
        self.assertEqual(self.app.app_name, self.data['name'])

    def test_app_prompt(self):
        self.assertEqual(self.app.prompt, self.data['prompt'])

    @unittest.skip('skip intro_msg checking')
    def test_intro_msg(self):
        self.assertEqual(self.app.welcome_msg, self.data['intro_msg'])
    
    def test_exit_msg(self):
        self.assertEqual(self.app.exit_msg, self.data['exit_msg'])


if __name__ == '__main__':
    unittest.main()
