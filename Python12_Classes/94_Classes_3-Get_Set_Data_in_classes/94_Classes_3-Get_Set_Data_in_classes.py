# 03-122: Get an Set data in Classes

class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'
    
google = Invoice('Google', 100)

# Getters
print(google.client)
print(google.total)


# Setters

google.client = 'Yahoo'
print(google.client)


# Coding Exercise

"""
We've added an array of cars to our garage.
 All of the vehicles are out for the day, and we need to update the array. 
 Now that you've seen getters and setters, use a setter to update the cars array to reflect all cars being gone. 
 Then, in the get_cars variable, get the cars data from the home object.
"""

# Starter code
class Garage:
    def __init__(self, size):
        self.size = size
        self.cars = ["Ram", "Model 3"]

    def open_door(self):
        return "The door opens"
    
home = Garage(2)
# End of starter code

# Setter goes here
home.size = 0
home.cars = []

get_cars = Garage(0)

