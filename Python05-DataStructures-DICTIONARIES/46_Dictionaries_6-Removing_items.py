# 02-067: Removing Key/value items

teams = {
    "astros" : ["Altuve", "Correa", "Bregman"],
    "angels":  ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"],
}
print('\nOriginal list : \n' + str(teams))


# 'del dict['key'][value Index]
print('\nUsing del\n')
del teams['astros']         # astros entire key
print(teams)

del teams['yankees'][1]     # yankees key, Stanton value
print(teams)

#del teams['asdasdasd']      # A non-existent key will throw an error
#print(teams)


# .get('if', 'else) avoids error at non-existent values
print('\nUsing .get()\n')
print(teams.get('angels', 'No key found for this value'))
print(teams.get('asdasdasd', 'No key found for this value'))



# .pop('key', 'new value for the key)
print('\nUsing .pop()\n')

extracted = teams.pop('astros', 'No key found')

print(teams)        
print(extracted)    # No key found due to .pop() removals

# .pop() with non-existant key

extracted_2 = teams.pop('sasdasd', 'Non.existant value, and the dictionary has NOT been altered')
print(teams)
print(extracted_2)


removed_team = teams.pop('rays', 'No team found by this name')
print(teams)
print(removed_team)


removed_team_2 = teams.pop('yankees', 'No team found by this name')
print(teams)
print(removed_team_2)   # The key exists, so .pop() do its stuff


# .clear() !

teams = {
    "astros" : ["Altuve", "Correa", "Bregman"],
    "angels":  ["Trout", "Pujols"],
    "yankees": ["Judge", "Stanton"],
    "red sox": ["Price", "Betts"],
}

print('\n\nOriginal Dictionary :\n'f'{teams}')
print(teams.clear())
print(teams)            # {}