# # # # # lambda function

# # # # x = lambda a : a +10

# # # # print(x(5))

# # # # Usando lambda con strings
# # # ## Además, lambda puede acceder a cualquier variable.

# # # a = "hola que tal"

# # # to_upper = lambda a : a.upper()

# # # print(to_upper(a))


# # # title = 'The Substance'
# # # main_actor = 'Demi Moore'

# # # def picking_a_title():
# # #     picked_film = f'(The film {{title}} is interpreted by {{main_actor}}'
# # #     return picked_film

	
# # # picking_a_title(title, main_actor)
# # #                 )

# # # a = 4 % 2
# # # print(a)
# # from decimal import Decimal
# # import math

# # base = 2
# # exponent = -3

# # print(math.pow(base, exponent))


# lista = ['d', 'a', 'b', 'c']

# lista_sorted = sorted(lista)
# print(lista_sorted)     # ['a', 'b', 'c', 'd']

# new_lista = sorted('bad')
# print(new_lista)        # ['a', 'b', 'd']



#     # lista.sort()
#     # print(lista)    # ['a', 'b', 'c', 'd']

#     # lista.sort(reverse=True)
#     # print(lista)    # ['d', 'c', 'b', 'a']

# tupla = (3, 9, 8, 1)
# sorted_tupla = sorted(tupla)
# print(sorted_tupla)


# number = 37
# number += 1     # Lo mismo que number = number + 1
# print(number)   # 38

# # En reasignación de elementos

# tupla_reasignacion = (1,2,3,4)
# tupla_reasignacion += (5,)
# print(tupla_reasignacion)



# logins = {
# 	'root' : 'mihiuhjkhbuih',
# 	'user1' : 'kasjdaokjdaosd'
# }

# print('The root pwd is: ' + list(logins.values())[0])


# # Sin se el mejor ejemplo, muestra que un diccionario también puede contener listas anidadas, no solo valores
# paletas_colores = {
# 	'dark' : 'black',
# 	'primavera' : ['verde', 'amarillo', 'cyan'],
# 	'ocaso' : ['naranja', 'ocre', 'teja']
# }

# print(paletas_colores)
# print(list(paletas_colores.values())[1][2]) # cyan
# print( list(paletas_colores.values())[0])   # black

"""

num_1 = 12
num_2 = 24

def sum_two_numbers(num_1, num_2):
    total = num_1 + num_2
    return total
    
sum_two_numbers(total)
"""

"""
def a(b,c):
    print(f'{b} {c}')

d = a('Pepito', 'Perez')

def e(f):
    print(f'Hey {f}')

e(d) # None !
"""

"""
def greeting(name, surname):
    def printing():
        return f'{name} {surname}'
    
    print(f'Hello, {printing()}')
        
greeting('Pepito', 'Perez')

def greeting(name):
    def printing():
        return f'Hello, {name}'
    
    print(f'{printing()}')
        
greeting('Jordan')
"""

def greeting(name = 'Guest'):
 print(f'Hi {name}!')
greeting()
greeting('Kristine')