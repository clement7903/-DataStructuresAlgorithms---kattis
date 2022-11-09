# Data Structure: Hashmap/Python Dict

from collections import defaultdict
num_of_trips = int(input())

d = defaultdict(lambda : [])
for _ in range(num_of_trips):
  country_year = input().split()
  country, year = country_year[0], int(country_year[1])
  d[country].append(year)

for k, v in d.items():
  v.sort()

num_of_queries = int(input())
output = []
for _ in range(num_of_queries):
  country_rank = input().split()
  country, rank = country_rank[0], int(country_rank[1])-1
  output.append(d[country][rank])

for item in output:
  print(item)