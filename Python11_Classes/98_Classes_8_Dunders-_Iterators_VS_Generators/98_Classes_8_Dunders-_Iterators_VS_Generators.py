# 03-127: Dunder __iter__, __next__ VS iter() next() Generators

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

class InfiniteLineup:

    def __init__(self, players):
        self.players = players

    def lineup(self):

        lineup_max = len(self.players)
        idx = 0

        while True:

            if idx < lineup_max:
                yield self.players[idx]

            else:

                idx = 0
                yield self.players[idx]

            idx += 1


    def __repr__(self):
            return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"




full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()


print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))


print(repr(astros_lineup))
print(str(astros_lineup))