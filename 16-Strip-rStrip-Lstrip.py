# 02 - 034: Strip, Rstrip, Lstrip functions

# Main use case: Reformatting Raw data
## Strip functions allows to remove blanks/spaces at entire string and/or on the right-left

### .strip()

url = '   https://google.com   '

print(url.strip())

# More use cases:
## Shorting the string as needed

### From the Left - .lstrip()

url_2 = 'https://google.com'

print(url_2.strip('https://'))

### From the right - .rstrip()

url_3 = 'https://google.com'

print(url_3.rstrip('.com'))

###########

## Use case: From domain to Company Name

url_4 = 'https://www.google.com'

url_4 = url_4.lstrip('https://www.')
url_4 = url_4.rstrip('.com')
url_4 = url_4.capitalize()

print(url_4)