# main.py 

"""
Original code works perfectly on terminal, BUT, for VSCode (or any IDE-Debuger),
some modifications are needed:

1. import os + sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "libs")))
OR
2. from pathlib import Path + sys.path.insert(0, str(Path(__file__).parent / 'libs'))

"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'libs'))
from helper import greeting

def render():
    print(greeting('Krisinte', 'Hudgens'))

render()
#print('DEBUG: render() is executed')