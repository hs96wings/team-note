from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# repeat combinations
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)