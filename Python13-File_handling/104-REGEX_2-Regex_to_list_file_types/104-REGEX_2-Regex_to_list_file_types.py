# 03-133: REGEX_2, Importing a file without overwriting its content.

import fnmatch
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print('Text files: , ', file)


list_files()



# Let's introduce more cases, one for each file type:

def list_files():

    for file in os.listdir('./'):
        # Py scripts
        if fnmatch.fnmatch(file, '*.py'):
            print('Python Scripts: ', file)
        
        # TXT files
        if fnmatch.fnmatch(file, '*.txt'):
            print('Txt Files: ', file)

list_files()


# Matching case example
## While it's not mandatory in this example to "from fnmatch import fnmatchcase",
## it's a good practice to import only the needed methods.

neighbours = [
    'Pepito Perez 1A',
    'Juanito Lopez 1B',
    'Menganito Smith 2A',
    'Sandra Bullock 2B'
]

first_floor_neighbours = [ neighbour for neighbour in neighbours if fnmatch.fnmatchcase(neighbour, '*1*')]

print(first_floor_neighbours)   # ['Pepito Perez 1A', 'Juanito Lopez 1B']
