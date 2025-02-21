# 03-081: Loops using Lists, Dictioanaries, Tuples


# Working with Lists

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)



# Working with Tuples

players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
    print(player)



# Working with Dictionaries

players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

for position, player in players.items():
    print(f'Position: {position}, Player: {player}')



## Coding Exercise:
"""
Create a list named my_list with 5 elements. Then loop over the list to print out each element.

def loop_over_list():
    # Write your code here
    
    
    return my_list

"""
# But I like to complicate things, so, the list has to be created automatically with random items:
def loop_over_list():
    
    # Our list is empty
    my_list = []
    
    # We want to add 5 random numbers, but we can't import any modules, so,
    # "randomisation" has to be done manually:
    
    max_range = 5 # We set the max size of our list
    items_included = 99999999999 # Here, we set "how many numbers" will be available to "random" choose
    
    for items in range(max_range):
        """
        Hash, like id() returns the unique identificator, as a hash, so
        we use the modulus operator to get: 
        
        - The rest of dividing every new hash of each item is being recently created but parsed to a string, 
        - (divided by) all the numbers/items can be included.
        
        This give us a random number everytime, that we append to the list
        each times the max_range tells.
        """
        my_list.append(hash(str(items)) % items_included)        
    
    # Finally, the ACE editor tell us to print each item included in our recently created list, so:
    for items in my_list:
        print(items)
    
    return my_list
    
    
loop_over_list()



"""
A lot of attemps, as drafts:



# def loop_over_list():
#     my_list = ['alpha', 'betta', 'gamma', 'delta', 'epsilon']
#     for element in my_list:
#         print(element)
    
    
# loop_over_list()



# import random

# my_list = []

# def loop_over_list():
    

    
#     for element_none in my_list:
#         my_list.append(random.randint())
    
#     for element in my_list:
#         print(element)
        
#     return my_list
    
    
# loop_over_list()



empty_list = []

for empty_element in range(3):
    empty_list.append(range(10))

my_list = empty_list

def loop_over_list():
    for element in my_list:
        print(element)
    
    return my_list
    
loop_over_list()


def loop_over_list():
    
    my_list = []

    size = 5
    possibilities = 100

    print([hash(str(seed)) % possibilities for seed in range(size)])

    for element in my_list:
        print(element)
    
    return my_list
    
loop_over_list()



def loop_over_list():

    my_list = []

    max_range = 5
    items_included = 9999
    
    for items in range(max_range):
        my_list.append(hash(str(items)) % items_included)
    
    
    # my_list = [hash(str(_)) % included for _ in range(max_range):print(_)]
    for items in my_list:
        print(items)

    return my_list

    
loop_over_list()


def loop_over_list():
    my_list = ['alpha', 'betta', 'gamma', 'delta', 'epsilon']
    for element in my_list:
        print(element)
    
    return my_list
    
loop_over_list()
"""