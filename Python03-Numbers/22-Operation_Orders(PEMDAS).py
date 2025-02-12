# 02-042 : Mathematical order operations (PEMDAS vs PEDMAS)

"""
P   ->  Parens ()
E   ->  Exponents ^   
M   ->  Multiplications *
D   ->  Divisions / and //
A   ->  Additions +
S   ->  Substractions -

1:  8 + 2 * 5 - (9 + 2) ** 2
2:  8 + 2 * 5 - 11 ** 2
3:  8 + 2 * 5 - 121
4:  8 + 10 - 121
5:  -103

Finally, PEMDAS and PEDMAS always give the SAME result.
"""

calculation = 8 + 2 * 5 - (9 + 2) ** 2


print(calculation)