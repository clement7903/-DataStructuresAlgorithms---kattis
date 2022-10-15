n = int(input())
domjudge = {}
kattis = {}
results = set()
output = 0

for _ in range(n):
  current_input = input()
  results.add(current_input)

  if current_input not in domjudge:
    domjudge[current_input] = 1
  else:
    domjudge[current_input] += 1

for _ in range(n):
  current_input = input()
  results.add(current_input)
  if current_input not in kattis:
    kattis[current_input] = 1
  else:
    kattis[current_input] += 1

for item in results:
  output += min(domjudge.get(item, 0), kattis.get(item, 0))

print(output)

#