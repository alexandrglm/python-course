# 02-070: Tuples, introduction

# Different Data Structures:

## List             [ ]
## Dictionary       { }
## Tuple            ( )

## Mutable:     Lists, Dictionaries
## Immutable:   Tuples


post = ('Python Basics', 'Intro Guide to Python', 'Some Cool Post content')

# Querying index mode:

title = post[0]
sub_heading = post[1]
content = post[2]

print('\nIndex Querying Method: \n\n'f'{title}\n{sub_heading}\n{content}\n\n')


# Unpacking method !

title, sub_heading, content = post

print('\nUnpacking Method: \n\n'f'{title}\n{sub_heading}\n{content}')


# Tupples are IMMUTABLE! Cannot be sorted nor edited nor nothing.

post.sort()

title, sub_heading, content = post
# print(post)