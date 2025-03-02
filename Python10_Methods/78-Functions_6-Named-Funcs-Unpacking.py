# 03-102: Named functions Unpacking


# Asterisk can be used to allow many non-defined arguments

def greeting(*args):
    print('Hi ' + ' '.join(args))

greeting('Tifanny', 'Hudgens')
greeting('Homer', 'J.', 'Simpson')


# Discovering the fact that * works with Tuples!

def printer(*args):
    print(args)

printer('Pepito', 'Perez')      # ('Pepito', 'Perez'), a tuple



##

def greeting(*names):
    print('Hey, ' + ' '.join(names))

greeting('Juanito', 'Lopez')
greeting('Menganito', 'Idelfonso', 'Juarez')



##

def more_use_cases(time_of_day, *args):
    print('Hi ' + ' '.join(args))

more_use_cases('Raquel', 'Diaz')
more_use_cases('Juanita', 'Rigoberta', 'Piscinas')

##

def more_use_cases_2(time_of_day, *args):
    print( f'Hello, {' '.join(args)}, Have a good {time_of_day}' )

more_use_cases_2('Morning', 'Raquel', 'Diaz')
more_use_cases_2('Night', 'Juanita', 'Rigoberta', 'Piscinas')