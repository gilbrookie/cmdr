# -*- coding: utf-8 -*-

"""
cmdr.command
~~~~~~~~~~~~~~

This module implements the base Command class.  This class defines the
functionality required the register commands with the Application and allow
them to be executed.
"""
import logging


class CmdMetaclass(type):
    def __new__(cls, name, bases, attrs):

        # Create an new super class
        new_cls = super(CmdMetaclass, cls).__new__(cls, name, bases, attrs)

        # a dict to track sub cmds
        subcmds = {}

        # Iterate through the attrs, looking specifically for methods that have
        # the "is_subcmd" attribute.   This attribute is not default, it is
        # added with the @subcmd decorator.

        for key in attrs:
            attr = getattr(new_cls, key)
            try:
                if hasattr(attr, "is_subcmd"):
                    subcmds[key] = {'help': attr.__doc__, 'exec_func': attr}

            except AttributeError:
                continue

        # Once we have found any/all subcmds, add them as a class attibute
        setattr(new_cls, "subcmds", subcmds)
        # return the new class
        return new_cls


class Command(object):
    """
    The Command class defines the interface required to be registered with the
    Application class. The command class may be used in a few different ways, but
    all have the same end effect/goal.

    Command takes no arguments to create, but many optional arguments are available
    to customize the class at creation time.

    The two main use cases are direct instantiation or subclassing.  Both are valid
    and and their use may depend on the needs of the object.

    Method 1: Direct
    ----------------
    ::
        from cmdr import Command

        def callback(arg):
            print arg

        c = Command(cmd="echo", exec_func=callback)


    Method 2: Subclass
    ------------------
    ::

        from cmdr import Command

        class Echo(Command):

            def execute(self, args):
                print args

    """

    __metaclass__ = CmdMetaclass

    def __init__(self, cmd=None, alt=None, sub_cmd_set=None, description=None,
                 exec_func=None, arg_spec=None):

        self.logger = logging.getLogger(self.__class__.__name__)

        self.subcmds = {}
        
        # In cases where Commands are created directly (cmdr.cmd generator, or
        # user generated, we need to check if a command string is actually two 
        # commands.

        # if the cmd can be split into two or more words (has a space in it) we 
        # take the first part as the primary command and the second part as a 
        # subcommand. In this case the primary command's exec_func needs to be 
        # the default execute(), and the exec_func assigned to the subcmd.

        # **NOTE: currently only supports one level of sub command
        if cmd:
            parts = cmd.split()
            
            self.exec_func = exec_func if exec_func else self.execute

            # We have a subcmd
            if len(parts) > 1:
                # figure out how to assign the execution function
                if exec_func:
                    self.sub_exec = exec_func
                    self.exec_func = self.execute
                else:
                    self.exec_func = self.sub_exec = self.execute
                        
                # assign accordingly
                self.name = parts[0]
                self.subcmds[parts[1]] = {'help': description,
                                          'exec_func': self.sub_exec}
            # Single command
            else:
                self.name = cmd
        else:
            self.name = self.__class__.__name__.lower()
            self.exec_func = self.execute
            if exec_func:
                self.exec_func = exec_func

        self.description = description
        if not description:
            self.description = self.__doc__ 

        self.alt = alt
        self.completion_dict = None

    @property
    def cmd_dict(self):
        """Returns a dictionary representation of the command"""
        return {self.name: {'help': self.description,
                            'alt': self.alt,
                            'exec_func': self.exec_func,
                            'comp_dict': self.completion_dict,
                            'subcmds': self.subcmds}}

    @property
    def cmd_strs(self):
        """Returns a list of complete commands (including subcommands)"""
        if not self.subcmds:
            return [self.name]

        else:
            return [" ".join([self.name, sc]) for sc in self.subcmds.keys()]

    def execute(self, cmd, args=None):
        """This method implements the functionality of the command.  When an
        Application calls to execute any command this method is called (by default).

        Execution code can be overriden with a callback method when the Command is
        created.

        When execute is called, it is given the full command (incl subcmds) as well
        as the provided arguments.  It is up to the execution method to ensure 
        that the arguments are correct.

        """
        self.logger.info("'%s' execute()" % self.name)

        #print "No action to perform for %s" % cmd
        print "No action to perform"


def subcmd(f):
    """subcmd Decorator - used in combination with a subclassed Command class to
    enable its methods that act as sub-commands.  These subcommand methods get
    auto-registered with an Application when the main command is registered.

    When a command is executed, the default execute method will automatically
    call the method defined by the decorator for the provided command.
    """

    # All this decorator does is set a function (method to be specific) attribute
    # "is_subcmd" so that the Command class's metaclass can find them and configure
    # the method as sub commands.

    f.is_subcmd = True
    return f
