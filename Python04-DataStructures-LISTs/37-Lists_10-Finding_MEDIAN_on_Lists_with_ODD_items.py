# 02 - 058: Python - Lists, Finding statical MEDIAN in a list

"""
sale_prices = [
    111,
    83,
    220,
    40,
    108,
    400,
    124,
    654,
    101,
    76898786,
    65454,
    16358,
    14412,
    610,
    65752413,
    321324,
    41564352135432134
]
"""
"""
Tools:

- math library
- sorted function
- list slicing
- computations
"""

# Attempt #1
import math
from decimal import Decimal

"""
1. Reordering the list

2. Getting how many items the list is

3, Depending on how many items, look for the median positioned item:
3.1 [Guide reviewed]    Half the item_list numbers
3.2 Assuming the MEDIAN is half_the_item_list AS IS (non-zero LEN + zero-based INDEX = DRAFT! )
3.2 But Round() only works well when the items < 10, so, math.ceil is the options

"""

sale_prices = [-math.inf, Decimal(-0.00000000092165), 0.22, math.inf, Decimal(1.546546546545321645343243423213451354), float(2.99999999999932413432543243299998), math.pi, round(math.log(76)), 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

sorted_prices = sorted(sale_prices) # 1. Reordering the list
print(sorted_prices)

items_length = len(sorted_prices)
print(items_length)

half_length = math.floor(items_length / 2) # round() doesn't work very well ...
print(half_length)

median = sorted_prices[half_length]
print(median)