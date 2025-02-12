# 02-047: Manual Exponents function

# Attempt 1:
## A first approach, a basic approach, would be:
"""
import math

def manual_exponent(base, exponent):
    print('Using basics "**" :  ' + str(base ** exponent))
    print('Using math.pow()  :  ' + str(math.pow(base, exponent)))

manual_exponent(2, 3)
manual_exponent(10, 2)
"""



# Attempt #2: Using iteration, not so serious, gargabe include
"""
import math
from decimal import Decimal


def manual_exponent_iterative(base, exponent):
        
    # if isinstance(exponent, float):
        # print('Sorry but I can\'t manage floating exponents.')
    # elif isinstance(exponent, Decimal):
        # print('Sorry, I can\'t manage Decimal exponents')
    
    # elif exponent <= 1:
        # print(math.pow(base, exponent))
    # else:
    
    
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
"""

# Now, the lesson:
"""
- **One is a manual way of doing it** it is what's called an **iterative approach** where we are going to **simply iterate over the elements and then build up the solution**.
  
- The second one, I'm also going to show you a **functional approach** and a functional approach is **going to leverage, and this is where one of the hints will be, it is going to leverage the reduce function**.
"""
# 1. Iterative approach

from functools import reduce

def manual_exponent_iteration_approach(base, exponent):
    
    counter = exponent - 1
    total = base

    while counter > 0:
        total *= base
        counter -= 1

    return(total)

print(manual_exponent_iteration_approach(2, 3))
print(manual_exponent_iteration_approach(10, 2))


# 2. Functional approach

def manual_exponent_functional_approach(base, exponent):

    computed_list = [base] * exponent

    return(reduce(lambda total, element: total * element, computed_list ))

print(manual_exponent_functional_approach(2,3))


