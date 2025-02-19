# 02-071: Reasigning elements to a Tuple

post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent'
)

# Is this a Tuple?
sum = (2 * 2) + 5   # Nope! A tuple always has `,` commas!


# Reassigning values on Tuples
## By Joining TWO TUPLES into ONE, then, RENAMING the Tuple to the original!

post = post + ('published',)

title, subtitle, content, status = post

print('\n'f'{title}\n{subtitle}\n{content}\n\nStatus: {status}')


post = (
    'Python Basics', 
    'Intro-Guide to Python',
    'PostContent'


)

# Reassingment Operator and id() method

print('\n\nOriginal Tuple: 'f'{post}')
print(id(post)) # 140229832234624
print(id(post)) # Again, 140229832234624

post += ('published',)

print('\n\nReasigned Tuple: 'f'{post}')
print(id(post)) # 140004734724480
