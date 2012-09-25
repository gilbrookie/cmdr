cmdr - A line based command interpreter framework/tool
======================================================
.. image:: https://secure.travis-ci.org/jamesgilbrook/cmdr.png?branch=develop
    :target: http://travis-ci.org/#!/jamesgilbrook/cmdr

.. contents::

What is it?
-----------
A simple to use API for creating line-based command interpreter applications that include custom commands.

**cmdr** is very similar to the `cmd <http://docs.python.org/library/cmd.html>`_ module.

The goal with **cmdr** is flexibility and require as little code as possible to get up and running.

Motivation
----------
I was working on a web application using Flask and I really like how Flask uses decorators to define
simple views. It was really easy to get something up and running.
At the same time I was building a simple cli tool that could access backend of the web application,
I thought it would be interesting to try and apply a similar design to how I built the command list.

Installing cmdr
===============

Clone the source to a local directory::

    git clone https://github.com/jamesgilbrook/cmdr

Then use the setup.py file to install it::

    python setup.py install

**TODO**
Add to pypi.

Getting Started!
================

Here is a simple example to get you started:::

    from cmdr import Cmdr

    # Create an application (give it the name of the current module)
    app = Cmdr("TestApp"):

    # Define simple command using a decorator, the argument passed in is the name of the command
    @app.cmd("hello")
    def say_hello():
        print "Hello!"

    # Start the interpreter loop
    app.start()

    # Save the content in app.py and run it from your command line
    # On launch, you'll get a prompt and when you enter "hello" the say_hello() function is called.

    $ python app.py

    Welcome to TestApp - Let's get started

    ->hello
    Hello!
    ->exit
    bye!


In this example, you have the three main interfaces of cmdr

#. Creating an app (instantiate a *Cmdr* class)
#. Defining and registering a command with your app
#. Starting the command interpreter (using *Cmdr.start()*)

Documentation
==================
Additional documentation is included with the source code, and can be built and viewed with a simple make command::

    make docs

This will build the documentation as HTML locally and open a web browser to the home
page.

History
=======

cmdr is still in development and rapidly nearing it's first release.

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


Issues/Feature Requests
=======================

All `issues/features <https://github.com/jamesgilbrook/cmdr/issues>`_ are being tracked in github
