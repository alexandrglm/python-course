# 03-105: Lambda functions


full_name = lambda first, last: f'{first} {last}'

print(full_name('Kristine', 'Hudgens'))


# Adding a function that needs the lambda

full_name = lambda first, last: f'{first} {last}'

def greeting(name):
    print(f'Hey {name} !')

greeting(full_name('Pepito', 'Perez'))




# Coding Exercise
"""
In the code below, create a variable called "greeting" and assign it a lambda function that accepts a name as an argument, and return the string "Hi, name".

Example: If you pass in the name "Jordan", it should return "Hi, Jordan".
"""

def lambda_practice():
    # Write your code here
    greeting = lambda name: f'Hi, {name}'
    
    return greeting
