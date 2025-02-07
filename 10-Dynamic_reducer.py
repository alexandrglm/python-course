# 02 028 Creating a dynamic reducer
## Exercise: reduce(), lambda functions, use of dictionaries

import operator
from functools import reduce

def dynamic_reducer(collection, op):

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)
                      
print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))

""""
list = [1, 2, 3]

operator = 1 + 2 + 3

def dynamic_reducer(list, str(operator)):
    return

dynamic_reducer()
"""

"""
dynamic__reducer([1, 2, 3],'+') # the sum, 6
dynamic__reducer([1, 2, 3],'-') # the subs, -4
dynamic__reducer([1, 2, 3],'*') # the mult., 6
dynamic__reducer([1, 2, 3],'/') # the division, -4
"""