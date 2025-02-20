# 03-077: ZIP Function zip()

# It merges many lists into a set of tuples
## Values MUST be correctly ordered, otherwise merging process will give wrong-unwanted correlations

positions = [
    '2b', '3b', 'ss', 'dh'
]

players = [
    'Altuve', 'Bregman', 'Correa', 'Gattis'
]

scoreboard = zip(positions, players)

print(list(scoreboard)) 
# [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]
# Each key has been merged with their own Values, into new immutable values, tuples.



# Another use case:

character_order = [(1, 'Ryu'), (9,'Honda'), (6, 'ChunLi')]
levels = [{'Power' : 87, 'Magic' : 155 }, {'Power' : 254, 'Magic' : 66 }, {'Power' : 188, 'Magic' : 44 }]
suit_colour = ['White', 'Blue', 'Pink']

merged_values = zip(character_order, levels, suit_colour)
print(list(merged_values))

# This can work with tuples, dictionaries and lists in origin
# Every zip-merged will be into a tuple
"""
[
((1, 'Ryu'), {'Power': 87, 'Magic': 155}, 'White'), 
((9, 'Honda'), {'Power': 254, 'Magic': 66}, 'Blue'), 
((6, 'ChunLi'), {'Power': 188, 'Magic': 44}, 'Pink')]
"""


# More use cases:   Client record

name = ['Pepito', 'Juanito', 'Menganito']
surname = ['Perez', 'Lopez', 'Diez']
id_card = ['73747274A', '0028144FH', 'token:6544df646543241sd6f4778654sdf']
id_type = ['NIF', 'PASSPORT', 'DigitalCert.']
phone = [600123123, 930025741, 699999999]

clients_records = zip(surname, name, id_type, id_card, phone)
print(list(clients_records))


# More use cases:   Building a Dictionary

keys = ['+', '-', '*', '/']
values = ['Adds', 'Subs', 'Muls', 'Divs']

oper_dict = dict(zip(keys, values))
print(oper_dict)    # {'+': 'Adds', '-': 'Subs', '*': 'Muls', '/': 'Divs'}


# More use cases:   Unpacking Data !!! By using zip(*the_data)

scoreboard_zipped = [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]

positions_unzipped, players_unzipped = zip(*scoreboard_zipped)

print(list(positions_unzipped))
print(list(players_unzipped))
