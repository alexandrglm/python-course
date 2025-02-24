# 03-094: Compound Conditionals: "and" / "or"

# 'and' operator

username = 'jonsnow'
mail = 'jon@snow.com'
password = 'thepassword'



if username == 'jonsnow' and password == 'thepassword':
    print('Granted access.')
else:
    print('Access\'s NOT granted.')


# 

username_2 = 'pepe'
mail_2 = 'pe@pe.com'
password_2 = 'thepassword2'

if username_2 == 'jonsnow' and password_2 == 'thepassword':
    print('Granted access.')
else:
    print('Access\'s NOT granted.')
 


 # Third Conditions
 # or, and
 # It can be used to allow one OR another

user_3 = ''                 # Empty value
mail_3 = 'mail@mail.com'    # 
pass_3 = 'pwd3'

if (user_3 == 'user3' or mail_3 == 'mail@mail.com') and pass_3 == 'pwd3':
    print('Granted access')
else:
    print('Access NOT granted')




user_3 = ''                 # Empty value
mail_3 = 'kjahsdjkahsdkl'   # A different value than the expected
pass_3 = 'pwd3'

if (user_3 == 'user3' or mail_3 == 'mail@mail.com') and pass_3 == 'pwd3':
    print('Granted access')
else:
    print('Access NOT granted')


user_3 = ''                 # Empty value
mail_3 = 'mail@mail.com'    # An accepted value
pass_3 = 'asdasdasdasd'     # AND with a different value

if (user_3 == 'user3' or mail_3 == 'mail@mail.com') and pass_3 == 'pwd3':
    print('Granted access')
else:
    print('Access NOT granted')




# AND NOT

logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('You can access the Admin dashboard')
else:
    print('You can only access the standard dashboard')


logged_in = True
standard_user = False

if logged_in and not standard_user:
    print('You can access the Admin dashboard')
else:
    print('You can only access the standard dashboard')



# CodingExercise



number = 33

def compound_conditional(number):
    if number > 0 and number <= 100:
        print("Success!")
    else:
        print("Failure...")

compound_conditional(number)