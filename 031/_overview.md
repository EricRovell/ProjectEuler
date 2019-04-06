# #031: Coin sums

- [#031: Coin sums](#031-coin-sums)
  - [Problem](#problem)
  - [Brute force](#brute-force)
  - [Dynamic programming approach](#dynamic-programming-approach)
    - [Smaller example for understanding the approach](#smaller-example-for-understanding-the-approach)

## Problem

*In England the currency is made up of pound **£**, and pence **p**, and there are eight coins in general circulation:*

> 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

*It is possible to make £2 in the following way:*

> £2 = 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

*How many different ways can £2 be made using any number of coins?*

---

## Brute force

The brute force solution is to create a set of nested loops for every coin type. The smaller the coin the deeper it goes in nesting. Inner loop value is dependent on the outer. This way it is possible to test if there is way to get 2£.

Obviously, it is better to use only pennies values in code.

```
value = 200  # how many we want to collect
ways  = 0    # how many ways to collect the target

for coin200 in range(value, -1, -200):
  for coin100 in range(coin200, -1, -100):
    for coin50 in range(coin100, -1, -50):
      for coin20 in range(coin50, -1, -20):
        for coin10 in range(coin20, -1, -10):
          for coin5 in range(coin10, -1, -5):
            for coin2 in range(coin5, -1, -2):
              ways += 1

print(ways)
```

This solution lacks any flexibility. It is impossible to change the number and values of coins by any means without rewriting the code. Furthermore, so much nesting makes code completely unreadable.

---

## Dynamic programming approach

In order to to make a solution using *Dynamic Programming* we should find a way to break up the problem into independent smaller ones. There are dimention which can be done in for this problem:

- the number of different coins
- value to split

The question should be answered repeatedly is:

> If I have to give a change to **n** pennies, if I give back one coin of **x**, how many ways can I give back the rest **n - x** pennies using only coins of value **x** or **smaller**?

This exactly question is the seed for our solution. We can start from this:

> If I want to give change to *1 penny* using *1 penny*, how many ways can this be done?

Instead ob breaking down the problem with the question above, we will build an array of solutions instead, to get the answer once we are ready to ask for it.

### Smaller example for understanding the approach

Let's solve a simpler version of the problem: *"How many ways is it possible to give a change to 5 pennies using only 1, 2, and 3 pennies?"*

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 0 | 0 | 0 | 0 | 0 | 0 |

</center>

First of all we consider a situation when it is necessary to give a change only using 1 penny coin. 

The initial question is:

*In how many different ways is it possible to give a change to 0 penny with 1 penny coins?*

Answer to this weird question is exactly **1**. One way of giveing away nothing.

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 0 | 0 | 0 | 0 | 0 |

</center>

Alright. Let's continiue. *In how many different ways is it possible to give a change to 1 penny using 1 penny coins?*

We give away 1 coin and are left with 0 pennies. Well, the answer for number of ways to give a change for 0 pennies is already found: 1. We add up number of solutions, to get new value for 1: 0 + 1 = 1.

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 0 | 0 | 0 | 0 |

</center>

Next question. *If I want to give change to 2 pennies using 1 penny coins, by giving back 1 penny, in how many ways I can give back the remaining 1 penny?*

We have 2 pennies. After giving away 1 penny only 1 is left and we already know the answer. It was found after the previous question: 1. So, there are only one way to give a change to 2 pennies after giving away 1 penny coin. Solution for 2 is: 0 + 1.

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 1 | 0 | 0 | 0 |

</center>

All steps until 5 pennies are the same, untill we get:

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 1 | 1 | 1 | 1 |

</center>

That was not so interesting so far. It is rather obvious that there is only one way to give a change to any amount of coins using only 1 penny.

Now we have 1 and 2 penny coins.
Since we can't give away 2 pennies when we need to change 1 penny, there is no need to ask that question. We start exactly from situation with giving a change for 2 pennies.

*How many ways are to give a change to 2 pennies?*

We have 2 pennies and we give them back. Now we have 0 pennies and that's is the solution we already found. We add this solution from 0 to 2: 1 (present) + 1 (at 0).
 
<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 2 | 1 | 1 | 1 |

</center>

For 3 pennies we also give away 2 penny coin and then only 1 is left and we already have solution for that. 3: 1 (present) + 1 (at 1).

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 2 | 2 | 1 | 1 |

</center>

For 4 pennies we give away 2 and are left with 2. Solution for 4: 1 (present) + 2 (at 2).

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 2 | 2 | 3 | 1 |

</center>

For 5 pennies we give away 2 and are left with 4. Solution for 5: 1 (present) + 2 (at 3).

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 2 | 2 | 3 | 3 |

</center>

For 3 pennies we have (check yourself):

<center>

| Coins | 0 | 1 | 2 | 3 | 4 | 5 |
| ----- |---|---|---|---|---|---|
| Ways  | 1 | 1 | 2 | 3 | 4 | 5 |

</center>

Using this approach it is possible to build up an array to find the solution for this problem. 

Pseudocode may look like this:

```
initialize a target value
initialize an array with value + 1 elements
let the first element of array to be 1.


```