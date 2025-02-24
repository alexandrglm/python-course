# 03-095
# This is the guided solution after 72_EXERCISE_Methods_0-Stretching_a_list.py tries

# Goblin theory

nums = [1, 2, 2.5, 2.6, 3, 4]
print('\nA simple list:  ', nums)



# First glob used, floats belong to its root base

one, *two, three, four = [1, 2, 2.5, 2.6, 3, 4]
print('\nRoot 1: ', one)
print('\nRoot 2: ', two)
print('\nRoot 3: ', three)
print('\nRoot 4: ', four)


# ATTEMPT 4: using globs

html_content = ['<h1>', 'Content', 'More Content', '</h1>']

def remove_first_and_last(html_content):

    _, *content, _ = html_content
    counter = 0
    for each in content:
        print(f'\nExtracted content #{counter + 1} : ', each)
        counter += 1
    return content

remove_first_and_last(html_content)




# SOLUTION

def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print('\nSolution: ', remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print('\nSolution: ', remove_first_and_last(other_content_to_clean))

more_content = ['', 'a','b','c','d','e']
print(remove_first_and_last(more_content))


