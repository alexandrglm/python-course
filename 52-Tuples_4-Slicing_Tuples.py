# 02-073: Slicing Tuples

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent',
    'published'
)

print(post[ : 2])         # ('Python Basics', 'Intro-Guide to Python')

print(post[ 1 : : 2])     # ('Intro-Guide to Python', 'published')