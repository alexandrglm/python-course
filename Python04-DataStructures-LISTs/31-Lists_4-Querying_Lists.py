# 02-052: Querying lists / len() - [-negative index] - index()

tags = ['python', 'development', 'tutorials', 'code']

# len() function
number_of_tags = len(tags) # REMEMBER, len() is NOT zero-based.
print(number_of_tags)   # 4 - The real items on a list BUT not zero-based.

# Negative index
last_items = tags[-1]   # Negative index used
print(last_items)       # 


# index()
index_of_last_item_with_ITEM = tags.index('python')
index_of_last_item_with_VARs = tags.index(last_items)

print(index_of_last_item_with_ITEM) # 0 - The index position for 'python' on the list
print(index_of_last_item_with_VARs) # 3 - Variables can be used here

