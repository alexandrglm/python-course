# Attempt #1: 
import math

def manual_exponent(base, exponent):
    print('Using basics "**" :  ' + str(base ** exponent))
    print('Using math.pow()  :  ' + str(math.pow(base, exponent)))

# manual_exponent(2, 3)
# manual_exponent(10, 2)


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
    

# manual_exponent_iterative(2, 2.2)
# manual_exponent_iterative(2, Decimal(2.2))
# manual_exponent_iterative(float(2.24323423421223424), 3)
# manual_exponent_iterative(2, (0.02+0j))
# manual_exponent_iterative(2, 2) 
# manual_exponent_iterative(2,-6)
# manual_exponent_iterative(2,0)


# Attempt 3: Mixing all offered solutions and mine's
import math
from decimal import Decimal
from functools import reduce


def super_power_root_function(base, exponent):

    # case 0 static
    if exponent == 0:
        total = 1
        print(total)
    
    # case imposible
    elif isinstance(exponent, complex):
        print('Sorry, I can\'t handle strings nor complex numbers whose content has an imaginary part that cannot be processed')
        
    # case negatives using functional approach with reduce
    elif Decimal(exponent) < 0:
        computed_list = [base] * abs(exponent) # le damos la vuelta al exponente ...

        total = reduce(lambda total, element: total * element, computed_list, 1)

        print(Decimal(1 / total)) # ... y aquí volvemos a recuperar el negativo como fracción.
    
    # case Decimals, using for ... in ... range()    
    elif isinstance(exponent, (float, Decimal)) or (isinstance(exponent, int) and exponent != int(exponent)):
        total = 1
        for i in range(int(exponent)):
            total = (math.pow(base, exponent))
        print('For...in...range used: ' + str(Decimal(total)))      
    
    
    # case positive integers using iteration
    elif exponent > 0:
        
        counter = exponent - 1
        total = base
        while counter > 0:
            total *= base
            counter -= 1
        print('Iteration approach used: ' + str(total))

    # Anything else, error debug, etc.
    else: print('debug error, general')


super_power_root_function(3, 3)
super_power_root_function(3, 3.2)
super_power_root_function(3, Decimal(3.2))
super_power_root_function(3, float(3.2))
super_power_root_function(float(3.24323423421223424), 3) 
super_power_root_function(3,0)

