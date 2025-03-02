# 03-109: Creating custom modules


# helper.py

def greeting(first, last):
    return f'Hi {first} {last}!'


# main.py 
import sys
sys.path.insert(0, './libs')
import helper

def render():
    print(helper.greeting('Krisinte', 'Hudgens'))
render()