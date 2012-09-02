# -*- coding: utf-8 -*-

"""
aclip2.application
~~~~~~~~~~~~~~~~~~

This module implements the main Application class and supported functions.
"""

from pprint import pprint as pp
import readline
import logging

from aclip2 import Command

logging.basicConfig(filename='/tmp/aclip2.log', level=logging.DEBUG, 
                    format='%(asctime)s [%(levelname)s] %(module)s - %(message)s')

class Application(object):
    """
    The Application object implements the main CLI interpreter and acts as the
    primary entry point for applications.

    It is passed the name of the application as it's only required argument.
    Optionally, a list of Command objects may be passed in, as well you can override
    the intro and exit messages.

    The Application class keeps track of the available commands through a
    registration system.  Users of the Application class can provide the commands at
    creation time or using the :meth:`register_cmd` method to register and make
    custom command available in the application.

    The Application provides two built-in commands; exit and help.

    For the commands that are registered, the application will try to provide basic
    tab completion and maintains a history of previously entered commands.

    :param: app_name: the name of the application
    :param: registered_commands: can be used to set the list of registered commands
                                 as creation time.  Defaults to None.
    :param: intro_msg: the introduction message printed by the Application class
    :param: exit_msg: the exit message printed by the Application class when the it
                        is terminated.


    """
    
    DEFAULT_WELCOME = u"""\nACLIP2 Command line framework\nLet's get started!\n"""
    DEFAULT_EXIT = u"""\nBye!"""

    def __init__(self, app_name, registered_commands=None, intro_msg=None,
            exit_msg=None, prompt_str=None):
        
        self.logger = logging.getLogger(self.__class__.__name__)
        # The default prompt string
        self.prompt = "-> "
        if prompt_str:
            self.prompt= prompt_str

        self.app_name = app_name

        if registered_commands:
            for cmd in registered_commands:
                self.register_cmd(cmd)
        else:
            self.registered_cmds = []

        self.complete_dict = {}
        self.exit_condition = False

        if not intro_msg:
            self.welcome_msg = self.DEFAULT_WELCOME

        if not exit_msg:
            self.exit_msg = self.DEFAULT_EXIT
        
        self.current_candidates = []


    def start(self):
        """Instructs the Application class to start the command line interreter.  All
        commands must be registered with the application prior to calling start."""
        
        
        # Show the welcome message up front.        
        print self.welcome_msg
       
        # set up the command completion code - so we can do "TAB" completion.
        self.rl_completer = readline.get_completer()

        # Configure the function that perform the command lookup (thus completion)
        readline.set_completer(self._complete_cmd)
        readline.parse_and_bind("tab: complete")


        # The main loop uses an flag to determine when it needs to exit. 
        # Run until the flag is set.

        while not self.exit_condition:
            #pp(self.complete_dict)
            
            try:              
                # read in the text input from cli
                cmd = raw_input(self.prompt)

                # then, execute
                self._exec_cmd(cmd)
                               
            # Catch keyboard shortcuts to kill the app (CTRL+C, CRTL+Z)
            except (KeyboardInterrupt, EOFError):
                self.exit_condition = True

            # Catch cases where an invalid command was entered
            except CommandNotFound, ex:
                print ex

            # Some debugging exceptions (TODO: Remove once intial dev work complete)
            except TypeError, ex:
                print "TypeError:%s" % ex

            # blanket execption catch-all - so we can print an approptiate message
            # without killing the running process.
            except Exception, ex:
                print "CAUGHT: %s" % ex

        # restore the previous completer function when we're done.
        readline.set_completer(self.rl_completer)

        # Show the exit message
        print self.exit_msg

    def _exec_cmd(self, cmd):
        print cmd

        cmdparts = cmd.split()
        for c in self.registered_cmds:
            if cmd in c.cmd_strs:
                print c
                c.execute(cmd)
                break
        else:
            raise CommandNotFound("Command not found: %s" % cmd)

    def register_cmd(self, cmd):
        """
        This method registers the provided command with the Application.  The command
        must be an instance if the Command class to be valid.
        """
        # Check if cmd has actually a Command Class
        if isinstance(cmd, Command):

            self.registered_cmds.append(cmd)
            self.complete_dict[cmd.cmd] = [c for c in cmd.subcmds]

        else:
            print "expecting a Command object"


    def cmd(self, cmd_name, alt=None):
        """A function decorator that registers the function as a command within
        the application.
        
        :param cmd_name: the name of the command (it is how the command will appear
                         within the application
        :param alt: an alternate name for the command - usually a shortcut that the
                    application can register.

        *Usage:*

        # Instantiate an app
        app = aclip2.Application(__name__)

        # register a command using the decorator
        @app.cmd(echo):
        def echo(msg):
            print msg

        # start the app
        app.start()

        ->echo Hello World!
        Hello World!

        """

        def decorator(f):
            self.logger.info("Registering new command '%s', func=%s" % (cmd_name, f))
            # Create a new Command object and register it.
            c = Command(cmd=cmd_name, description=f.__doc__, exec_func=f)
            self.register_cmd(c)
            if alt:
                # Create a separate Command for the alternate.
                a = Command(cmd=alt, description=f.__doc__, exec_func=f)
                self.register_cmd(a)

        return decorator

    def _show_cmds(self):
        for cmd in self.registered_cmds:
            print cmd['name']

    def _complete_cmd(self, text, state):
        self.logger.debug('STATE=%s', state)

        origline = readline.get_line_buffer()
        begin = readline.get_begidx()
        end = readline.get_endidx()
        being_completed = origline[begin:end]
        words = origline.split()

        self.logger.debug('origline=%s', repr(origline))
        self.logger.debug('begin=%s', begin)
        self.logger.debug('end=%s', end)
        self.logger.debug('being_completed=%s', being_completed)
        self.logger.debug('words=%s', words)

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

                    self.logger.debug('candidates=%s', self.current_candidates)
                    
                except (KeyError, IndexError), err:
                    self.logger.error('completion error: %s', err)
                    self.current_candidates = []
        
        try:
            response = self.current_candidates[state]
        except IndexError, e:
            response = None
        self.logger.debug('complete(%s, %s) => %s', repr(text), state, response)
        return response



class CommandNotFound(Exception):
    """Raised when an unregistered command is entered"""
    pass

class InvalidCommandType(Exception):
    """Raised when attempting to register a command that is not an instance of the
    Command class."""
    pass
