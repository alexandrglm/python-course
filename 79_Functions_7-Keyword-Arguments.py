# 03-103: Keyword Arguments


# ** keywords, returns a dictionary:

def greeting(**kwargs):
    print(kwargs)

greeting()  # {}

# Extending the dict creation

greeting(first_name = 'Pepito', last_name = 'Perez')


# Extending them introducing conditions

def greeting(**kwargs):
    if kwargs:
        print(f'Hi {kwargs['first_name']} {kwargs['last_name']}, have a {kwargs['mood']} {kwargs['moment']}!')
        print(kwargs)

    else:
        print('Hi Guest, have a great day!')


greeting(mood = 'Terrorific', moment = 'afternoon', first_name = 'Susana', last_name = 'Lopez' )
greeting()      # Hi Guest, have a great day!



