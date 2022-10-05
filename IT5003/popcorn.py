players = int(input())
BAGS_NEED_AFTER_FIRST_ROUND = 4

def bagsOfPopcorn(players):

  def sumNTerms(n):
    return (n / 2) * (2 + (n -1))
  
  def calculatePlayersPerGrp(players):
    return players // 4

  playersPerGrp = calculatePlayersPerGrp(players)

  bagsNeededInFirstRound = sumNTerms(playersPerGrp-1) * 4

  return bagsNeededInFirstRound + BAGS_NEED_AFTER_FIRST_ROUND
print(int(bagsOfPopcorn(players)))