aclip2 - Another Command Line Interface Processor written in Python
===================================================================

Seriously, isn't this what the world needs, another CLI processor in python?
I get it, I know.  I just wanted to try my hand at writing one myself - deal with it.

Impotus
-------
I have a web application that I wanted to build my own CLI application to interact
with the data and provide some admin functionality.

This project is made to provide an API for designing your own cli applications

Usage
=====

Designing Commands
------------------
:: 

# Build a command directly
cmd = Command(name="cmd", desc="Sample", exec_func=exec_call_back)

::

# Subclass
class Cmd(Command):
    def __init__(self):
        self.name = "cmd"
        self.desc = "Sample"

    def execute(self):
        print do something
        return True

::

# Using function Decorator 
@aclip.cmd
def cmd(args):
    """description: Sample"

Building the CLI application
-----------------------------
::

# Instatiate an Application object
app = aclip2.Application()
# Pass in the commands that are available
app.register_commands([cmd])
# Start the app
app.start()

# note "exit" and "help" are builtin comands


Roadmap
=======

1. Get the basics working
    1. Implement Decorator commands (for non-complex commands)
    2. Implement Subclasses commands (for more complex commands- better control)
    3. Add support for tab completion
    4. Create documentation
    5. Create unittests
2. Add other "nice" features
    1. Colors
    2. ProgressBar
    3. Execute in thread
