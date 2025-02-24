# 03-095: Stretching a list

"""
remove_first_and_last(list_to_clean)

html_content = ['<h1>', 'Some Content', '</h1>']

remove_first_and_last(html)
=> 'some content'

html_2 = ['<h1>', 'Some Content', 'more content', '</h1>']
=> ['some content', 'more content']
"""
# ATTEMPT 1

# a simple solution, case "<xx>" then remove
# This removes tags if specified manually into while

html_2 = ['<h1>', 'Some Content', 'more content', '</h1>']

tags = ['<h1>', '</h1', '<h2>', '</h2>', '<h3>', '</h3>', '<h4>', '</h4>', '<h5>', '</h5>', '<h6>', '</h6>']

def cleaning(html_2):

    iter = 0
     
    while '<h1>' in html_2 and '</h1>'  in html_2:
        html_2.remove('<h1>')
        html_2.remove('</h1>')
    for each in html_2:
        iter += 1
        print(f'Scrapped Content #{iter} : {each}')    

cleaning(html_2)




# ATTEMTP 2
# This

html_3 = ['<h1>', 'Some Content', 'more content', '</h1>', '<h3>', 'Another subheading', '</h3>']

tags = ['<h1>', '</h1>', '<h2>', '</h2>', '<h3>', '</h3>', '<h4>', '</h4>', '<h5>', '</h5>', '<h6>', '</h6>']

def maxi_cleaner(html_scrapped):
    counter = 0

    html_scrapped = [ element for element in html_scrapped if element not in tags ]
    
    for each in html_scrapped:
        counter +=1
        print(f'Extracted Content #{counter} :', each )


maxi_cleaner(html_3)




# ATTEMPT 3, improving the RegExps

html_4 = [
    '<h1>', 'Some Content', 'more content', '</h1>', 
    '<h3>', 'Another subheading', '</h3>',
    '<h4>', 'More content', '</h4>',
    '<h6>', 'And much more', 'Even much more', '</h4>'
    ]

def maxi_cleaner_regexp(html_scrapped_2):
   
    counter = 0

    tags = [f'<h{heading}>' for heading in range(1,7)] + [f'</h{heading}>' for heading in range(1,7)]

    html_scrapped_2 = [ element for element in html_scrapped_2 if element not in tags ]
    
    for each in html_scrapped_2:
        counter +=1
        print(f'Attempt # content extracted:  #{counter} :', each )


maxi_cleaner_regexp(html_4)