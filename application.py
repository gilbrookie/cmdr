import inspect
from pprint import pprint as pp
import readline

DEFAULT_WELCOME = u"""\nACLIP2 Command line framework\nLet's get started!\n"""
DEFAULT_EXIT = u"""\nBye!"""

class Application(object):
    def __init__(self, app_name, registered_commands=None, intro_msg=None, exit_msg=None):
        self.prompt = "-> "
        self.app_name = app_name

        if registered_commands:
            self.registered_cmds = registered_commands
        else:
            self.registered_cmds = []

        self.exit_condition = False

        if not intro_msg:
            self.welcome_msg = DEFAULT_WELCOME

        if not exit_msg:
            self.exit_msg = DEFAULT_EXIT
        
            
    def start(self):
        """Runs the command loop"""
        # Show prompts,wait for input
        # Validate command
        # loop until termination command issued (exit, CTRL+C)
        print self.welcome_msg
        while not self.exit_condition:
            pp(self.registered_cmds)
            try:
                cmd = raw_input(self.prompt)
                self.exec_cmd(cmd)
                                
            except (KeyboardInterrupt, EOFError):
                self.exit_condition = True

            except CommandNotFound, ex:
                print ex

            except TypeError, ex:
                print ex

        print self.exit_msg

    def exec_cmd(self, cmd):
        for c in self.registered_cmds:
            if c['name'] == cmd:
                c['exec_func']()
                break
        else:
            raise CommandNotFound("Command not found: %s" % cmd)


    def register_cmd(self, **options):
        cmd_name = options.get('name')
        exec_func = options.get('exec_func')
        help = options.get('help')
        argspec = options.get('argspec')

        readline.parse_and_bind("tab: complete")
        self.registered_cmds.append(options)
    
    def cmd(self, cmd_name):
        print "Decorator called"
        def decorator(f):
            self.register_cmd(name=cmd_name,
                                help=f.__doc__,
                                exec_func=f, )
                                #argspec=inspect.getargspec(f))
        return decorator

    def show_cmds(self):
        for cmd in self.registered_cmds:
            print cmd['name']
        
   
class CommandNotFound(Exception):
    pass
