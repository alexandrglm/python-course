

# Attempt 2: Iterative approach (lol)

import math
from decimal import Decimal

def manual_exponent_iterative(base, exponent):

    if isinstance(exponent, float):
        print('Sorry but I can\'t manage floating exponents.')
    elif isinstance(exponent, Decimal):
        print('Sorry, I can\'t manage Decimal exponents')
    elif isinstance(exponent, complex):
        print('I\'m not designed for using complex numbers as exponents. I can only manage whole numbers as exponents, can\'t you???')
    elif exponent == math.inf:
        print('Oh my gosh! Can you stop giving non-functional exponents? Have you ever tried to calculate a power root using Infinite as Exponent?????')
    elif exponent <= 1:
        print(math.pow(base, exponent))
    else:
        for exponent in range(1, int(exponent)):
            exponent = exponent + 1
            print(math.pow(base, exponent))
    

manual_exponent_iterative(2, 2.2)
manual_exponent_iterative(2, Decimal(2.2))
manual_exponent_iterative(2, (0.02+0j))
manual_exponent_iterative(2, math.inf)
manual_exponent_iterative(2, 2)

