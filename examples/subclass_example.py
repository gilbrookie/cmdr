
from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cmdr import Cmdr, Command, subcmd
from pprint import pprint as pp

class Blog(Command):
    """Blog command"""

    def __init__(self):
        super(Blog, self).__init__()
        self.data={}

    @subcmd
    def add(self):
        print("Blog Add subcmd")

    @subcmd
    def edit(self, id=None):
        print("Blog Edit subcmd")

class Project(Command):
    """Project command"""

    @subcmd
    def add(self):
        """Adds a new project entry"""
        print("Project Added")

    @subcmd
    def edit(self):
        """Edits a project entry"""
        print("Project Edited")

class LoadTest(Command):
    """LoadTest"""
    def execute(self):
        print("Execute LoadTest")


app = Cmdr("blog_cli")

b = Blog()
p = Project()
lt = LoadTest()

print("")

#pp(b.cmd_dict)

app.register_cmd(b)
app.register_cmd(p)
app.register_cmd(lt)

app.start()


