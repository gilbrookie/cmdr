cmdr - A line based command interpreter framework/tool
======================================================
.. image:: https://secure.travis-ci.org/jamesgilbrook/cmdr.png?branch=develop
    :target: http://travis-ci.org/#!/jamesgilbrook/cmdr


What is it?
-----------
A simple to use API for creating command line application with custom commands.  The goal is be
flexible and require as little code as possible to get up and running.

Motivation
----------
I was working on a web application using Flask and I really like how Flask uses decorators to define
simple views. It was really easy to get something up and running.  
When I wanted to build a cli backend of the web application, I thought it would be
interesting to try and apply a similar design to how I built the command list.

Installing cmdr
===============

Clone the source to a local directory

::

    git clone https://github.com/jamesgilbrook/cmdr

Then use the setup.py file to install it

::

    python setup.py install

**TODO** 
Add to pypi.

Getting Started!
================

Here is a simple example to get yoru started:

::

    from cmdr import Cmdr

    # Create an application (give it the name of the current module)
    app = Cmdr(__name__):

    # Define simple command using a decorator, the argument passed in is the name of the command
    @app.cmd("hello")
    def say_hello():
        print "Hello!"

    # Start the interpreter loop
    app.start()

    # you'll get a prompt, and when you enter "hello" the say_hello() function is called.
    ...
    >hello
    Hello!
    ...
    
In this example, you have the three main interfaces of cmdr

#. Creating an app (instantiate a *Cmdr* class)
#. Defining and registering a command with your app
#. Starting the command interpreter (using *Cmdr.start()*)


Advanced Usage
==============

Designing Commands
------------------

There are three ways to develop commands for the cmdr application

Method 1: Creating a Command object with some arguments
-------------------------------------------------------
:: 

    def echo1(*args):
        print args

    # Build a command directly
    cmd = Command(name="echo1", desc="Sample", exec_func=echo1)

Method 2: Subclassing Command - For greater control/flexibility
---------------------------------------------------------------
::

    # Subclass
    class Echo2(Command):
        """This docstring will show up as "help echo2" in the application"""

        def execute(self, *args):
            """This method will perform the echo functionality"""
            print "echo2 %s" % " ".join(args)


Method 3: Using the cmd decorator
---------------------------------
::

    # Using function Decorator 
    @app.cmd
    def echo3(*args):
        """This docstring will appear as help for the echo cmd"""
        print "echo3 %s" % " ".join(args)

Building the CLI application
============================
::

    # Instatiate an Cmdr object, use the module __name__ to set the name of the app
    app = cmdr.Cmdr(__name__)
    
    # Pass in a command that are available
    app.register_cmd(cmd)
    app.register_cmd(Echo2())
    
    # Start the app
    app.start()

A simple example of the app running:

::
    
    cmdr Command Line Framework
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

Cmdr object:  **COMPLETE**

#. Run primary interpreter loop **Done**
#. Provide a registration interface for commands **Done**.
#. Provide tab completion support **Done**
#. Expose builtin commands for "help" and "exit", implement each builtin. **Done**

Command object:  **COMPLETE**

#. Define (finalize) the data needed by all commands (Cmdr needs these details) **Done**
#. Define the methods required by all commands **Done**
#. Allow methods to be used as sub commands **Done**
#. Helper properties (used by Cmdr for tab completion and easy command lookup) **Done**

Misc project requirements  **IN PROGRESS**

#. Docstrings for all public classes/functions/methods/data **Done**
#. Passes pep8 and pyflakes **Done**
#. Must execute on Python 2.6 and python 2.7 **In progress**
#. Basic level of documentation
#. Basic level of unittests **Done**
#. finalize package name  (cmdr has been chosenas package name!) **Done**
#. need setup.py and Makefile (for basic testing/docs/setup) **Done**
#. register and publish to pypi


**Target rev1 version is 0.1. ETA: Oct 2012**


Post rev1 feature ideas (in no order)
-------------------------------------
* Add support for terminal colors
* Improve argument parsing (I have some ideas, but nothing has been vetted)
* Allow support for arbitrary level of command depth
* Support sub command prompts (to expose levels of subcommands)
* Execute in thread
* Progess bar (maybe useful for long running commands)
* Unicode support
* Add subcmds as argument to Command. Are subcmds Command objects or dict?


