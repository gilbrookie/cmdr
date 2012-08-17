
class Application(object):
    def __init__(self, registered_commands=None):
        self.prompt = "> "

    def start(self):
        """Runs the command loop"""
        # Show prompts,wait for input
        # Validate command
        # loop until termination command issued (exit, CTRL+C)
