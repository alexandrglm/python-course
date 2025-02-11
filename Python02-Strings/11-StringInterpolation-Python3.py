# name = 'kristine'
# greeting = f'This is my {{bracket}} post'
# print(greeting)

name1 = 'Pepito'
name2 = 'José'
place1 = 'mi casa'
place1reverse = 'su casa'

# sentence = f"""
# {{José}}: - "Hola Don {name1}"
# {{Pepito}}  - "Hola Don {name2}"
# {{José}}  - "¿Pasó Vd. por {place1}?"
# {{Pepito}}  - "¿Por {place1reverse} yo pasé?"
# """

# print(sentence)

first_name = '{Don}}'
last_name = '{Pepito}'

def function(first_name, last_name):
    greeting = f'Hello, {{first_name}} {{last_name}}'
    
    
    return greeting