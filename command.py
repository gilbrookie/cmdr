"""
"""
from functools import wraps

class CmdMetaclass(type):
    def __new__(cls, name, bases, attrs):

        new_cls = super(CmdMetaclass, cls).__new__(cls, name, bases, attrs)

        subcmds = {}
        for key in attrs:
            print key

            attr = getattr(new_cls, key)
            try: 
                if hasattr(attr,"is_subcmd"):
                    print "SUBCMD: %s" % key

                    subcmds[key] = {'help': attr.__doc__, 'exec_func': attr }

            except AttributeError:
                continue
   
        setattr(new_cls, "subcmds", subcmds)

        return new_cls

class Command(object):
    """
    Optional args:
    * cmd
    * sub_cmd_set - (cmd1, args), (cmd2, args)
    * alt
    * description
    * validator_func - callback
    * execution_func - callback
    * arg_spec
    """

    __metaclass__ = CmdMetaclass

    def __init__(self, cmd=None, alt=None, sub_cmd_set=None, description=None, 
                    valid_func=None, exec_func=None, arg_spec=None):

        print "__init__ %s" % self.__class__.__name__

        self.cmd = cmd
        if not cmd:
            self.cmd = self.__class__.__name__.lower()
#        else:
#            self.cmd = cmd
    
        self.description = description
        if not description:
            self.description = self.__doc__
#        else:
#            self.description = description

        self.valid_func = self.validate
        if valid_func:
            self.valid_func = valid_func
#        else:
#            self.valid_func = self.validate

        self.exec_func = self.execute
        if exec_func:
            self.exec_func = exec_func
#        else:
#            self.exec_func = self.execute

        self.alt = alt
        self.completion_dict = None
        #self.subcmds = self.__dict__['subcmds']

    @property
    def cmd_dict(self):
        return { self.cmd:{ 'help'     : self.description, 
                            'alt'      : self.alt, 
                            'valid_func': self.valid_func,
                            'exec_func': self.exec_func,
                            'comp_dict': self.completion_dict,
                            'subcmds' : self.subcmds } }

    @property
    def cmd_strs(self):
        if not self.subcmds:
            return [self.cmd]

        else:
            return [" ".join([self.cmd, sc]) for sc in self.subcmds.keys()]

    def validate(self):
        """Validates the commands arguments"""
        print "validate"

    def execute(self, line):
        """Executes the command
        Return  True on success
                False on error
        """
        print "Execute"

        if self.subcmds:
            for k, v in self.subcmds.iteritems():
                if line == k:
                    f = getattr(self, k)
                    f(v)


    

        return True


def subcmd(f):
    f.is_subcmd = True
    return f
