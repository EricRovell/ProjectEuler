# dictionary subclass -> count thr frequency
from collections import Counter

# data location
_path = '054_data.txt'

# ranks -> values
values = {rank: value for value, rank in enumerate('23456789TJQKA', 2)}
# straights combinations
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
# cards ranking
ranks = [
  (1,1,1,1,1),
  (2,1,1,1),  # -> 1 pair
  (2,2,1),    # -> 2 pairs
  (3,1,1),    # -> 3 of a kind
  (),         # -> ? straight
  (),         # -> ? flush
  (3,2),      # -> 3 of a kind and a pair
  (4,1)       # -> 4 of a kind
]

# ranking algorithm
def hand_rank(hand):
  cards_count = Counter(x[0] for x in hand)
  score = ((v, values[k]) for	k,v in cards_count.items())
  score = list(zip(*sorted(score, reverse = True)))
  score[0] = ranks.index(score[0])
  # -> flush
  if len(set(card[1] for card in hand)) == 1:
    score[0] = 5
  # -> straight
  if score[1] in straights:
    # -> straight / straight flush
    score[0] = 8 if score[0] == 5 else 4
  return score

# simulate games from the data file,
# count how many times the player 1 won.
def games(path = _path):
  hands = [line.split() for line in open(path)]
  p1_wins = sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)
  return p1_wins

# results
print(games())