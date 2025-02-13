# 02-055: Lists -> Ranges (1)

tags = ['python', 'development', 'tutorials', 'code']
print(tags)

# list[start:end]
## Remember, the end position is, always, minus one.

tag_range = tags[1:2] 
print(tag_range)        # ['development']

tag_range = tags[1:3]
print(tag_range)        # ['development', 'tutorials']

tag_range = tags[1:]
print(tag_range)        # ['development', 'tutorials', 'code']

tag_range = tags[:2]    # ['python', 'development']
print(tag_range)

# With negative delimiters
tag_range = tags[:-1]    
print(tag_range)        # ['python', 'development', 'tutorials']

tag_range = tags[-1:]    
print(tag_range)        # ['code']


# Empty delimiters = Full list
tag_range = tags[:]    
print(tag_range)        # ['python', 'development', 'tutorials', 'code']

