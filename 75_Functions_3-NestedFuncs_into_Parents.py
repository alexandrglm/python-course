# 03-099: Nested Functions into Parents functions

"""
We came from here:


def full_name(first, last):
    return f'{first} {last}'

data = full_name('TheName', 'TheSurname')


def greeting(name, surname):
    print(f'Hey {name} {surname}!')

greeting('Kristine', 'Hudgens')
"""

def greeting(first, last):
    def full_name():
        return f'{first} {last}'
    
    print(f'Hey {full_name()}')

greeting('Pepito', 'Perez')



# CodingExercise
"""
Create a function called greeting that accepts a persons name as an argument. Your function should return "Hello, {persons name}".

Example: Passing in 'Jordan' should return 'Hello, Jordan'
def greeting(name):
    return f'Hello, {name}'
    

greeting('Pepito')
"""