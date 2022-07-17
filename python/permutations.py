from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# repeat permutations
from itertools import product
data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)