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


# More ways to combine lists

# .extend() - Merging both into one directly

users = ['root', 'user1']
pwd = ['rootPass', 'user1Pass']

users.extend(pwd)
print(users)


# Using list comprehesion (The following guide will expand this)

users = ['root', 'user1']
pwd = ['rootPass', 'user1Pass']

users = [user for user in users] + [single_pwd for single_pwd in pwd ]
print(users)




# Coding Exercise
"""
Write a for loop that takes each number from the numbers list, increments it by 1, and adds it to the result list.

def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    # Write your code here
    
    
    return result

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
"""