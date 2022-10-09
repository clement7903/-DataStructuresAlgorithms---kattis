# Time complexity - n
n = int(input())

# keep track of the number of people infected for each strain
vaccine_infected, placebo_infected = [0, 0, 0], [0,0,0]
vaccine_total, placebo_total = 0, 0

for _ in range(n):
  participant = input()
  if participant[0] == 'Y':
    # vaccinated grp
    vaccine_total += 1
    for i in range(1, 4):
      vaccine_infected[i-1] += (participant[i] == 'Y')
  else:
    placebo_total += 1
    for i in range(1, 4):
      placebo_infected[i-1] += (participant[i] == 'Y')

for i in range(3):
  vaccine_rate = vaccine_infected[i] / vaccine_total
  placebo_rate = placebo_infected[i] / placebo_total
  if vaccine_rate >= placebo_rate:
    print('Not Effective')
  else:
    print((placebo_rate - vaccine_rate) / placebo_rate * 100)