# 03-081. Control Structures -> Loops
import random


# for...in

numbers = []

for number in range(10):
    numbers.append(str(random.randint(0, 10000)))

print(numbers)



# while 

numbers_while = []

while len(numbers_while) < 10:
    do: numbers_while.append(str(random.randint(0, 1000)))

print(numbers_while)