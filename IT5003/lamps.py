h, P = list(map(int, input().split()))

'''Constants'''
BULB_POWER = 60
BULB_LIFE = 1000
BULB_PRICE = 5

LAMP_POWER = 11
LAMP_LIFE = 8000
LAMP_PRICE = 60
'''Constants'''

'''Functions'''
def runningCost(E, H, P):
  return E * H * P / 100_000

def countNumNeeded(numOfDays, h, LIFE):
  totalHoursUsed = numOfDays * h
  return totalHoursUsed // LIFE + 1
''' Functions '''

# for 1st day
numOfDays = 1
H = numOfDays * h
bulb_running_cost = runningCost(BULB_POWER, H, P)
lamp_running_cost = runningCost(LAMP_POWER, H, P)
bulb_total_cost = bulb_running_cost + countNumNeeded(numOfDays, h, BULB_LIFE) * BULB_PRICE
lamp_total_cost = lamp_running_cost +  countNumNeeded(numOfDays, h, LAMP_LIFE) * LAMP_PRICE # no 

# iterate days till the lamp is cheaper
while lamp_total_cost >= bulb_total_cost: # until it is cheaper
  numOfDays += 1
  H = numOfDays * h
  bulb_running_cost = runningCost(BULB_POWER, H, P)
  lamp_running_cost = runningCost(LAMP_POWER, H, P)

  bulb_total_cost = bulb_running_cost + countNumNeeded(numOfDays, h, BULB_LIFE) * BULB_PRICE
  lamp_total_cost = lamp_running_cost +  countNumNeeded(numOfDays, h, LAMP_LIFE) * LAMP_PRICE # no need to buy additional lamp

print(numOfDays)