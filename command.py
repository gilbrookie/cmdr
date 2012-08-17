




class Commmand(object):
    """
    Optional args:
    * name
    * alt
    * description
    * validator_func - callback
    * execution_func - callback
    * arg_spec
    """
    def __init__(self, name=None, description=None, valid_func=self.validate
                    exec_func=self.validate, arg_spec=None):

        self.name = self.__class__.__name__
        self.descrption
    
    def validate(self):
        """Validates the commands arguments"""
        print validate

    def execute(self):
        """Executes the command
        Return  True on success
                False on error
        """
        print "Execute"
        return True



_registered_commands = [Exit, 
                        Help]
