# 03-076: Tuples as Dictionaries

# Use cases:
# An e-commerce site, package tracking service.
# Some metadata is included into the Keys.
# 

priority_index = {
    (1, 'premier')  : [1, 34, 12],
    (1, 'mvp')      : [84, 22, 24],
    (2, 'standard') : [93, 81, 3]
}



# Use cases 2:

# List all available Packaging categories:

print( list( priority_index.keys() ) )  # [(1, 'premier'), (1, 'mvp'), (2, 'standard')]



# Show what products are inside a specific package tariff:
## As a list, or original format (must know all dict keys)

print( priority_index[1, 'mvp'] )   # [84, 22, 24]


