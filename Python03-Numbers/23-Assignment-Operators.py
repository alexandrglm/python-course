# 02-043. Assignment Operators
# the syntax for assignment operators is that it is nearly identical to a standard type of operator.

total = 100

total = total + 10  # 110
total += 10         # 120
total -= 10         # 110
total *= 2          # 220
total /= 10         # 22
total //= 10        # 2
total **= 2         # 4
total %= 2          # 0

product_two = 120
product_three = 10

total += product_two    # 120
total += product_three  # 130

print(total)