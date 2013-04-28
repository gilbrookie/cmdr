
#from __future__ import print_statement

"""
cmdr.state
~~~~~~~~~~

This module implements the StateController class that is used to manage shared variables and "state"
between commands and application.
"""

class StateController(object):
    """
    The StateController class models the "Borg" pattern whereby instances of this class share the
    same data and implement access to the shared data resources.  The shared resource is managed
    with a class attribute, and instances of the StateController all have access to it.

    Access is restricted except through the StateController instance's __getitem__ and __setitem__
    accessors.  Which provides dictionary style lookups and access.
    
    One additional feature added is that each client is given an ID and name.
    """
    _app_state = {}
    client_count = 0

    def __init__(self, client_str=None):
        self.client_id = self.client_count + 1
        self.client = "_".join([str(self.client_id), client_str])

    def dump(self):
        """Print out the shared data dictionary (keys and values)"""
        if not _app_state():
            print("State dict is empty")
        else:
            for k, v in self._app_state.iteritems():
                print("%s, %s" % (k, v))

    def __getitem__(self, key):
        return self._app_state.get(key)

    def __setitem__(self, key, value):
        try:
            self._app_state[key] = value
        except KeyError:
            print("Error: Failed to locate key %s" % key)
        except Exception as e:
            print(e)

