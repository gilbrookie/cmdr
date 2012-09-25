Creating Commands
==================

There are three ways to develop commands for a Cmdr application.

#. @cmd decorator
#. Subclassing Command
#. Direct instances of Command

Method 1: Using the @cmd decorator - Simple and Easy
----------------------------------------------------

::

    # Using function Decorator
    @app.cmd()
    def echo3(*args):
        """This docstring will appear as help for the echo cmd"""
        print "echo3 %s" % " ".join(args)

Using the @cmd decorator is the easiest way to create and register commands.

To use the decorator, you first need an instance of Cmdr as the decorator is just a method.
Without any arguments provided, the decorator registers a command with the name of the decorated
function (lowercased). The function's docstring is used as it's help string.

You can provide a *name* argument that will register a command of that name.

The decorated function is called when the command is ready to execute.

Method 2: Subclassing Command - For greater control/flexibility
---------------------------------------------------------------
::

    # Subclass
    class Echo2(Command):
        """This docstring will show up as "help echo2" in the application"""

        def execute(self, *args):
            """This method will perform the echo functionality"""
            print "echo2 %s" % " ".join(args)


The base Command class provides the necessary interface that Cmdr needs to identify and execute a
command.  Some features of the :class:`Command` class.

* The class name automatically becomes the command string (inside the Cmdr instance)
* The class's docstring will appear in the help command of Cmdr instance
* The :meth:`execute` method is called when the command is striggered to run from Cmdr.  Overriding
this method will ensure that the desired code is executed.

The :meth:`execute` can take 0 or more arguments - It's up to you!

Subclassing the command class also allows you to create subcommands for greater flexibility and
better code organization.

Method 3: Creating a Command object with some arguments
-------------------------------------------------------
::

    def echo1(*args):
        print args

    # Build a command directly
    cmd = Command(name="echo1", desc="Sample", exec_func=echo1)

When creating a Command class directly, you need to provide some of the optional arguments to ensure
that Cmdr can identify and execute it.  At minimum, you need to include the :attr:`name` and :attr:`exec_func` arguments.


Creating commands with sub-commands
===================================

In cases where more than just single commands are required, the Command class provides two ways to
create sub-commands - which are just a way separate command execution under a common functional
area name.

For example, you have a Cmdr app that allow backend access to a database.  You may want commands
that perform different actions on a particular set of data.

Using decorated functions, it may look like this::

    app = Cmdr('Single cmd')

    @app.cmd('db create')
    def db_create():
        ...

    @app.cmd('db select')
    def db_select(args):
        ...

    @app.cmd('db insert')
    def db_insert(keys, values):
        ...

Using subcomands::

    class db(Command):
        def __init__(self):
            super(db, self).__init__()
            # Add any common data/setup values

        @subcmd()
        def create(self, args):
            ...

        @subcmd
        def insert(self, keys, values):
            ...

        @subcmd
        def select(self, args):
            ...

Both methods are functionally equivalent, usage may depend only on preference.
