# main.py 

import sys
sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('Krisinte', 'Hudgens'))

render()
print('DEBUG: render() is executed')