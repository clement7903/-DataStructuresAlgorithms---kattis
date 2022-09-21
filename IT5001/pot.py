total_num = int(input())
total = 0

def power(num, pow):
  return num ** pow

for i in range(total_num):
  num = input()
  actual_num = int(num[:-1])
  pow = int(num[-1])
  total += power(actual_num,pow)
print(total)

