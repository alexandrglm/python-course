# 03-134: Exercise - "Building a Pretty Nice method"

## EXERCISE
# Desired callbacks
# pretty_price(3.20, 99) > 3.99
# prety_price(3.20, 0.99) > 3.99

# Desired Output
# 3.21
# 3.97


# ATTEMPT #1

# Even it's not exactly exactly what exercise should be,
# this attempt tries to joint last guides' learnings

import math

class PrettyPrice:
    
    def __init__(self, gross_price, input_type):
        self.gross_price = gross_price
        self.input_type = input_type

    def prettify(self):
        base = math.floor(self.gross_price)
        
        if isinstance(self.input_type, int):
            decimals /= 100
            prettified_price = base + decimals
            return f'Prettified price, from {self.gross_price}, is:  {float(prettified_price)} !'

        else:

            prettified_price = base + 0.99
            return f'Prettified price, from {self.gross_price}, is:  {prettified_price} !'



price = float(input('Price to be prettfied? :  '))
input_type = input('Choose your rounding up method (0.xx / xx) :')

prettified_price = PrettyPrice(price, input_type)
print(prettified_price.prettify())
