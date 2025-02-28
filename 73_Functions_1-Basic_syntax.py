# 03-097: Functions, basic syntax


def full_name():
    print('Hi')

full_name()




# With positional args
# Now, a functions, is a method

def full_name_args(first, last):
    print(f'{first} {last}')

full_name_args('Kristine', 'Hudgens')  
full_name_args('AnotherName', 'AnotherSurname')  




# Authorizing example

def auth(email, password):
    if email == 'thecorrect@mail.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not Authorized')

auth('theINCORRECT@mail.com', 'secret')
auth('thecorrect@mail.com', 'secret')




# No args.

def hundred():
    for num in range(1,101):
        print(num)

hundred()

## Converted into a Counter

def counter(max_value):
    for num in range(1, max_value):
        print(num)

counter(68)

