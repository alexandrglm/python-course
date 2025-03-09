# 03-115: 'Requests' module, API communications

import requests
import pprint


# Part 1: Simple .get() using requests

r = requests.get('https://dummyjson.com/posts')

print(r.json())


# Part 2 - pprint - From JSON to a more comprehensible data preview

r = requests.get('https://dummyjson.com/posts')

r.json()

pprint.pprint(r.json()['posts'][3])
pprint.pprint(r.json()['posts'][3]['tags'])


