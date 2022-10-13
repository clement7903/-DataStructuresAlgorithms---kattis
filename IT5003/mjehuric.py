lst = list(map(int, input().split()))

# bubble sort
def sortlist(lst):
  if lst[0] > lst[1]:
    lst[0], lst[1] = lst[1], lst[0]
    print(*lst)
  if lst[1] > lst[2]:
    lst[1], lst[2] = lst[2], lst[1]
    print(*lst)
  if lst[2] > lst[3]:
    lst[2], lst[3] = lst[3], lst[2]
    print(*lst)
  if lst[3] > lst[4]:
    lst[4], lst[3] = lst[3], lst[4]
    print(*lst)

while lst != [1, 2, 3, 4, 5]:
  sortlist(lst)