# 02-060: Extending a list's items - .extend()

tags = ['python', 'development', 'tutorials', 'code']
print('\nOriginal List:  ' + str(tags))

# Nope !
# Replacing with an index:

tags[-1] = 'Programming (via [index])'
print(tags)

# Nope!
# Extending via .extend()
#tags.extend('Programming (via .extend())')
# print(tags)     # our string has been inserted CHARACTER BY CHARACTER !

# Yep !
# Extending via .extend( [ ] ) !

tags.extend( ['Programming ( via .extend([ ]) )'] )    # Using ( [ ] ) !
print(tags)     # ['python', 'development', 'tutorials', 'Programming (via [index])', 'Programming (via .extend( [ ] ) )']
