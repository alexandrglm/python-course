# 02 - 037: Checking what represents a String /  .isAlpha() .isNumeric()

# Main use case: 
##  A query over a database which needs to ensure the string represents an Integer or not 

### TIP
### .isalpha() can result in a false positive so that better use .isnumeric()
### var = 'Hi sir' ... Is it Alpha? NO! the blank space IS NOT an alphanumeric character.
    

api_data = '5'
greeting = 'Hi'

print(api_data.isalpha())
print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isnumeric())