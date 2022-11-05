# use set intersection
user_input = list(map(int, input().split()))
n, m = user_input[0], user_input[1]

d = set(input().split())

for _ in range(n-1): #O(mn)
  current_list = set(input().split())
  appear_in_all = d.intersection(current_list) # O(min(len(appear_in_all), len(current_list)))
print(len(appear_in_all))
for item in sorted(appear_in_all):
  print(item)



