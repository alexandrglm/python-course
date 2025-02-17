# 02-063: Nested Collections into Dictionaries

# A Dictionary can store any kind of data.
# E.g., a List inside a dictionary:

teams = {
    "astros"    : ["Altuve", "Correa", "Bregman"],
    "angels"    : ["Trout", "Pujols"],
    "yankees"   : ["Judge", "Stanton"]
}

print('\n' + str(teams) + '\n')


# Using index RANGES
# Syntax:   dictionary['key'][ start : stop : step]

print(teams['astros'])
print(teams['astros'][:2])      # From key 'astros', start: 0, stop: 2


# Using Indices

print(teams['astros'][2])       # Bregman, the value  as is, without brackets nor quotations.

# Querying key by key

print(teams["astros"])
print(teams["angels"])
print(teams["yankees"])

# Handling Dictionary values onto new vars.

team_astros_as_variable = teams['astros']
print('\n' + 'This "Astros team" list is a variable' + '\n\n' + str(team_astros_as_variable))