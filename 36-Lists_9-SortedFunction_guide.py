# 02-057: Lists - Sorted function (advanced)

sale_price = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3,
]

# Simply sorting

sale_price.sort()
print(sale_price)   # [1, 3, 10, 40, 83, 100, 100, 220, 400]



# .sort() function does not store anything (due to the mentioned immutability)

sorted_list = sale_price.sort()
 print(sorted_list) # None - Anything!



# sorted(list) function

sorted_list = sorted(sale_price)

print(sorted_list)  # new stored value: [1, 3, 10, 40, 83, 100, 100, 220, 400]
print(sale_price)   # immutable value:  [100, 83, 220, 40, 100, 400, 10, 1, 3]



# sorted(list, reverse=True)

sorted_list = sorted(sale_price, reverse=True)

print(sorted_list)  # Sorted, and Reversed: [400, 220, 100, 100, 83, 40, 10, 3, 1]
