# -*- coding: utf-8 -*-

"""
cmdr.application
~~~~~~~~~~~~~~~~~~

This module implements the main Cmdr class and supported functions.
"""

import readline
import logging
import sys

from cmdr import Command
from cmdr.state import StateController

logging.basicConfig(filename='/tmp/cmdr.log', level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(module)s - %(message)s')


class Cmdr(object):
    """
    The Cmdr object implements the main CLI interpreter and acts as the
    primary entry point for applications.

    It is passed the name of the application as it's only required argument.
    Optionally, a list of Command objects may be passed in, as well parameters that
    can override the prompt, intro and exit messages.

    The Cmdr class keeps track of the available commands through a
    registration system.  Users of the Cmdr class can provide the commands at
    creation time or using the :meth:`register_cmd` method to register and make
    custom command available in the application.

    The Cmdr provides two built-in commands; exit and help.

    For the commands that are registered, the application will try to provide basic
    tab completion and maintains a history of previously entered commands for the
    current session.

    :param app_name: the name of the application
    :param registered_commands: can be used to set the list of registered commands
                                 as creation time.  Defaults to None.
    :param intro_msg: the introduction message printed by the Cmdr class
    :param exit_msg: the exit message printed by the Cmdr class when the it
                        is terminated.
    :param prompt_str: the characters used for the prompt

    """

    DEFAULT_WELCOME = "\nWelcome to %s - Let's get started!\n"
    DEFAULT_EXIT = "\nBye!"
    DEFAULT_PROMPT = "->"

    def __init__(self, app_name, registered_commands=None, intro_msg=None,
                 exit_msg=None, prompt_str=None):

        self.logger = logging.getLogger(self.__class__.__name__)
        # The default prompt string
        self.prompt = self.DEFAULT_PROMPT
        if prompt_str:
            self.prompt = prompt_str

        self.app_name = app_name

        # data stored for the registered commands
        self.complete_dict = {}
        self.registered_cmds = []

        # a list used for code completion
        self.current_candidates = []

        # flag used to trigger the application to close
        self.exit_condition = False

        # Add the default registered commands (help, exit)
        self.builtin_cmds = [
            Command(cmd='help', description="Shows this menu",
                    exec_func=self._show_cmds),
            Command(cmd='exit', description="Exits the app",
                    exec_func=self.exit)]

        for cmd in self.builtin_cmds:
            self.register_cmd(cmd)

        if registered_commands:
            # we need to process each command through the registration function
            for cmd in registered_commands:
                self.register_cmd(cmd)

        self.welcome_msg = self.DEFAULT_WELCOME % self.app_name
        if intro_msg:
            self.welcome_msg = intro_msg

        self.exit_msg = self.DEFAULT_EXIT
        if exit_msg:
            self.exit_msg = exit_msg
    
        # Create an instance of the StateController
        self.app_state = StateController("Cmdr")

    def start(self):
        """Instructs the Cmdr class to start the command line interreter.  All
        commands must be registered with the application prior to calling start."""

        # Show the welcome message up front.
        sys.stdout.write(self.welcome_msg)
        sys.stdout.write("\n")

        # make backup of the current completer function
        self.rl_completer = readline.get_completer()

        # set up the command completion code - so we can do "TAB" completion.
        # Configure the function that performs the command lookup and completion
        readline.set_completer(self._complete_cmd)
        readline.parse_and_bind("tab: complete")

        # The main loop uses a flag to determine when it needs to exit.
        # Run until the flag is set.
        while not self.exit_condition:

            try:
                # read in the text input from cli
                cmd = raw_input(self.prompt)

                # Check for specific builtin shortcuts
                if cmd == "?":
                    self._show_cmds()
                elif cmd == "q":
                    self.exit_condition = True
                elif cmd == "":
                    continue
                else:
                    # then, execute
                    self._exec_cmd(cmd)

            # Catch keyboard shortcuts to kill the app (CTRL+C, CRTL+Z)
            except (KeyboardInterrupt, EOFError):
                self.exit_condition = True

            # Catch cases where an invalid command was entered
            except CommandNotFound as ex:
                sys.stderr.write(str(ex))
                sys.stderr.write("\n")
            # Some debugging exceptions (TODO: Remove once intial dev work complete)
            except TypeError as ex:
                sys.stderr.write(str(ex))
                sys.stderr.write("\n")

            # blanket execption catch-all - so we can print an approptiate message
            # without killing the running process.
            #except Exception, ex:
            #    print "CAUGHT: %s" % ex

        # restore the previous completer function when we're done.
        readline.set_completer(self.rl_completer)

        # Show the exit message
        sys.stdout.write(self.exit_msg)
        sys.stdout.write("\n")

    def _exec_cmd(self, cmd):
        (fn, args) = self._lookup_cmd(cmd.split())
        if fn:
            if args:
                fn(args)
            else:
                fn()
        else:
            raise CommandNotFound("Command not found: %s" % cmd)

    def _lookup_cmd(self, key_list):

        # track the function to be executed
        ex_fn = None
        args = None

        for cmd in self.registered_cmds:
            # lookup the primary command name
            if key_list[0] == cmd.name:

                key_list.pop(0)
                try:
                    # if we match, try to match subcmds
                    if key_list[0] in cmd.subcmds:
                        # we found a subcmd
                        subcmd = key_list.pop(0)
                        meth = cmd.subcmds[subcmd]['exec_func']

                        # if we have a subcmd, we need to get the method from
                        # the instance stored in the command list
                        ex_fn = getattr(cmd, meth.func_name)
                        args = key_list

                    else:
                        ex_fn = cmd.exec_func
                        args = key_list

                except IndexError:
                    # if no match is found
                    ex_fn = cmd.exec_func

                break

            else:
                continue

        return (ex_fn, args)

    def register_cmd(self, cmd):
        """
        This method registers the provided command with the Cmdr.  The command
        must be an instance if the Command class to be valid.
        """
        # Check if cmd has actually a Command Class
        if isinstance(cmd, Command):
            # populate the statecontroller for the command 
            cmd.app_state = StateController(cmd.name)
            self.registered_cmds.append(cmd)
            self.complete_dict[cmd.name] = [c for c in cmd.subcmds]
        else:
            raise InvalidCommandType("Expecting type cmdr.Command")

    def cmd(self, name=None, alt=None):
        """A function decorator that registers the function as a command within
        the application.

        :param name: the name of the command (it is how the command will appear
                         within the application
        :param alt: an alternate name for the command - usually a shortcut that the
                    application can register.

        *Usage:*

        # Instantiate an app
        app = cmdr.Cmdr("TestApp")

        # register a command using the function decorator
        @app.cmd('echo'):
        def echo(msg):
            print msg

        # start the app
        app.start()

        The command is automatically registered with app using the decorator
        ->echo Hello World!
        Hello World!

        """

        def decorator(f):
            # If no name is provided, use the decorated function name (lowercase)
            if not name:
                cmd_name = f.func_name.lower()
            else:
                cmd_name = name

            self.logger.info("Registering new command '%s', func=%s" %
                             (cmd_name, f))
            # If the function does not have a docstring, override the __doc__ to
            # ensure that the Command base class's docstring is not shown.
            if not f.__doc__:
                f.__doc__ = " "

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
            sys.stdout.write("\t%s\t\t%s" % (cmd.name, cmd.description))
            sys.stdout.write("\n")

    def exit(self):
        self.exit_condition = True

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
                        self.current_candidates = \
                            [w for w in candidates
                             if w.startswith(being_completed)]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                    self.logger.debug('candidates=%s', self.current_candidates)

                except (KeyError, IndexError) as err:
                    self.logger.error('completion error: %s', err)
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
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
