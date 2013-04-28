"""Rough outline of colour \"sections\"

- Normal command output
- Warning messages
- Error messages
- highlighed messages
- "special" messages
- Table output? 

- can you define commands that only use specific colours?

"""
from clint import colored 
class ColourScheme(object):
    def __init__(self, name):
        self.name = name

        # default colourscheme
        self.std = colored.white
        self.warn = colored.yellow
        self.err = colored.red
        self.emph = colored.white
        self.special = colored.blue
        self.table  = colored.yellow

    
