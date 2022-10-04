pa, ka, pb, kb, n = list(map(int, input().split()))

# cost per fridge per trip - lower is better
def calculateCostEffectiveness(pa, ka, pb, kb):
  return pa / ka, pb / kb

# maxtrips given n fridge & capacity
def calculateMaxTrips(n, capacity):
  if n <= capacity:
    return 1
  if n % capacity != 0:
    numOfTrips = (n // capacity)+ 1
  numOfTrips = n // capacity
  return numOfTrips

# total cost given trips and cost per trip
def calculateTotalCost(carATrips, carBTrips, pa, pb):
  return (carATrips * pa) + (carBTrips * pb)

# gets the lowest cost & the corresponding trips made by carA and carB
def getLowestCostCombination(possibilities):
  cost = min(possibilities.keys())
  CarATrips = possibilities[cost][0]
  CarBTrips = possibilities[cost][1]
  return CarATrips, CarBTrips, cost

# main function which runs the logic
def final_output():
  efficiencyA, efficiencyB = calculateCostEffectiveness(pa, ka, pb, kb)

  ''' Edge cases'''

  # if the cost is lowest, load is highest, exact multiple of load, just use that car
  if pa < pb and ka > kb and (n % ka == 0):
    CarATrips = calculateMaxTrips(n, ka)
    CarBTrips = 0
    totalCosts = calculateTotalCost(CarATrips, CarBTrips, pa, pb)
    
  elif pa > pb and ka < kb and (n % kb == 0):
    CarATrips = 0
    CarBTrips = calculateMaxTrips(n, kb)
    totalCosts = calculateTotalCost(CarATrips, CarBTrips, pa, pb)
  
  # if n is <= capacity of either cars, choose the highest delivery efficiency car to deliver
  elif n <= ka and n <= kb and efficiencyA < efficiencyB:
    CarATrips = calculateMaxTrips(n, ka)
    CarBTrips = 0
    totalCosts = calculateTotalCost(CarATrips, CarBTrips, pa, pb)

  elif n <= ka and n <= kb and efficiencyA > efficiencyB:
    CarATrips = 0
    CarBTrips = calculateMaxTrips(n, ka)
    totalCosts = calculateTotalCost(CarATrips, CarBTrips, pa, pb)

  ''' End of edge cases '''

  # else: Prioritize the highest delivery efficiency car
  # if CarA has better (aka. lower) cost efficiency: start with maxcarA trips
  possibilities = {}
  if efficiencyA < efficiencyB:
    carATrips = calculateMaxTrips(n, ka)
    remainingFridge = n - (carATrips * ka)
    carBTrips = calculateMaxTrips(remainingFridge, kb)
    remainingFridge = n - (carBTrips * kb)
    possibilities[calculateTotalCost(carATrips, carBTrips, pa, pb)] = (carATrips, carBTrips)
    while remainingFridge != 0 and carATrips != 0:
      carATrips -= 1
      remainingFridge = n - (carATrips * ka)
      carBTrips = calculateMaxTrips(remainingFridge, kb)
      remainingFridge = n - (carBTrips * kb)
      if (carATrips * ka) + (carBTrips * kb) >= n: # add only those combinations delivering more than n
        possibilities[calculateTotalCost(carATrips, carBTrips, pa, pb)] = (carATrips, carBTrips)
    carATrips, carBTrips, totalCosts = getLowestCostCombination(possibilities)

  else:
    carBTrips = calculateMaxTrips(n, kb)
    remainingFridge = n - (carBTrips * kb)
    carATrips = calculateMaxTrips(remainingFridge, ka)
    remainingFridge = n - (carBTrips * kb)
    possibilities[calculateTotalCost(carATrips, carBTrips, pa, pb)] = (carATrips, carBTrips)
    while remainingFridge != 0 and carBTrips != 0:
      carBTrips -= 1
      remainingFridge = n - (carBTrips * kb)
      carATrips = calculateMaxTrips(remainingFridge, ka)
      remainingFridge = n - (carATrips * ka)
      if (carATrips * ka) + (carBTrips * kb) >= n: # add only those combinations more than n
        possibilities[calculateTotalCost(carATrips, carBTrips, pa, pb)] = (carATrips, carBTrips)
    carATrips, carBTrips, totalCosts = getLowestCostCombination(possibilities)

  return carATrips, carBTrips, totalCosts
  
carA, carB, costs = final_output()

print('{} {} {}'.format(carA, carB, costs))