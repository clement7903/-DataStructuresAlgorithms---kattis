# edge (u, v) ==> v depends on u

import sys
sys.setrecursionlimit(1_000_000) # avoid recursion
# inputs = sys.stdin.readlines()

from collections import defaultdict
n = int(input())
AL = defaultdict(list)

for _ in range(n):
  line = input().split()
  file = line[0][:-1] # retrieve f, take out :
  for j in range(1, len(line)):
    dep = line[j]
    # edge from deps to file
    AL[dep].append(file)

# topological sort ==> use dfs
vis = set()
toposort = []

def dfs(u):
  vis.add(u)
  for v in AL[u]:
    if v in vis:
      continue
    dfs(v)
  toposort.append(u)

dfs(input())
print(*reversed(toposort), sep='\n')