# 03-098: Functions Return statements

"""
def full_name(first, last):
    print(f'{first} {last}')

full_name('TheName', 'TheSurname')
"""

# Returning the value
def full_name(first, last):
    return f'{first} {last}'

## Once returned, invoking a function as is won't give us nothing
full_name('TheName', 'TheSurname')

## We need to add the result into something, like a new object

data = full_name('TheName', 'TheSurname')


def greeting(data):
    print(f'Hey {data}!')

greeting(data)




## Take care of what you do with the objects, otherwise your nested functions won't work

def a(b,c):
    print(f'{b} {c}')

d = a('Pepito', 'Perez')

def e(f):
    print(f'Hey {f}')

e(d) # None !

# CodingExercise

"""
Create a function called sum_two_numbers that accepts two arguments. The function should 'return' the total of those two arguments added together.
"""

def sum_two_numbers(a , b):
    return a + b

value = sum_two_numbers(5,7)
print(value)