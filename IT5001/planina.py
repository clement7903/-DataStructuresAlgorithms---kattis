num = int(input())

def planina(num):
  if num == 0:
    return 4
  else: 
    return (2**num + 1) ** 2

print(planina(num))