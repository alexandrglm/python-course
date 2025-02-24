# 03-092. Conditionals full list

"""
List of Comparision operators:

==  - EQUALITY
!=  - INEQUIALITY
<>  - INEQUALITY (but deprecated)

>   - GREATER
>   - GREATER OR EQUAL

<   - LESS
<=  - LESS OR EQUAL


"""

# EQUALITY
username = 'jonsnow'

if username == 'jonsnow':
    print('Welcome Jon')
else:
    print('You are not allowed to pass in!')

# INEQUALITY

username = 'jonsnow'

if username != 'jonsnow':
    print('You are not allowed to pass in!')
else:
    print('Welcome Jon')

# Greater 

age = 18

if age > 19:
    print(f'Selected {age} is greater than 19')
else: 
    print(f'Selected {age} is NOT greater than 19')



# Lists comparisions
## Comparision operators VALUES ! (not items)

user_list = ['Kristine', 'Tiffany']
second_list = ['Jordan', 'Brayden']

if user_list == second_list:
    print('They match')
else:
    print('They don\'t match')




user_list = ['Kristine', 'Tiffany']
second_list = ['Kristine', 'Tiffany']

if user_list == second_list:
    print('They match')
else:
    print('They don\'t match')
