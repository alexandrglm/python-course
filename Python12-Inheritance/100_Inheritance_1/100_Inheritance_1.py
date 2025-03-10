# 03-129: Inheritance


# Defining a Parent Class/Base Class
## Creating a user class

class User:

    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):

        return f'Hi, {self.first_name} {self.last_name}!'
        
# Defining a Child Class/Derived Class
## Creating an Admin class

class AdminUser(User):      # class ChildClass(ParentClass)

    def active_user(self):
        return '500'
    

# Creating Instances from both classes

pepe = AdminUser('pepe@mail.com', 'Pepe', 'Perez')
juan = User('juan@juan.com', 'Juan', 'Juarez')

print(pepe.active_user())
print(pepe.greeting())

print(juan.greeting())
# print(juan.active_user())     # Cannot be called, error active_user for juan is not defined


    

