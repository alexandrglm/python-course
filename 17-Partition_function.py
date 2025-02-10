# 02 - 035: .partition() function

# When you want a subsection of the data gets passed, .partition() breaks wathever you pass in.
# It ONLY works with THREE elements.
# It creates new a TUPLE of these THREE variables when used.


## Main use case: 
### Distilling/Cleaning up garbage data from a variable

heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')
"""
New tuple with 3 vars have been created here:
- header
- _ : Underscore is the mainly adopted way to label the garbage data.
-subheader
"""

print(header)
print(subheader)

# [!] .partition() will ONLY break on the FIRST match found:

heading_2 = 'Title: The Substance - Main Actress: Demi Moore'

title_category, _ , title = heading_2.partition(': ')

print(title) # Break occurs at the FIRST ': '



## More examples:
### Storing the number

raw_data = 'Support: +18001112233 Free call'
_, number, _ = raw_data.partition('+18001112233')
print(number)

### Storing an username

raw_data2 = 'Username: admin'
title, _, username = raw_data2.partition(': ')
print(username)

