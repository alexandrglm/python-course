# 02-030 String interpolation using an Index
# with .format() function.

name = 'Elisabeth'
age = 65
product = 'The Substance'
from_account = 'José from Don Pepito\'s Store'

# greeting = 'Product Purchased: {2}\n Greetings, {0},\n  you are listed as {1} years old - {3}'.format(name, age, product, 'Don Pepito\'s Store')

greeting = f'Product Purchase: {product}\n Hi, {name} \n you are listed as {age} years old. -\n {from_account}.'

print(greeting)