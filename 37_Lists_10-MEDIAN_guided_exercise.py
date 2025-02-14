# 02 - 058: Python - Lists, Finding statical MEDIAN in a list
# Guided exercise

import math

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]
"""
sorted_list = sorted(sale_prices)

num_of_sales = len(sorted_list)     # List length (non-zero result)

first_sale_items = sorted_list[ None : math.floor(num_of_sales / 2) ]

last_sale_items_draft = sorted_list[ (math.floor(num_of_sales / 2) + 1) : None ] # A non-visual way to always catch the last sorted items without the MEDIAN value

last_sale_items = sorted_list[ -math.floor(num_of_sales / 2) : None] # The same but the proper, using NEGATIVE Index!

median = sorted_list [ math.floor(num_of_sales / 2) : (math.floor(num_of_sales / 2) + 1)  ]
"""

# Cleaning up the code
sorted_list = sorted(sale_prices)

num_of_sales = len(sorted_list)

half_slice = math.floor(num_of_sales / 2)

first_sale_items = sorted_list[ : half_slice ]
last_sale_items = sorted_list[ -(half_slice): ]

median = sorted_list[ half_slice : (half_slice + 1) ]

print(sorted_list)
print(num_of_sales)
print(first_sale_items)
# print(last_sale_items_draft)
print(last_sale_items)
print(median)