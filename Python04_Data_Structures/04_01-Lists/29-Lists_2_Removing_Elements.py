# 02-050: Lists - Removing elements
# .remove() / .pop() / .clear() / `del`

users = ['Kristine', 'Tifanny', 'Jordan', 'Leann']

# .remove()
users.remove('Jordan')

print(users)    # ['Kristine', 'Tifanny', 'Leann']

# .pop()
## Pop takes the LAST item, prints it and then removes it from the list

popped_user = users.pop()
print(popped_user)      # Leann
print([popped_user])    # ['Leann']

print(users)            # ['Kristine', 'Tifanny'] The reamining items in the list.

# del method
## Syntax: del list[index]

print(users)    # ['Kristine', 'Tifanny']

del users[0]
print(users)    # ['Tifanny']


# .clear()
users = ['a', 'b', 'c', 'd']
print(users) # ['a', 'b', 'c', 'd']

users.clear()
print(users) # [] None, empty, the entire list has been wiped.