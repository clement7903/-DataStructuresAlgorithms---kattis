import sys
from math import ceil

# read the input using an iterator
m, p, n = map(int, input().split())
w = [int(input()) for _ in range(n)]

base_m = m # recording the target baseline
result = 0 # keeps track of the episodes
for wi in w:
  if wi >= m:
    result += 1
  m = ceil(base_m - (wi - m) * p / 100)

print(result)