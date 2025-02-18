# 02-068: Lists of Nested Dictionaries

# list = [ { dictionary_1 : { 'key' : 'value }, {dict_2 : { 'key' : 'value' } } ]

teams = [
    {
        'astros' : {
            '2B' : 'Altuve',
            'SS' : 'Correa',
            '3B' : 'Bregman'
        }
    },
    {
        'angels' : {
            '0F' : 'Trout', 
            'DH' : 'Pujols'
        }
    }
]

print('\nA list of nested dicts:\n'f'{teams}') 
# [{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'0F': 'Trout', 'DH': 'Pujols'}}]


# Using Indices[]

print('\nNested dicts. using Indices:\n'f'{teams[0]}') 
# {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}



# .get(), Getting by using Indices[]

angels = teams[1].get('angels', 'Team not found')
print('\nGetting by using Indices:\n'f'{angels}')
# {'0F': 'Trout', 'DH': 'Pujols'}


# Getting by .values()
angels = teams[1].get('angels', 'Team not found')

print('\nGetting the Values:\n'f'{angels.values()}')
# dict_values(['Trout', 'Pujols'])



# Getting LISTED .list() dict .get('key', 'else') .values()

angels = list(teams[1].get('angels', 'Team not found').values())

print('\nGetting LISTED values: \n'f'{angels}')



# Getting A VALUE, not a list nor dictionary, using INDICES on .values()
# list() dict[index of which] .get('key', 'else') .values()[indices]

angels = list(teams[1].get('angels', 'Team not found').values())[1]

print('\nGetting ONE LISTED value: \n'f'{angels}')      
# Pujols