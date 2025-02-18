# 02-066: View objects in Dictionaries

players = {
    "ss" : "Correa",
    "2b" : "Altuve",
    "3b" : "Bregman",
    "DH" : "Gattis",
    "OF" : "Springer",
}

teams = {
    "astros" : ["Altuve", "Correa", "Bregman"],
    "angels" : ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"],
}


# .keys() - Showing a key list

print(players.keys())       # dict_keys(['ss', '2b', '3b', 'DH', 'OF'])


# .values() - Showing the values list

print(players.values())     # dict_values(['Correa', 'Altuve', 'Bregman', 'Gattis', 'Springer'])


# .items() - Key, Value list in a list into a tuple
print(players.items())      # dict_items([('ss', 'Correa'), ('2b', 'Altuve'), ('3b', 'Bregman'), ('DH', 'Gattis'), ('OF', 'Springer')])


# .values()[] - EMPTY INDICES NOT SUPPORTED
#print(players.values()[]) # !



# .list +  .values() + [indices] - Yep!
# Syntax:  ( .list( dictionary.values()  ) [index] )

print(list(players.values())[1])    # Altuve, the second item, as expected


# .copy()

player_names = list(players.copy().values())

print(player_names)


#########################################
# Let's work the same with the teams    #
#########################################
print('\n' + 'Teams: ' + '\n' + str(teams) + '\n')

team_groupings = teams.items()

print(team_groupings)

# Length
print(len(team_groupings))      # 4 items!


team_groupings = teams.items()
print(list(team_groupings))

"""
[
('astros', ['Altuve', 'Correa', 'Bregman']),
('angels', ['Trout', 'Pujols']),
('yankees', ['Judge', 'Stanton']),
('red sox', ['Price', 'Betts'])
]
"""

# list() using indices for key/values
# Syntax: [a][b][c]
print('\n\n')

print(list(team_groupings)[1][1])   # ['Trout', 'Pujols']

print(list(team_groupings)[1][1][0])   # Trout
print(list(team_groupings)[1][1][1])   # Pujols
