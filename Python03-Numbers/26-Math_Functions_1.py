# 02-046: Math functions (1)

import math

loss = -20.25
product_cost = 89.99

# ABS - Absolute value          Syntax: abs(number)
print(abs(loss)) # 20.25, the absolute value

# math.floor() - Round down    Syntax: math.floor(number)
print(math.floor(product_cost)) # 89, floor-rounded, similar as int() but ...

# math.ceil() - Round up value  Syntax: math.ceil(number)
print(math.ceil(product_cost)) # 90, the ceil-rounded value

# Flooring/Ceiling with NEGATIVE NUMBERS
## Be careful when floor-ing/ceiling:   It returns an Integer.
## Numbers are ... Whole Numbers! ... -3 -2 -1 0 1 2 3 ...

print(math.floor(-5.99)) # -6 - math.floor() is still lowering the value, so -6!
print(math.ceil(-5.99))  # -5 - math.ceiling() is still "uppering" the value, so -5 !


# Nesting math functions:
## abs(math.floor(number))
print(abs(math.floor(loss))) # 21 (Absolute from(Floor of -20.25))

## math.floor(math.ceil(abs(number)))
### (No sense but for understanding how the functions can be nested)
print(math.floor(math.ceil(abs(loss)))) # 21


# round() - Getting to the CLOSEST whole number
product_cost = 89.99        
print(round(product_cost)) # 90

product_cost = 89.12
print(round(product_cost)) # 80


# SquareRoots - math.sqrt()
product_cost = 89.99
print(math.sqrt(product_cost)) # 9.486305919587455



# PowerRoots - math.pow(base, exponent)
print(math.pow(5, 2)) # 25 - 5²
print(math.pow(2, 3)) # 8  - 2³
print(math.pow(2, 6)) # 64 - 2⁶


# base ** exponent VS math.pow(base,exponent)

print(5 ** 2)         # ** returns INTEGERS
print(math.pow(5, 2)) # math.pow returns FLOATS  ... Perfect for large scientific/accurate calculations 


# Extended functions:

## Exponentials     math.exp(exponential)
print(math.exp(2)) # 7.38905609893065

## Simple Logarithm
print(math.log(10)) # 2.302585092994046

## Base10 Logarithm
print(math.log10(100)) # 2.0 (integer)
print(math.log10(1000)) # 3

# Constants

## Pi
print(math.pi) # 3.141592653589793

## Tau
print(math.tau) # 6.283185307179586

## Euler
print(math.e) # 2.718281828459045

## Infinite
print(math.inf) # inf


# Trigonometrics

## Sine
print(math.sin(math.pi / 2)) # 1

## Cosine
print(math.cos(0)) # 1

## Tangent
print(math.pi / 4) # 0.7853981633974483






