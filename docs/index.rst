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

.. toctree::
   :maxdepth: 2
    
   applications.rst
   commands.rst
   

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

