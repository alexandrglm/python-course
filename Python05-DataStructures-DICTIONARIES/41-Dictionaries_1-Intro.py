# 02-062: Dictionaries, intro

# Syntax { 'key' : 'value', 'key2' : 'value2', ... }

players = {
    "ss" : "Correa",
    "2b" : "Altuve",
    "3b" : "Bregman",
    "DH" : "Gattis",
    "0F" : "Springer"
}

print('\nOriginal Dictionary: ' + str(players))

# Querying an item
# Syntax dictionary['key']

second_base = players['2b']
print(second_base)

"""
## Calling an unknown key will throw an error:

second_base = players['sdfsdfsdfsdf']
print(second_base)



## Also, syntax is lower-UPPER/case sensitive

second_base = players['2b']
designatted_hitter = players['dh']
print(designatted_hitter)
"""