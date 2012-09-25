.. cmdr documentation master file, created by
   sphinx-quickstart on Sat Sep  8 16:00:30 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to cmdr's documentation!
================================

:mod:`cmdr` is a simple to use API for creating command line application with custom commands. The goal is be flexible and require as little code as possible to get up and running.

Installing cmdr
===============
To get :mod:`cmdr` (on linux), clone the source in a local directory::

    git clone https://github.com/jamesgilbrook/cmdr

Then, use the :mod:`setup.py` script to install it::

    python setup.py install

TODO: Add to pypi and provide instructions here.

Getting Started
===============
Here is a simple example to get yoru started:

::

    from cmdr import Cmdr

    # Create an application (give it the name of the current module)
    app = Cmdr("TestApp"):

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

#. Creating an app (instantiate a :class:`Cmdr` class)
#. Defining and registering a command with your app
#. Starting the command interpreter (using :meth:`Cmdr.start()`)


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


.. toctree::
   :maxdepth: 2
    
   applications.rst
   commands.rst
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

