# 03-128: Class VS Instance Attributes

# Recalling ...
# 1: Defining Instance Attributes

class Website:
    
    def __init__(self, title, heading):
        self.title = title
        self.heading = heading


# Creating Instances, and accessing Attributes

ws1 = Website('My First Website', '<h1>My first heading</h1>')

ws2 = Website('The Second webpage', '<h1>My second heading</h1>')


# The attributes (Here, title) **exist independently** for each object.
print(ws1.title, ws1.heading)
print(ws2.title, ws2.heading)



# __dict__ -> Inspecting Instance Attributes

print(ws1.__dict__)     # {'title': 'My First Website', 'heading': '<h1>My first heading</h1>'}
print(ws2.__dict__)


#####################

# 2. Class Attributes

class DifferentWebsites:
    
    # All instances will share this CLASS ATTRIBUTE
    title = 'My Class Title'

    def __init__(self, heading):
        self.heading = heading

dw1 = DifferentWebsites('<h1>New Heading 1</h1>')
dw2 = DifferentWebsites('<h2>Another heading</h2>')

print(dw1.title)
print(dw1.heading)

print(dw2.title)
print(dw2.heading)

