# 03-091: Ternary operator (elvis)

# Syntax
# value_if_true if condition else value_if_false


# If/Else regular statements

role = 'admin'

if role == 'admin':
    auth = 'is allowed.'

else:
    auth = 'is NOT allowed'

print(f'The user "{role}"', auth)



# Using Ternary operator

role = 'admin'
auth = 'is allowed.' if role == 'admin' else 'is NOT allowed.'

print(f'The user "{role}"', auth)


# Coding Exercise

"""
Write a ternary operator that sets "language_check" to True if "language" is set as "python", and sets it to False if it's not.

language = "python"

language_check = # Write your code here
"""

language = "python"

language_check = True if language == "python" else False
# language_check = True if language is "python" else False
# language_check = False if language is not "python" else True

print(language_check)

