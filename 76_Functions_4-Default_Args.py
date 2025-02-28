# 03-100: Default Arguments in functions

""" 
def greeting(name):
    print(f'Hi {name}')

greeting()      # Error! Missing args
greeting('Kristine')
"""

# Setting a default value in args

def greeting(name = 'Guest'):
    print(f'Hi {name}')

greeting()
greeting('Kristine')


# The wrong way

def a_function(collection = []):
    collection.append(1)
    print(id(collection))
    return collection

print(a_function())     # 1

# Other part of code
print(a_function())     # 1, 1
## Both are using the same memory spot




# CodingExercise
"""
Create a function called counter that accepts an argument called initial_count and returns that argument incremented by 1. initial_count must have a default value of 0.
"""


def counter(initial_count = 0, last_count = 5):
    print(initial_count)
    for step in range(initial_count, last_count):
        def printer_func():
            return step +1
        print(printer_func())
        
counter(0, 5)
    

def counter(initial_count = 0):
       
       return initial_count +1

print(counter())
