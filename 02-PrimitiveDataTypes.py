# Booleans
# Numbers
# Strings

# Bytes / Byte Arrays
# Lists
# Tuplas
# Sets
# Dictionaries

## Code Examples
## Using numbers

meal_Complete = True
sub_total = 100
tip = sub_total * 0.20
total = sub_total + tip

# "receipt = "Your total is" + tip" will cause an error -  data type error due to mixing both data types
# so that's why `str` subordinate function needs to be used at VARIABLE time (not at return time)
receipt = "Your total is " + str(total)

print(sub_total)
print(tip)
print(receipt)