# 02-065: Using .get() to configure fallback values

teams = {
    'astros' : ['Altuve', 'Correa', 'Bregman'], 
    'angels' : ['Trout', 'Pujols'],
    'yankees': ['Judge', 'Stanton'], 
    'red sox': ['Price', 'Betts']
}


featured_team = teams['astros']

print(featured_team)


# featured_team = teams['NONEXISTENT']
# print(feature)

# .get() querying 
# Syntax:   dictionary.get('KEY', 'VALUE')
# thus this method we can query already available AND Non-existent Keys/Values without errors

## Non-existent key/value pairs
featured_team = teams.get('fgdfgdg')
print(featured_team)      # None

featured_team = teams.get('retertert', 'werwerwe') #Non existent key/value pair
print(featured_team)        # This prints The value

## An existan KEY without non-existant value
featured_team = teams.get('yankees', 'non-existant value')
print(featured_team)        # This returns the content from the existant key, ignoring non-existant values




## Already available key/value pairs
featured_team = teams.get('astros')
print(featured_team)        # ['Altuve', 'Correa', 'Bregman']



