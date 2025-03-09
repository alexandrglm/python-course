# 03-126: Dunder __iter__, __next__ : Iterators

class LineUp:

    def __init__(self, players):
        self.players = players
        self.last_player_index = ( len(self.players) -1 )

    # def __str__(self):
    # def __repr__(self)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    # Continuous iteration as long as how many times have been invoked next(var)
    def __next__(self):
        
        if self.n < self.last_player_index:

            player =  self.get_player(self.n)
            self.n += 1
            return player
        
        elif self.n == self.last_player_index:

            player = self.get_player(self.n)
            self.n = 0
            return player  

astros = [
    '1: Springer',
    '2: Bregman',
    '3: Altuve',
    '4: Correa',
    '5: Reddick',
    '6: Gonzalez',
    '7: McCann',
    '8: Davis',
    '9: Tucker'
]

astros_lineup = LineUp(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
