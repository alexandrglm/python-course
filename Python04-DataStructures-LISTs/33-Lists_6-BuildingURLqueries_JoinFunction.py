# 02-054: Building a URL Query / `.join()`

# https://www.google.com/search?q=python+tutorial

uri = 'https://www.google.com/search?q='        # the uri base
tags = ['python', 'development', 'tutorial']    # Query terms, the keywords used



# .join()
## Syntax: 'what to join'.join(the list)
formatted_tags = '+'.join(tags)
print(formatted_tags)       # python+development+tutorial



# Adding string interpolation to build the complete URI
query_uri = f'{uri}{formatted_tags}'
print(query_uri)    # https://www.google.com/search?q=python+development+tutorial



# '*data*'.join(*list*) can be used in any needed way

formatted_tags = ' '.join(tags)         # Blank spaces, not the common use in URI
query_uri = f'{uri}{formatted_tags}'
print(query_uri)    # https://www.google.com/search?q=python development tutorial

formatted_tags = '-'.join(tags)         # With the minus sign
query_uri = f'{uri}{formatted_tags}'
print(query_uri)    # https://www.google.com/search?q=python-development-tutorial

formatted_tags = '@#~#€¬~'.join(tags)         # With wathever you need
query_uri = f'{uri}{formatted_tags}'
print(query_uri)    # https://www.google.com/search?q=python@#~#€¬~development@#~#€¬~tutorial



