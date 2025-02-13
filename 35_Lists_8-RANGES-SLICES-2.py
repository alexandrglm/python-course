# 02-056: Advanced techniques for implementing RANGES and SLICES inlists.

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]
print('Original List:  ' + str(tags))  

# Ranges [ startDelimiter : endDelimiter]
tag_range = tags[1:-1]
print(tag_range)        # ['development', 'tutorials', 'code', 'programming']


# Slicing [ inclusive : exclusive : the range ]
"""
What slice ranges do:
- Inclusive: The starting index of the slice.
- Exclusive: The ending index of the slice.
- Interval: It determines how many items to skip between each selected item.
"""

tag_range = tags[:-1:2] # From 0 to the Second-Last, take EVERY TWO items
print(tag_range)        # ['python', 'tutorials', 'programming']

tag_range = tags[1:4:]  # Same as [1:4], take ALL the items
print(tag_range)        # ['development', 'tutorials', 'code']

tag_range = tags[1:5:2] # From First to Fifth, take EVERY TWO items
print(tag_range)        # ['development', 'code']

tag_range = tags[1:5:3] # From 1 to 5 - From 1st to 5th, take EVERY THREE items
print(tag_range)        # ['development', 'programming']

tag_range = tags[::2]   # From Start to End, take EVERY TWO items
print(tag_range)        # ['python', 'tutorials', 'programming']

## A better slicing understanding:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

ranges = numbers[::3]       # From the Beginning to the END, take every THREE items
print(ranges)               # 1, 4, 7, 0

ranges = numbers[::4]       # From the Beginning to the END, take every FOUR items
print(ranges)               # 1, 5, 9

ranges = numbers[2:-1:2]    # From 3rd to SecondLast, take every TWO items
print(ranges)               # 3, 5, 7, 9




# RESERVSE sorting with RANGES

tag_range = tags[::  -1  ]

print('Original List:  ' + str(tags)) 
print(tag_range)    # ['computer science', 'programming', 'code', 'tutorials', 'development', 'python']

tag_range = tags[  :  : -2 ]
print(tag_range)    # ['computer science', 'code', 'development']

## Reverse sorting DOES NOT ALLOW INCLUDING START-FROM / END-ON
tag_range = tags[ 1 : 6 : -2 ]
print(tag_range)    #  []




# RESERVSE sorting the list ONTO A NEW VARIABLE by using .sort()

sorted_tags = tags.sort(reverse=True)
print(sorted)       # Empty! That's the immutability on Python!

## REVERSE sorting directly onto the list will work, instead.
tags.sort(reverse=True)
print(tags)         # ['tutorials', 'python', 'programming', 'development', 'computer science', 'code']



