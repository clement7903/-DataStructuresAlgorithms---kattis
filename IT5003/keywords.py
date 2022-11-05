num = int(input())

d = set()

for _ in range(num):
  word = input().lower()
  word.replace('-', ' ')
  d.add(word)

print(len(d))
# set implemention is something like dictionary implementation
# unable to do indexing operations