"""
"""


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
    def __init__(self, cmd=None, alt=None, sub_cmd_set=None, description=None, 
                    valid_func=None, exec_func=None, arg_spec=None):
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
        self.subcmds = {}

    @property
    def cmd_dict(self):
        return {self.cmd : { 'help'     : self.description, 
                             'alt'      : self.alt, 
                             'valid_func': self.valid_func,
                             'exec_func': self.exec_func,
                             'comp_dict': self.completion_dict,
                             'sub_cmds' : self.subcmds } }

    def subcmd(self):
        def decorator(f):
            print "detected subcmd"
            self.subcmd[f.name] = {'help':f.__doc__, 'exec_func': f}
        return decorator

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
