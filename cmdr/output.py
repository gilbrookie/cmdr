
import sys
from cmdr.state import StateController


STDOUT = sys.stdout.write
STDERR = sys.stderr.write
# Load the state manager that has the scheme information
__state = StateController("output_manager")
__scheme = __state['colorscheme']

def writeln(msg, stream=STDOUT):
    """Send messages to STDOUT, can contain formatting info"""
    stream(msg)

def draw_table(headers, data):
    pass

def draw_list(keys, values):
    pass

def debug(msg):
    """Sends messages to stderr, can contain formatting info"""
    writeln(msg, STDERR)

def log_msg(msg):
    """Sends logs to logger without formatting"""
    logger.info(msg)

# functions that wrap the msg text in colour information
# These can be combined into text that is sent to writeln()
def warn(msg):
    return __scheme.warn(msg)

def err(msg):
    return __scheme.err(msg)

def emph(msg):
    return __scheme.emph(msg)

def special(msg):
    return __scheme.special(msg)

def clean(msg):
    pass
