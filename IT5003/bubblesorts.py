# time complexity - O(n2)
from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)

def bubblesort(lst):
  n = len(lst)
  
  # for each element
  for i in range(n-1):
    # look at the pairs
    for j in range(n-1-i): # Largest item would be at the end of array after every iteration, ignore last pair
      if (lst[j] > lst[j+1]):
        lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)

def optimizedbubblesort(lst):
  n = len(lst)
  swap = False
  
  # for each element
  for i in range(n-1):
    # look at the pairs
    for j in range(n-1-i): # Largest item would be at the end of array after every iteration, ignore last pair
      if (lst[j] > lst[j+1]):
        swap = True
        lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)
    if not swap: # breaks out because there is no swapping taking place aka. list is sorted
      break
      
''' Code for testing '''
# print(bubblesort(lst))
print(optimizedbubblesort(lst))