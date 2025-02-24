# 03-090: Conditionals: if / if else / elif


# If statement

age = 1500

if age < 25:
    print(f'I\'m sorry, you need to be at least 25 years old')




# If - Else statements

age = 1500

if age < 25:
    print(f'I\'m sorry, you need to be at least 25 years old')

else:
    print(f'You are good to go, {age} fits in the range to rent a car')



# Elif statement 

age = 1500
age_2 = 26

if age_2 < 25:
    print(f'I\'m sorry, you need to be at least 25 years old')

elif age_2 > 100:
    print(f'I\'m sorry, {age_2} is too old to rent a car')

else:
    print(f'You are good to go, {age_2} fits in the range to rent a car')



## Coding Exercise
"""
Create a conditional that returns true, using the starting code below.


answer = False

if #WriteYourConditionsHere:
  answer = True

"""

answer = True

# 1
if answer is not True:
    answer = True

# 2
if answer is False:
    answer = True

# 3
if answer == False:
    answer = True
