arr = [i for i in range(20) if i % 2 == 1]

# 2-Dimension array Initialize
n = 5
m = 5
arr = [[0] * m for _ in range(n)]
# wrong example
arr = [[0] * m] * n