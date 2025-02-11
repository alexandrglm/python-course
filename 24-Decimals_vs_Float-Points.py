# 02-044: Decimals / Float-Points

from decimal import Decimal

## As floats
product_cost = 88.40
comission_rate = 0.08
qty = 450

product_cost += ( comission_rate * product_cost ) # Rapidly calculating the product cost plus the comission rate for the salesman by using the assignment add. operator
# print('As Floats: ' + str(product_cost * qty) ) # 42962.4

## As decimals
product_cost = Decimal(88.40)
comission_rate = Decimal(0.08)
qty = 450 

product_cost += ( comission_rate * product_cost )
print('As Decimals: ' + str(product_cost * qty) ) # 42962.40000000000282883716451


## Decimals passed as Strings

a = 10 / 3
b = Decimal(10) / Decimal(3)
c = Decimal('10') / Decimal('3')
d = Decimal(10) / Decimal('3')
e = Decimal('10') / Decimal(3)
print(a) # 3.3333333333333335
print(b) # 3.333333333333333333333333333
print(c) # 3.333333333333333333333333333
print(d) # 3.333333333333333333333333333
print(e) # 3.333333333333333333333333333