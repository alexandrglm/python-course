# 02-045: Converting between Floats, Decimals, Complex numbers

from decimal import Decimal


product_cost = 88.80
comission_rate = 0.08
qty = 450

# Integer syntax:   int(number)
print(int(product_cost)) # 88 (Losing decimals)

# Float syntax:     float(number)
print(float(qty)) # 450.0 (Adding decimals)

# Decimal syntax:   Decimal(number)
print(Decimal(product_cost)) # 88.7999999999999971578290569595992565155029296875

# Complex syntax:   complex(number)
print(complex(comission_rate)) # (0.08+0j)