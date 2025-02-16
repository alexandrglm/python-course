# 02-061: Python Exercise: Building a Weighted Lottery function
"""
import numpy as np

# This freezes the system:
# DEBUG: It creates almost infinite numbers.
def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)

    return np.random.choice(container_list)



other_weights = {
    # minimum 5digits
    f"{number:05d}": max(1, number) for number in range(100000)
}
print(weighted_lottery(other_weights))
"""



# Attempt 2

import numpy as np

def weighted_lottery(weights):

    keys = list(weights.keys())
    values = np.array( list(weights.values()), dtype=np.float64 )

    return np.random.choice( keys, p=values / values.sum() )

other_weights = {
    f"{number:05d}": max(1, number) for number in range(100000)
}

print('El número agraciado del sorteo de hoy es:  ' + str(weighted_lottery(other_weights)))


"""
# Whith colours
other_weights = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
    'purple': 5,
    'orange': 6,
    'pink': 7,
    'brown': 8,
    'black': 9,
    'white': 10,
    'gray': 11,
    'cyan': 12,
    'magenta': 13,
    'lime': 14,
    'teal': 15,
    'indigo': 16,
    'violet': 17,
    'gold': 18,
    'silver': 19,
    'bronze': 20,
}
"""
