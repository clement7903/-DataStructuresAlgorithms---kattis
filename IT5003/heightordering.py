P = int(input())
output = []

for _ in range(P):
  user_input = list(map(int, input().split()))
  K = user_input[0]
  lst = user_input[1:]
  counter = 0
  n = len(lst)

  for i in range(1, n): # insertion sort algo
    X = lst[i] # selects item to be inserted
    j = i-1 # j will be from 0 to n-1
    while j >=0 and X < lst[j]:
      lst[j+1] = lst[j] # shift last element of sorted list to the right
      j-= 1        # checks through the sorted list on the left
      counter += 1
      
    lst[j+1] = X

  output.append([K, counter])

for item in output:
  print(item[0], item[1])