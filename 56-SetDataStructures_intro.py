# 03-078 Python - Set Data Structures intro

# Syntax is near from other data structures syntax, as list or dictionaries.
# Syntax:   name = { 'item1', 'item2, ... }

## Creating a set

empty_dict_tags = {}    # This is not a set, a dict instead.
empty_set_tags = set()  # Always use set()

print(type(empty_dict_tags))    # <class 'dict'>
print(type(empty_set_tags))     # <class 'set'>


set_tags = {
    'python',
    'coding',
    'tutorials',
}

tags = set_tags
print(tags)     # {'python', 'coding', 'tutorials'}

# Set characteristiques:

## 1 - Unique Elements property 
### Duplicates are ignored

tags.add('coding')
print(tags)     # {'python', 'coding', 'tutorials'}


## 2 - Unorderded elements property  - Unsubscribable
""""
print(tags[0]) # Index cannot be used, there's no indices in a Set
"""
### Instead of trying to index a set, use IN:

query_one = 'python' in tags
print(query_one)    # True

query_two = 'This element is not contained in the set' in tags
print(query_two)    # False



## 3 - A set is MUTABLE - Its elements MUST be IMMUTABLE
# Valid set with immutable elements

valid_set = {1, 2, "python", (4, 5)}    # As it contains IMMUTABLE elements

# Invalid set with mutable elements (will raise an error)
"""
NOPE!
invalid_set = {1, 2, [3, 4]}  #  Lists are mutable
"""


## 4 - Hash-based storage

import time

big_list = list(range(1000000))
big_set = set(big_list)

start = time.time()
print(99999 in big_list)
print('List search time:  ', time.time() - start)

start = time.time()
print(99999 in big_set)
print('Set search time:  ', time.time() - start)



# Set methods

## .add() - Items has to be added ONE BY ONE, only one argument
tags.add('Added tag')
tags.add('Another one')
tags.add('Also another one')
print(tags)

# .remove() - Raises an error if 'coding' is not present
tags.remove('Added tag')
print(tags)

# .discard() - Removes a tag safely if it's not in the set
tags.discard('This tags does not exist')
tags.discard('Another one')
print(tags)

# .pop() - Arbitrary element will be popped!
## THIS DOES NOT WORK WITH INTEGERS, ONLY STRINGS !

lottery_participants = {'Juan', 'Pepe', 'John', 'Menganito'}
print('\n\nA lottery for ten participants :\n', lottery_participants)
print('\nWinner: ', lottery_participants.pop())
print('\nNot Winner: ', sorted(lottery_participants))


# Set Opertations

set_1 = {'Alpha', 'Beta', 'Gamma'}
set_2 = {'Red', 'Green', 'Blue'}
set_3 = {'Gamma', 'Delta', 'Epsilon'}


## union() - Merges sets, with no order
union_sets = set_1.union(set_2)
print(union_sets)

## intersection() - Finds repeated value, the sets' intersection
intersection_sets = set_1.intersection(set_3)
print(intersection_sets)


## difference() - Finds the unique values from one set over another set
difference_sets = set_1.difference(set_3)
difference_sets_2 = set_3.difference(set_1)
print(difference_sets)
print(difference_sets_2)


# - frozenset() . The immutability, but with conditions
## It always retuns an initial 'frozenset' wrapped into parenthesis as is a function.

immutable_tags = frozenset(tags)

#immutable_tags.add('Nope!')    # This will raise an error due to immutability
tags.add('Yep')

print(tags)
print(immutable_tags)   # frozenset({'python', 'coding', 'tutorials'})





