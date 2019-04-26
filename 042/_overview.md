# 042: Coded triangle numbers

## Problem

The $n-th$ term of the sequence of triangle numbers is given by:

$$t_n = \frac{n(n + 1)}{2}$$

so the first ten triangle numbers are:

$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...$$

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.

$$ score(word) = \sum_{letter}^{word} (letter \mapsto alphabetical \ order)$$

For example, the word value for SKY is the 10th triangle number:

$$score(sky) = (s \rightarrow 19) + (k \rightarrow 11) + (y \rightarrow 25) = 55 = t_{10}$$

If the word value is a triangle number then we shall call the word a triangle word.

Using **data file (042_data.txt)**, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?

---

## Brute force

## Optimized solution

