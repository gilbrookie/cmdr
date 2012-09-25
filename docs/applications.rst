
=======================
Creating an Application
=======================

To create your own command line interpreter, you need to create an application, by creating a
:class:`Cmdr` object.  The :class:`Cmdr` class provides all the necessary functionality to run,
all it needs is  a set of commands to run (See Registering commands).

:class:`Cmdr` takes only a name argument to create an application.::

    # test.py
    import cmdr
    app = cmdr.Cmdr("TestApp")
    ...

The *name* argument can be any string. This name is used to provide a nice welcome message for you
when the application is started.

Registering Commands
--------------------

:class:`Cmdr` provides two methods for registering commands with a application.

* *Register_cmd(cmd)* method
* *@cmd* decorator

Builtin Commands
-----------------
All applications come builtin with a help and an exit command.

* *help/?* will print out the available commands and their help strings
* *exit/q* will stop the interpreter from executing and exit.


Customizing the your App
------------------------

The following can be modified using the optional paramters in :class:`Cmdr`:

* Welcome Message - The string shown when the application starts.
* Exit Message - The string shown as the application closes.
* Prompt - you can change the defautl "->" prompt string.

::

    c = Cmdr("TestApp",
             intro_msg="TestApp - just what you always wanted",
             exit_msg="See ya!"
             prompt="=>")



