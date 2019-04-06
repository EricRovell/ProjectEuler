# #076: Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can 100 be written as a sum of at least two positive integers?

---

## Dynamic programming approach

For explaining the idea Let us create an array for storing up solution and solve the problem for smaller number 9.

Instead of trying to get the solution for the nu,ber itself, we will build up solutions from the smallest sub-problems that will slowly lead to the answer we need.

|number| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| ways | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

We begin with the number 1. Obviously there is the only way to get any number using ones.

|number| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| ways | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

Now we have 1 and 2 at our disposal. We can't use our new number '2' to make up 1. Actually any new number in our collection won't be used to make up any number less than this number, obviously.

Let's start with number 2. We can get number 2 by using only 2 itself. We should not forget that we already have 1 solution for 2 as (2 = 1 + 1) from previous step. Hence now we add up one more to the array:

|number| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| ways | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

All next steps are similar:

1: Untouched
2: Only 2, +1 solution -> 2
3: 3 - 2 = 1, +1 solution from '1' -> 2
4: 4 - 2 = 2, +2 solution from '2' -> 3
5: 5 - 2 = 3, +2 solution from '3' -> 3
6: 6 - 2 = 4, +3 solution from '4' -> 4
7: 7 - 2 = 5, +3 solution from '5' -> 7
8: 8 - 2 = 6, +4 solution from '6' -> 5
9: 9 - 2 = 7, +4 solution from '7' -> 5

And we get this result:

|number| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|
| ways | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 |

Once more time, to grasp the idea better.

Now we have 1, 2, and 3 at our disposal.

1: Untouched
2: Untouched
3: Only 3, +1 solution -> 3
4: 4 - 3 = 1, +1 solution from '1' -> 4
5: 5 - 3 = 2, +2 solution from '2' -> 5
6: 6 - 3 = 3, +3 solution from '3' -> 7
7: 7 - 3 = 4, +4 solution from '4' -> 8
8: 8 - 3 = 5, +5 solution from '5' -> 10
9: 9 - 3 = 6, +7 solution from '6' -> 12

|number| 1 | 2 | 3 | 4 | 5 | 6 | 7 |  8 |  9 |
|------|---|---|---|---|---|---|---|----|----|
| ways | 1 | 2 | 3 | 4 | 5 | 7 | 8 | 10 | 12 |