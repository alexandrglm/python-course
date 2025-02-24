# 03-088: List comprehesion

num_list = range(1,11)

cubed_nums = []


# A regular for...in expression

for num in num_list:
    cubed_nums.append(num ** 3)

print(list(num_list))
print(cubed_nums)   # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]



# A for...in declaration in a var

cubed_nums = [num ** 3 for num in num_list]

print(list(num_list))
print(cubed_nums)       # Gives the same result


# As we've seen before, the iterator can be named as wanted

cubed_nums = [x ** 3 for x in num_list]

print(list(num_list))
print(cubed_nums)       # Gives the same result


# .map() + lambda

cubed_nums = list(map( lambda num: num ** 3, list(num_list) ))
print('\nUsing lambda :\n', cubed_nums)



# Adding conditionals

even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

print('\nNumber List: ', list(num_list))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\nEven Numbers: ', even_numbers)     # [2, 4, 6, 8, 10]

# In a expression

even_numbers = [num for num in num_list if num % 2 == 0 ]

print('\nUsing comprehesion: \n', list(num_list))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers)     # # [2, 4, 6, 8, 10]








# Coding Exercise
"""
Create a variable called result and use list comprehension to increment each number from the numbers list by 1.
"""

"""
def list_comprehension():
    numbers = [1,2,3,4,5,6]
    # Write your code here
    
    
    return result
"""