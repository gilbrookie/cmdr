
from datetime import datetime
from aclip2 import application 
from aclip2.command import Command
from pprint import pprint as pp


class Blog(Command):
    """Blog command"""

    def __init__(self):
        super(Blog, self).__init__()

    def cmd_str(self):
        if not self.sub_cmds:
            return self.cmd

        else:
            [" ".join([self.cmd, sc[0]]) for sc in self.sub_cmds]
            

    def add(self):
        print "Blog Add subcmd"

    def edit(self, id=None):
        print "Blog Edit subcmd"


app = application.Application("blog_cli")

b = Blog()
pp(b.cmd_dict)
