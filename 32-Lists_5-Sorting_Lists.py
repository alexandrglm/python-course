# 02-053: Sorting Lists content / sort()

tags = ['Python', 'Development', 'Tutorials', 'Code']
print(tags)


# sort() function
tags.sort()
print(tags) # Returns the list ALPHABETICALLY sorted !


# Reversed sort(reverse=True)
tags.sort(reverse=True)
print(tags) # Returns the list ALPHABETICALLY & REVERSeLY sorted !


# Sorting with Numbers (integers)
totals = [234, 1, 534 , 2345]
print(totals)   # [234, 1, 534 , 2345]

totals.sort()
print(totals)   # [1, 234, 534, 2345]

totals.sort(reverse=True)
print(totals)   # [2345, 534, 234, 1]
