# 02-051: Nesting lists & Multiple Data Types 

users = ['Kristine', 'Tifanny', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

users_list = mixed_list.pop()

print(users_list)
print(mixed_list)

# Handling nested lists
nested_lists = [[123], [234], [345]]

print(nested_lists)
print(nested_lists[2])

from_nested = nested_lists.pop()

print(nested_lists)
print(from_nested)