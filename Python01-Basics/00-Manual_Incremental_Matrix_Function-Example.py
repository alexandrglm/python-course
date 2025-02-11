# From Module 02 - 013, previous to Python Part 1

def manualIncrementingMatrix(n):
  matrix = [ [ None for y in range(n) ] for x  in range(n)  ]

  counter = 0

  for idx, el in enumerate(matrix):

    for nested_idx, nested_elel in enumerate(el):
        matrix[idx][nested_idx] = counter + nested_idx

        counter += 1
  
  return matrix
  
print(manualIncrementingMatrix(5))
