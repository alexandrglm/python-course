# 02-074: Removing items from a tuple

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent',
    'published'
)
print('\nOriginal Tuple:  \n'f'{post}\n')



# Removing items from the end [-1]

post = post[ : -1]
print(post)



# Removing items from the end [-2]
post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent',
    'published'
)

post = post[ : -2]
print(post)



# Removing elements from beginning

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent',
    'published'
)

post = post[1 : ]
print(post)



# Removing specific element (messy/not recomended !!! )
# .remove() and list(), and tuple()

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent',
    'published'
)

post = list(post)

post.remove('published')
post = tuple(post)

print(post)


