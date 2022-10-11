# time complexity - O(n^2)
from random import randint

lst = [randint(1, 100) for _ in range(10)]
print(lst)

def min_selectionsort(lst):
  n = len(lst)
  for i in range(n-1): # O(n)
    min_index = i
    for j in range(i+1, n): # O(n)
      if lst[j] < lst[min_index]:
        min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
  return lst

print(min_selectionsort(lst))