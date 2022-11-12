# Data Structure: using graphs
# marketability = popularity - success

from collections import defaultdict

N, M = map(int, input().split())
AL = defaultdict(list) # dictionary with default value to be an empty list

for _ in range(M):
  person1, person2 = map(int, input().split())
  AL[person1].append(person2)
  AL[person2].append(person1)

for i in range(1, N+1):
  print(len(AL[i]) - i, end = ' ')
print()

# method 2
# we dont need to care about neighbours, only need the number of friends

import sys

inputs = iter(sys.stdin.readlines())
N, M = map(int, next(inputs).split())

degree = [0] * (N+1) # use 1 index

for _ in range(M):
  print(degree[i] - i, end=' ')
print()