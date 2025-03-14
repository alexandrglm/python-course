# 03-145: Exercise: Getting Average from a list

# A first approach, but NOT the expected way
## Libs to be used
#import statistics
#import numpy

## Var list to be used
# num_list = [1, 2, 3, 4, 5, 6]


## The expectec callback
#print(statistics.mean(num_list))

# Exercise must be implemented with NO external libs
## Suggestions:
#
# functools library has:
# functools.reduce
####################
# 1st Attempt
# 
# Resources read:
# https://www.geeksforgeeks.org/reduce-in-python/
# from functools import reduce

# num_list = [1, 2, 3, 4, 5, 6]

# def get_average(num_list):

#     total = reduce(
#         lambda x, y: x + y, num_list
#     )

#     total_elements = int(len(num_list))

#     average = total / total_elements
    
#     return average

# print(get_average(num_list))    # 3.5


# Guided Solution

from functools import reduce
# import numpy

num_list = [1, 2, 3, 4, 5, 6]

def get_average(num_list):
    
    total = reduce( ( lambda total, element: total + element), num_list )

    return total / len(num_list) # Remember, a non-zero based is an advantage here

# print(numpy.mean(num_list)) # 3.5
# What numpy.mean does:
'''
numpy.MEAN directly get the average from a list
'''

print(get_average(num_list))    # Nox, it's the average: 3.5
