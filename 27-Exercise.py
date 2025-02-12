# Attempt #1: 
import math

def manual_exponent(base, exponent):
    print('Using basics "**" :  ' + str(base ** exponent))
    print('Using math.pow()  :  ' + str(math.pow(base, exponent)))

manual_exponent(2, 3)
manual_exponent(10, 2)


# Attempt 2: Iterative approach (lol)

import math
from decimal import Decimal


def manual_exponent_iterative(base, exponent):
    """    
    if isinstance(exponent, float):
        print('Sorry but I can\'t manage floating exponents.')
    elif isinstance(exponent, Decimal):
        print('Sorry, I can\'t manage Decimal exponents')
    
    elif exponent <= 1:
        print(math.pow(base, exponent))
    else:
    """
    
    if isinstance(exponent, complex):
        print('Sorry, I can\'t handle complex numbers whose content has an imaginary part that cannot be processed')
    elif exponent < 0:
        result = (math.pow(base, exponent))
        print(result)
    else:
        result = 1
        for iteration in range(int(exponent)):
            result = (math.pow(base, Decimal(exponent)))
        print(result)


        # for exponent in range(1, int(exponent)):
            # exponent = exponent + 1
            # print(math.pow(base, exponent))
    

manual_exponent_iterative(2, 2.2)
manual_exponent_iterative(2, Decimal(2.2))
manual_exponent_iterative(float(2.24323423423424), 3)
manual_exponent_iterative(2, (0.02+0j))
manual_exponent_iterative(2, 2) 
manual_exponent_iterative(2,-6)
manual_exponent_iterative(2,0)


