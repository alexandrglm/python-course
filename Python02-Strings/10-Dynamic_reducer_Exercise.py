import operator
from functools import reduce


def dynamic_reduce(collection, op):
    operators = {
        # The dictionary stores data here as further lambda function needs:
        # string : function
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }


    return reduce((lambda final, element : operators[op]( final, element ) ), collection ) 

final_a = dynamic_reduce( [1, 2, 3], '+' )
final_b = dynamic_reduce( [1, 2, 3], '-' )
final_c = dynamic_reduce( [1, 2, 3], '*' )
final_d = dynamic_reduce( [1, 2, 3], '/' )

print(str(final_a) + '\n' + str(final_b) + '\n' + str(final_c) + '\n' + str(final_d) )