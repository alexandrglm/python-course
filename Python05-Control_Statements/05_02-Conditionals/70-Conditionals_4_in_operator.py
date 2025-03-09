# 03-093: "in" Operator

sentence = 'The quick brown fox jumped over the lazy dog'

word = 'quick'

if word in sentence:
    print(f'The word "{word}" was found in the sentence')
else:
    print('There were no matches found')


# comparisions are case sensitive !

word = 'Dog'

if word in sentence:
    print(f'The word "{word}" was found in the sentence')
else:
    print(f'There were no matches found with "{word}"')



# We can combine with string methdos to perform some input data validation

word = "DOG"

if word.lower() in sentence:
    print(f'The word "{word.lower()}" was found in the sentence')
else:
    print(f'There were no matches found with "{word.lower()}"')



# Using another data type

evens = [ num for num in list(range(1,1000)) if num % 2 == 0 ]
my_list = evens[::17]

choice = input('Make your choice: ')

if choice in evens:
    print(f'The chosen number, {choice}, is listed!')

else:
    print(f'The chosen number, {choice}, is NOT listed')



# CodingExercise

"""
In the below code, fix the condition so that the program prints out "The word is in the sentence".

def value_in_string():
    sentence = 'Python is the best!'
    
    if #YourConditionHere:
      print('The word is in the sentence')
    else:
      print('The word is not in the sentence')
"""

# 1
def value_in_string():
    sentence = 'Python is the best!'
    word = 'BeSt'
    
    if word.lower() == 'best' in sentence:
      print('The word is in the sentence')
    else:
      print('The word is not in the sentence')