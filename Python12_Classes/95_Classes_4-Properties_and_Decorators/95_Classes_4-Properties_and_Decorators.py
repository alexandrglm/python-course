# 03-123: Properties and Decorators

class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self.client} owes: ${self._total}'
    
    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        self._client = client

    
    @property
    def total(self):
        return self._total


google = Invoice('Google', 100)
print(google.client)

google.client = '\nAnother Client'
print(google.client)



# Coding Exercise

class Garage:
    def __init__(self, size):
        #   Protect the size attribute
        self._size = size
        self._cars = []

    # add decorator here
    @property
    def size_getter(self):
        return self._size
  
    def open_door(self):
        return "The door opens"
    