# 02 - 036: .split() / Breaking a var. over multiple points

# As .partition(), this can distill data but:
# -: By breaking FROM MULTIPLE (repeated) points.
# -: A LIST will be returned

## Use case: Extracting comma-separated values
### WITH Args.
tags = 'python, coding, programming, development'

list_of_tags = tags.split(', ')

print(list_of_tags) # Returns a string with main LIST format "['a' , 'b' , 'c', 'd']""

### WITHOUT Args.

tags_2 = 'alpha,beta,gamma,delta'

list_of_tags_2 = tags_2.split()

print(list_of_tags_2) # Returns a list, ok, but ALL the tags here ARE the list ['alpha, beta, gamma, delta']



## partition() VS split()

versus_heading = "Python: An Introduction"


print(versus_heading.split()) # Returns: ['Python:', 'An', 'Introduction'] ... LIST
print(versus_heading.partition(': ')) # Returns: ('Python', ': ', 'An Introduction') .... TUPLE







