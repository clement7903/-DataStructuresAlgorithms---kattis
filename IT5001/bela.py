scores = {
  'A': [11, 11],
  'K': [4, 4],
  'Q': [3, 3], 
  'J': [20, 2],
  'T': [10, 10],
  '9': [14, 0],
  '8': [0, 0],
  '7': [0, 0]  
}

TOTALSCORE = 0

playerinput = input().split(' ')
numOfCards = int(playerinput[0]) * 4
dominantSuit = playerinput[1]

for i in range (numOfCards):
  card = input()
  card_num = card[0]
  card_suit = card[1]
  if card_suit == dominantSuit:
    TOTALSCORE += scores[card_num][0]
  else:
    TOTALSCORE += scores[card_num][1]

print(TOTALSCORE)
  
