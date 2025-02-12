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

"""
Two methods will be explained:

1. By doing an ITERATIVE approach.
2. By performing a FUNCTIONAL approach.
"""



# 1. Iterative approach

from functools import reduce


