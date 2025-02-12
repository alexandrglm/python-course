# 02-049: Lists

"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']
print(users)    # ['Kristine', 'Tiffany', 'Jordan']

# .insert(index, data)
users.insert(0, 'Anthony')
print(users)    # ['Anthony', 'Kristine', 'Tiffany', 'Jordan']


# .append(data)
users.append('Ian') 
print(users)    # ['Anthony', 'Kristine', 'Tiffany', 'Jordan', 'Ian']

# Querying elements by using [index]
print(users[2]) # Tiffany

print([users[2]]) # ['Tifanny']

# Reasigning elements using [index]
users[2] = 'Francisca'

print(users[2]) # Francisca

print(users)    # ['Anthony', 'Kristine', 'Francisca', 'Jordan', 'Ian']



