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
