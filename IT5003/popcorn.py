# Time complexity = O(1)
players = int(input())

BAGS_NEED_AFTER_FIRST_ROUND = 4

def bagsOfPopcorn(players):

  def matches_per_group(size_per_group):
    return size_per_group * (size_per_group-1) // 2
  
  def calculatePlayersPerGrp(players):
    return players // 4

  size_per_group = calculatePlayersPerGrp(players)

  bagsNeededInFirstRound = matches_per_group(size_per_group) * 4

  return bagsNeededInFirstRound + BAGS_NEED_AFTER_FIRST_ROUND
print(int(bagsOfPopcorn(players)))