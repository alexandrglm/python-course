# 03-106: FizzBuzz exercise

"""
Write a program that prints the numbers from 1 t 100.
But, for multiples of 3, print 'Fizz'.
For multiples of 5, print 'Buzz'.
For numbers that are multiples of both, print "FizzBuzz"
"""

# 1st approach

numbers = list(range(1,101))
print(numbers)

for num in range(1,101):
    if (num % 3 == 0) and (num % 5 == 0):
        print('FizzBuzz') 
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)



# 2nd Approach: Implementing logic as a function

def Fizz_Buzz():

    print('\nWelcome to the Fizz-Buzz exercise!\n')
    start = int(input("Please, Select the start number: "))
    stop = int(input("Please, select the stop number: "))

    for num in range(start, stop + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz') 
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

Fizz_Buzz()