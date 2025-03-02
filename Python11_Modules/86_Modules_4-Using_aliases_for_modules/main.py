# 03-111 main.py 

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

from math import sqrt


def render():
    print(greeting('Krisinte', 'Hudgens'))
    num = float(input('We\'re going to do some square roots.\nChoose a base number : '))
    print(f'The square root for {num} is  {sqrt(num)}.')
render()
#print('DEBUG: render() is executed')