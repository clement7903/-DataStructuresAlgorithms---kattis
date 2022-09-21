VOWELS = ['a', 'e', 'i', 'o', 'u']
count = 0

user_input = input()

for char in user_input:
  if char in VOWELS:
    count += 1
print(count)