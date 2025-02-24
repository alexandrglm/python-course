# 03-084: Looping into Ranges

# range()
# Syntax: range(start, stop, step)
# Ranges work similar to slicing, the STOP is off by one value!

for number in range(1,10):
    print(number)       # 1 2 3 4 5 6 7 8 9



# Ranges work similar to slicing, the STOP is off by one value!
for number in range(1,11):
    print(number)       # 1 2 3 4 5 6 7 8 9 and .. 10 !


# Stepping

for number in range(1,11, 2):
    print(number)       # 1 3 5 7 9

for number in range(1,11, 3):
    print(number)       # 1 4 7 10