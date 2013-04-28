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

0.1 - initial release (Oct 2012) 

Issues/Feature Requests
=======================

All `issues/features <https://github.com/jamesgilbrook/cmdr/issues>`_ are being tracked in github
