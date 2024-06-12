"""
index.py
---------
index all function handlers
"""


# imports here -----------------------
from .start import start
from .echo import echo
from .help import help_command
from .hello import hello
from .whoami import whoami
from .join import join
from .today import today
from .oneweek import oneweek
from .onemonth import onemonth

command_map = {
    'start': start,
    'echo' : echo,
    'join': join,
    'today': today,
    'oneweek': oneweek,
    'onemonth': onemonth,
    'whoami' : whoami,
    'hello' : hello,
    'help' : help_command
    }

# --------------------------------------
def index():
    """
    
    """
    return command_map