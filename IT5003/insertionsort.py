# time complexity - O(n^2)
from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)

def insertionsort(lst):
  n = len(lst)

  for i in range(1, n):
    X = lst[i] # selects item to be inserted
    j = i-1 # j will be from 0 to n-1
    while j >=0 and X < lst[j]:
      lst[j+1] = lst[j] # shift last element of sorted list to the right
      j-= 1        # checks through the sorted list on the left
      
    lst[j+1] = X
  return lst

print(insertionsort(lst))