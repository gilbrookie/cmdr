
from datetime import datetime
from aclip2 import application 
from aclip2.command import Command, subcmd
from pprint import pprint as pp

class Blog(Command):
    """Blog command"""

    def __init__(self):
        super(Blog, self).__init__()

    @subcmd
    def add(self):
        print "Blog Add subcmd"

    @subcmd
    def edit(self, id=None):
        print "Blog Edit subcmd"

class Project(Command):
    """Project command"""

    @subcmd
    def add(self):
        """Adds a new project entry"""
        print "Project Added"

    @subcmd
    def edit(self):
        """Edits a project entry"""
        print "Project Edited"

class LoadTest(Command):
    
    def execute(self):
        print "Execute LoadTest"


app = application.Application("blog_cli")

b = Blog()
p = Project()


print ""

#pp(b.cmd_dict)

app.register_cmd2(b)
app.register_cmd2(p)

app.start()


