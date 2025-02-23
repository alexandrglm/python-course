# 03-085: While loops, intro


# Example 1:    print a range list

nums = list(range(1,100))

print(nums)


# Example 2:    For...in, print a range list

nums = list(range(1,11))
for num in nums:
    print(num)



# Example 3:    While there are numbers, pop and print allz

nums = list(range(1,100000))

while len(nums) > 0:
    print(nums.pop())

print(nums)


# Example 4: While, with sentinel value as an specific value

def guessing_name():
    while True:
        print('What\'s your guess?')
        guess = input()

        if guess == '37':
            print('You\'ve correctly guessed it!')
            return False
        else:
            print(f'No, the number {guess} isn\'t the answer, try again!')

guessing_name()



# Coding Exercise

"""
Coding Exercise

In the below starter code, place 4 dog names (elements) of your choice in the dog_house list. Then write a while loop that iterates through the dog_house list and prints each dogs name. An iterator variable named "counter" must be set, and must have an initial value of 0.

Hint: An iterator value (also sometimes called a sentinel value) is a value that exists outside of your loop, and that you update or otherwise keep track of each time you loop, so that your while loop knows when to end.

Example:
iterator_value = 0
while iterator_value < 10:
    print("Keep looping...")
    iterator_value += 1

"""


# Option 1

def loop_using_while():
    dog_house = ['a', 'b', 'c', 'd']
    counter = 0
    while counter < 4:
        print(dog_house[counter])
        counter += 1

    return [dog_house, counter]

loop_using_while()

## Option 2
def loop_using_while():
    dog_house = ['a', 'b', 'c', 'd']
    counter = 0
    while counter < 4:
        print(dog_house.copy()[counter])
        counter += 1

    return [dog_house, counter]

loop_using_while()

## Option 3 .pop()
def loop_using_while():
    dog_house = ['a', 'b', 'c', 'd']
    counter = 0
    while counter < 4:
        print(dog_house.pop()[counter])
        counter += 1

    return [dog_house, counter]

loop_using_while()