# 03-087: Combining list with for...in

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']


# Merging list
raw_db = [legacy_customers, new_customers]

print(raw_db)           # [['Alice', 'Bob'], ['Tiffany', 'Kristine']]



# Using a for...in

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)
 
print(new_customers)    # ['Tiffany', 'Kristine', 'Alice', 'Bob']

# Coding Exercise
"""

"""
# 1
def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for number in numbers:
        print(number + 1)
    
    
    return result

loop_over_list()

# 2
def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for number in numbers:
        result.append(number + 1)
        print(result)   # This is visually helpful in understanding how the result list increments
            
    
    return result


loop_over_list()