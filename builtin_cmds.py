
from commands import Command as Cmd

def show_help():
    return True

def exit():
    return False

# Built-in commands
Help = Cmd(name="Help", alt=["?"],
            desc="Show the help menu",
            exec_func=show_help)

Exit = Cmd(name="Exit", alt=["q","x"],
            desc="Exit the command line",
            exec_func=exit)
