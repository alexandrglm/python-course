# 02-059: slice() - Handling slice() to store slices.

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming'
]
print(tags)
# print(tags[ : 2 ])      # ['python', 'development']


# slice() - How Slice works:
# slice() returns a tuple, adding one None item on the right/on the left sides.

slice_obj = slice(2)
print(slice_obj) # slice(None, 2, None)


slice_obj = slice(tags)
print(slice_obj) # slice(None, ['python', 'development', 'tutorials', 'code', 'programming'], None)