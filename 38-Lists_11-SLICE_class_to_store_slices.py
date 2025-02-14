# 02-059: slice() - Handling slice() to store slices.

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming'
]
print('\nOriginal List: ' + str(tags))
print(tags[ : 2 ])      # ['python', 'development']


# slice() - How Slice works:
# slice() returns a tuple, adding one None items on the right/on the left both sides.
## Explicit slice()

slice_obj = slice(2)
print(slice_obj) # slice(None, 2, None)



## Explicit slice() using a list

slice_obj = slice(tags)
print(slice_obj) # slice(None, ['python', 'development', 'tutorials', 'code', 'programming'], None)



## Slice() as an index onto a new var

slice_obj = slice(2)
print(tags[slice_obj])  # Again, ['python', 'development'], using slice(2) as a new object on index



## slice() and Immutability 
## (Uncomment this to see what syntax error is returned)

# slice_obj = [ : 2]
# print(tags[slice_obj])  # Slice_obj, which stored "slice(tags)" cannot be reused like this



# slice( start : stop : step ) syntax

print(tags[1 : 4 : 2])      # ['development', 'code']

slice_obj = slice(1, 4, 2)
print(tags[slice_obj])      # Both methods returns the same, ['development', 'code']

print(slice_obj.start)      # Slice Start:  1
print(slice_obj.stop)       # Slice Stop:   4
print(slice_obj.step)       # Slice Step:   2



# More examples

list2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print('\nOriginal list:  ' + str(list2))

print(list2[ 2 : -1 : 3 ])  # c, f, i

slice_list2 = slice(2, -1, 3)
print(list2[slice_list2])   # c, f, i

print(slice_list2.start)      # Slice Start:  2
print(slice_list2.stop)       # Slice Stop:   -1
print(slice_list2.step)       # Slice Step:   3


