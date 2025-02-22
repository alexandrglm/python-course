# 03-084: Continue/Break loops

usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa'
]

# Continue

for username in usernames:
    if username == 'cersei':
         print(f'Sorry, {username} is banned!') 
         continue
    else:
         print(f'Acces granted for {username}.')



# Break

usernames_2 = [
     'a',
     'b',
     'c',
     'd'
]

for user2 in usernames_2:
    if user2 == 'd':
          print(f'{user2} was found at index {usernames_2.index(user2)}')
          break
    print(user2)