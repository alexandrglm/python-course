# 03-132: REGEX-1 -> Reading/Writing files

# open() / write() / close()

file_builder = open('logger.txt', 'w+')

file_builder.write('Hey, this is a line in the file\n')

file_builder.close()


# Let's fun with file operations and some logic

## 1
file_builder = open('logger.txt', 'w+')

for i in range(1,11):
    file_builder.write(f'{i}: Hey, I\'m a looped line!\n')

file_builder.close()



## 2
file_builder = open("logger.txt", "w+")

for i in range(100):
 file_builder.write(f"I'm on line {i + 1}\n")

# file_builder.write("Hey, I'm in a file!")

file_builder.close()

"""
## Handling files with os

import os

new_folder = os.mkdir('new_subfolder')

list_folder = os.listdir()

change_back_dir = os.chdir('..')
# change_last_dir = os.chdir('-')

file_mv = os.rename('old_file', 'new_file')

remove_file = os.remove('logger.txt')

remove_folder = os.rmdir('new_subfolder')

folder_to_check = 'new_subfolder'
does_the_folder_exist = os.path.exists(folder_to_check)

if does_the_folder_exist is True:
    print('it exists!')
else:
    print('It does not exist') 

get_info_from_file = os.stat('test_file.md')
"""
