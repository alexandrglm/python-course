# Module 02 - 069: Python: Dictionaries, Exercise:
## Building an Histogram with no external libraries

"""
Concepts:

g $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
x $$$$$$$$$$$$$$$$$
o $$$$$$$$$$$$$$$$$$$$$$$$

print(4 + 'w')  # NOPE!
print(4 * 'w')  # YEP!
"""


# Attempt 1

dict_1 = {
    '$' :   '$' * 10
}

g = 7
f = 8
x = 4
o = 5

print( 'g:' + f'{dict_1['$'] * g}\n')
print( 'f:' + f'{dict_1['$'] * f}\n')
print( 'x:' + f'{dict_1['$'] * x}\n')
print( 'o:' + f'{dict_1['$'] * o}\n')



# Proposed solution
## The dictionary must include all the variables, not the printed symbol!

sales = {
    'google' : 20,
    'facebook' : 42,
    'x-twitter' : 10,
    'offline' : 12
}


print('g: ' + sales['google'] * '$')
print('f: ' + sales['facebook'] * '$')
print('x: ' + sales['x-twitter'] * '$')
print('o: ' + sales['offline'] * '$')

"""
g: $$$$$$$$$$$$$$$$$$$$
f: $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
x: $$$$$$$$$$
o: $$$$$$$$$$$$
"""