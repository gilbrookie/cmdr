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

1. Get the basics working
    1. Implement Decorator commands (for non-complex commands) **DONE**
    2. Implement Subclasses commands (for more complex commands- better control) **DONE**
    3. Add support for tab completion **DONE**
    4. Get a first release done (get it working and ship it)      
    5. Verify support for python version (2.7, 3.0) 
    6. Create documentation
    7. Create unittests

2. Add other "nice" features
    1. Colors
    2. Allow support for arbitrary level of command depth
    3. Support sub command prompts 
    2. Execute in thread
