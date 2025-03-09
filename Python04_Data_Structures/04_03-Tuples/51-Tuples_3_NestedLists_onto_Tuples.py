# 02-072: Tuples with Nested Lists

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent'
)

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post) 
"""
The tags list is "inserted" (reassigned) to the new Tuple:

('Python Basics', 'Intro-Guide to Python', 'PostContent', ['python', 'coding', 'tutorial'])
"""

# Accesing the second value for the list, which is the last value on this tuple

print(post[-1][1])      # coding