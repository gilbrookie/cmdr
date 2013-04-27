
"""
"""

class StateController(object):
    _app_state = {}
    client_count = 0

    def __init__(self, client_str=None):
        self.client_id = self.client_count + 1
        self.client = "_".join([client_str, client_id])

    def dump(self):
        if not _app_state():
            print "State dict is empty"
        else:
            for k, v in self._app_state.iteritems():
                print k, v

    def __getitem(self, key):
        return self._app_state.get(key)

    def __setitem(self, key, value):
        try:
            self._app_state[key] = value
        except KeyError:
            print "Error: Failed to locate key %s" % key
        except Exception as e:
            print e

