# #054: Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

- High Card: Highest value card.
- 1 Pair: Two cards of the same value.
- 2 Pairs: Two different pairs.
- 3 of a Kind: Three cards of the same value.
- Straight: All cards are consecutive values.
- Flush: All cards of the same suit.
- Full House: 3 of a kind and a pair.
- 4 of a Kind: Four cards of the same value.
- Straight Flush: All cards are consecutive values of same suit.
- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

$$
\begin{array}{cccc}
  \text{Hand} & \text{Player 1} & \text{Player 2} & \text{Winner} \\
  \hline
  1 & \text{5H 5C 6S 7S KD} & \text{2C 3S 8S 8D TD} & \text{Player 2} \\
  & \text{Pair of Fives} & \text{Pair of Eights} \\
  \hline
  2 & \text{5D 8C 9S JS AC} & \text{2C 5C 7D 8S QH} & \text{Player 1} \\
  & \text{Highest card Ace} & \text{Highest card Queen} \\
  \hline
  3 & \text{2D 9C AS AH AC} & \text{3D 6D 7D TD QD} & \text{Player 2} \\
  & \text{Three Aces} & \text{Flush with Diamonds} \\
  \hline
  4 & \text{4D 6S 9H QH QC} & \text{3D 6D 7H QD QS} & \text{Player 1} \\
  & \text{Pair of Queens} & \text{Pair of Queens} \\
  & \text{Highest card Nine} & \text{Highest card Seven} \\
  \hline
  5 & \text{2H 2D 4C 4D 4S} & \text{3C 3D 3S 9S 9D} & \text{Player 1} \\
  & \text{Full House} & \text{Full House} \\
  & \text{with Three Fours} & \text{with Three Threes} \\
  \hline
\end{array}
$$

The file, **054.data.txt**, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?