
from aclip2 import Application, Command, subcmd

class Echo1(Command):
    def execute(self, *args):
        print "Echo1!"
        print args

class Echo2(Command):
    
    @subcmd
    def stars(self):
        print "****Echo2: stars() ****"

    @subcmd
    def carets(self, *args):
        print "^^^^Echo2: carets() ^^^^"
        print args

app = Application(__name__, registered_commands=[Echo1(), Echo2()])

@app.cmd("echo3")
def echo3(*args):
    print "Echo3"
    print args

app.start()
