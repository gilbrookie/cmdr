aclip2 - Another Command Line Interface Processor written in Python
===================================================================

Seriously, isn't this what the world needs, another CLI processor in python?
I get it, I know.  I just wanted to try my hand at writing one myself - deal with it.

What is it?
-----------
A simple to use API for creating a command line application with custom commands.

Motivation
----------
I was working on a web application using Flask and I really like how Flask uses decorators to define
simple views.  When I wanted to build a cli backend of the web application, I thought it would be
interesting to try and apply a similar design to how I built the command list.



Usage
=====

Designing Commands
------------------
:: 

    def echo1(*args):
        print args

    # Build a command directly
    cmd = Command(name="echo1", desc="Sample", exec_func=echo1)

::

    # Subclass
    class Echo2(Command):
        """This docstring will show up as "help echo2" in the application"""

        def execute(self, *args):
            """This method will perform the echo functionality"""
            print "echo2 %s" % " ".join(args)

::

    # Using function Decorator 
    @aclip.cmd
    def echo3(*args):
        """This docstring will appear as help for the echo cmd"""
        print "echo3 %s" % " ".join(args)

Building the CLI application
-----------------------------
::

    # Instatiate an Application object, use the module __name__ to set the name of the app
    app = aclip2.Application(__name__)
    
    # Pass in a command that are available
    app.register_cmd(cmd)
    app.register_cmd(Echo2())
    
    # Start the app
    app.start()

A simple example of the app running:

::
    
    ACLIP2 Command Line Framework
    Let's get started
    
    -> echo1 Test echo1
    echo1 Test echo1
    -> echo2 abc def
    echo2 abc def
    ->help echo2
    This docstring will show up as "help echo2" in the application
    ->exit
    Bye!



Roadmap/Status
==============

I am nearing my goal of being feature complete for rev1 release:
Below are the features that will (need to) make it in (priority order)

Application object:

#. Run primary interpreter loop **Done**
#. Provide a registration interface for commands **Done**.
#. Provide tab completion support **Done**
#. Expose builtin commands for "help" and "exit", implement each builtin.

Command object:

#. Define (finalize) the data needed by all commands (Application needs these details) **Done**
#. Define the methods required by all commands **Done**
#. Allow methods to be used as sub commands **Done**
#. Helper properties (used by Application for tab completion and easy command lookup) **Done**

Misc project requirements

#. Docstrings for all public classes/functions/methods/data **Done**
#. Passes pep8 and pyflakes **Done**
#. Must execute on Python 2.6 and python 2.7 **In progress**
#. Basic level of documentation
#. Basic level of unittests **In progress**
#. finalize package name  (aclip2 isn't great)
#. need setup.py and Makefile (for basic testing/docs/setup)

Post rev1 feature ideas (in no order)
-------------------------------------
* Add support for terminal colors
* Improve argument parsing (I have some ideas, but nothing has been vetted)
* Allow support for arbitrary level of command depth
* Support sub command prompts (to expose levels of subcommands)
* Execute in thread
* Progess bar (maybe useful for long running commands)
* Unicode support

Name Ideas
==========

Seriously, I need a new name.

What am I really? A line based command interpreter tool/framework/api.  Kind of Like the Cmd module, but
better/more flexible/more modern?  (hint: I'm not a fan of do_* style class methods)

Uses:
- quickly prototyping a projects
- Provide command line (admin) tools for web applications, or any app with a db backend. 
- To create test harnesses

Other packages provide extensions to Cmd, but I was to provide a new way to create
custom commands.  I want it to be easy and flexible (more than one way to do it) with little code
required to get started.

Ideas:

PyInterpret
PyCmd2
CoCmd
Cmdpy
subcmdr (subcmd is taken by a very similar application)

**cmdr** or **cmdrunner*





