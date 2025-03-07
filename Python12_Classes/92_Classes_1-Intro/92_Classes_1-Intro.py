# 031-120: Classes, intro

# New pipenv has been created

# A new class is created at invoice.py

"""
class Invoice:
    def greeting():
        return 'Hi there'"
"""

# Then, a class instantiation is done

"""
inv_one = Invoice()
print(inv_one)"
"""

# If we call the class an error is returned
# NOTICE: Methods inside a class must take `self` as their first argument

"""
class Invoice:
    def greeting(self):
        return 'Hi there'"
"""


# CodingExercise

"""
Create a class named Garage. Add a method to the Garage class named open_door that returns a string (EX: "The door opens").
Finally, instantiate a new object named home. You do not need to print anything.
"""

class Garage:
    def open_door(self):
        return 'The door is opening...'
    
home = Garage()