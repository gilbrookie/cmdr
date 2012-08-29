import inspect
from pprint import pprint as pp
import readline
import logging
from aclip2 import command

logging.basicConfig(filename='/tmp/aclip2.log', level=logging.DEBUG)

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

        self.complete_dict = {}
        self.exit_condition = False

        if not intro_msg:
            self.welcome_msg = DEFAULT_WELCOME

        if not exit_msg:
            self.exit_msg = DEFAULT_EXIT
        
        self.current_candidates = []


    def start(self):
        """Runs the command loop"""
        # Show prompts,wait for input
        # Validate command
        # loop until termination command issued (exit, CTRL+C)
        print self.welcome_msg

        self.rl_completer = readline.get_completer()
        readline.set_completer(self.complete_cmd)
        readline.parse_and_bind("tab: complete")

        while not self.exit_condition:
            pp(self.complete_dict)
            try:
                cmd = raw_input(self.prompt)
                self.exec_cmd(cmd)
                                
            except (KeyboardInterrupt, EOFError):
                self.exit_condition = True

            except CommandNotFound, ex:
                print ex

            except TypeError, ex:
                print "TypeError:%s" % ex

            except Exception, ex:
                print "CAUGHT: %s" % ex

        readline.set_completer(self.rl_completer)

        print self.exit_msg

    def exec_cmd(self, cmd):
        print cmd

        cmdparts = cmd.split()
        for c in self.registered_cmds:
            if cmd in c.cmd_strs:
                print c
                c.execute(cmd)
                break
        else:
            raise CommandNotFound("Command not found: %s" % cmd)


    def register_cmd(self, **options):
        """
        cmd_name = options.get('name')
        exec_func = options.get('exec_func')
        help = options.get('help')
        argspec = options.get('argspec')
        """

        self.registered_cmds.append(options)

    def register_cmd2(self, cmd):


        print type(cmd)
        # Check if cmd has actually a Command Class
        if isinstance(cmd, command.Command):
            # if not already instatiated, do that.

            self.registered_cmds.append(cmd)
            
            self.complete_dict[cmd.cmd] = [c for c in cmd.subcmds]

        else:
            print "expecting a Command object"


    def cmd(self, cmd_name, alt=None):
        print "Decorator called"
        def decorator(f):
            self.register_cmd(name=cmd_name, help=f.__doc__, exec_func=f, )
            if alt:
                self.register_cmd(name=alt, help=f.__doc__, exec_func=f)
        return decorator

    def show_cmds(self):
        for cmd in self.registered_cmds:
            print cmd['name']

    def complete_cmd(self, text, state):
        logging.debug('STATE=%s', state)

        origline = readline.get_line_buffer()
        begin = readline.get_begidx()
        end = readline.get_endidx()
        being_completed = origline[begin:end]
        words = origline.split()

        logging.debug('origline=%s', repr(origline))
        logging.debug('begin=%s', begin)
        logging.debug('end=%s', end)
        logging.debug('being_completed=%s', being_completed)
        logging.debug('words=%s', words)

        if state == 0:

            if not words:
                self.current_candidates = sorted(self.complete_dict.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.complete_dict.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.complete_dict[first]
                    
                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [ w for w in candidates
                                                    if w.startswith(being_completed) ]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    logging.debug('candidates=%s', self.current_candidates)
                    
                except (KeyError, IndexError), err:
                    logging.error('completion error: %s', err)
                    self.current_candidates = []
        
        try:
            response = self.current_candidates[state]
        except IndexError, e:
            response = None
        logging.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response
"""
registered_cmds


{cmd: { help:"",
        alt:"",
        subcmds:[],
        validate_func:
        exec_func:
        completion_dict:{}
        }
}

        



complete_dict = {key1:[{subkey1, args},
                       {subkey2, args}],
                 key2:[subkey1,
                       subkey2]...}

"""

class CommandNotFound(Exception):
    pass
