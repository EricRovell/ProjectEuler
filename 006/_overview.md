# 006: Sum square difference

Table of contents:
- [006: Sum square difference](#006-sum-square-difference)
  - [Description:](#description)
  - [Brute force](#brute-force)
  - [Optimized solution](#optimized-solution)
    - [Sum of natural numbers](#sum-of-natural-numbers)
    - [Sum of squares](#sum-of-squares)
  - [The difference function](#the-difference-function)

## Description:

The sum of the squares of the first ten natural numbers is:

$1^2 + 2^2 + ... + 10^2 = 385$

The square of the sum of the first ten natural numbers is:

$(1 + 2 + ... + 10)^2 = 55^2 = 3025$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 − 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---

## Brute force

Considering such low bound the problem asks for, the brute force solution is not a bad option. Realization is straightforward.

We start with initializing three variables for storing:

- limit value
- sum of squres
- square of sum

After that, iterating over closed interval [1, limit] with *for* loop, loop-variable **i** is added to the square of sum and **i ^ 2** to the sum of squres simultaneously.

After the loop is finished, calculated difference between two variables if printed (sum ^ 2 - sum of squares).

```
limit <- 100
sum   <- 0   // sum of natural numbers
sumsq <- 0   // sum of squares

for number in [1, limit]:
  sum += number
  sumsq += number ^ 2

print sum ^ 2 - sumsq
```

However, such an approach will definetely get in trouble when limit become very large.

---

## Optimized solution

Optimized solution to this problem makes it possible to get the answer directly without incrementing the sum values, making improvements in time and memory usage.

### Sum of natural numbers

Sum of natural numbers can be easily found using the *sum of the finite arithmetic progression* formula:
$$
\begin{aligned}
\sum\limits_{i = 1}^n i = \frac{1 + n}{2}n, n \in \mathbb{N}
\end{aligned}
$$

To get the square of sum we can use this formula directly and raise to the power of 2.

### Sum of squares

Dealing with sum of squares is a bit trickier, but a possible task. 

The investigation for the functional relation between the natural number and the sum of all squares up to this number begins with mapping values for some arguments:

|    argument    | 0 | 1 | 2 |  3 |  4 |  5 |  6 |
|----------------|---|---|---|----|----|----|----|
| sum of squares | 0 | 1 | 5 | 14 | 30 | 55 | 91 |

Let's investigate how much increments the sum with each time we increment our argument (values of differential):

We have: +1, +4, +9, +16, +25, +36. Non-linear growth. It means that function is not linear and may have quadratic form. To investigate further we get the incrementation of incrementation values:

We have: +3, +5, +7, +9, +11. Still not linear. Function is not quadratic and may be the 3rd order polynomial. It will become clear if we will check the incrementation of the values above:

We have: +2, +2, +2, +2. Linear growth! It means the function we are searching is definetly the 3rd order polynomial after all and has the form:

$ax^3 + bx^2 + cx + d = 0$

Let's map all information we got to the table:

|    argument    | 0 |  1 |  2 |  3 |   4 |   5 |   6 |
|----------------|---|----|----|----|-----|-----|-----|
| sum of squares | 0 |  1 |  5 | 14 |  30 |  55 |  91 |
| $\varDelta_1$  |   | +1 | +4 | +9 | +16 | +25 | +36 |
| $\varDelta_2$  |   |    | +3 | +5 |  +7 |  +9 | +11 |
| $\varDelta_3$  |   |    |    | +2 |  +2 |  +2 | +2  |

Putting in zero argument to the function we get that d member of polynomial is actually zero:

$a * 0^3 + b * x^2 + c * x + d = 0 \Rightarrow d = 0$

We have 3 unknown variables $(a, b, c)$, thus we use the next three arguments to build-up the system of equations:

$$
\left\{
\begin{array}{ll}
a + b + c &= 1 \\
8a + 4b + 2c &= 5 \\
27a + 9b + 3c &= 17
\end{array}
\right.
$$

We can rewrite this system to the matrix form:

$$ \left[
\begin{array}{ccc}
  1&1&1\\
  8&4&2\\
  27&9&3
\end{array}
\right]

\left[
  \begin{array}{ccc}
  a\\
  b\\
  c
\end{array}
\right]

=

\left[
  \begin{array}{ccc}
  1\\
  5\\
  14
\end{array}
\right] $$

By solving this equation we have:

$$
\left[
\begin{array}{ccc}
  a\\
  b\\
  c
\end{array}
\right]

=

\left[
  \begin{array}{ccc}
  1/3\\
  1/2\\
  1/6
\end{array}
\right] $$

The function we were searching for:

$$
\begin{aligned}
\sum_{n = 1}^{x}n^2 = f(x) = \frac{1}{3}x^3 + \frac{1}{2}x^2 + \frac{1}{6}x
\end{aligned}
$$

We can refactor it:

$$
\begin{aligned}
  f(x) &= \frac{2x^3 + 3x^2 + x}{6} \\
       &= \frac{x(2x^2 + 3x + 1)}{6} \\
       &= \frac{x(2x + 1)(x + 1)}{6}
\end{aligned}
$$

Having the function under out belt we can write highly optimized solution. 

```
limit <- initializing the limit value

// calcultating the sum of natural numbers
sum <- (1 + limit) * limit / 2

// calcultating the sum of squares
sqsum <- limit * (2 * limit - 1) * (limit - 1) / 6

print sum ^ 2 - sqsum
```

This algorithm is limited only by the size of the integer types your programming language (and computer
memory) support.

---

## The difference function

The formulas we got in the previous step seems to be enough, but we can improve the solution a bit more. Using those two equations we can derive the direct formula to get the answer the problem asks for:

To get the difference, we have to subtract the sum of squares from sum of natural numbers raised to the power of two:

$$
\begin{aligned}
  \varDelta(n) &= \Big(\frac{1 + n}{2}n\Big)^2 - \frac{n(2n + 1)(n + 1)}{6}\\
    &= \frac{(1 + 2n + n^2)n^2}{4} - \frac{2n^3 + 3n^2 + n}{6} \\
    &= \frac{n^4 + 2n^3 + n^2}{4} - \frac{2n^3 + 3n^2 + n}{6} \\
    &= \frac{3n^4 + 6n^3 + 3n^2 - 4n^3 - 6n^2 - 2n}{12} \\
    &= \frac{3n^4 + 2n^3 - 3n^2 - 2n}{12} \\
    &= \frac{n(3n^3 + 2n^2 - 3n - 2)}{12} \\
    &= \frac{n(n - 1)(3n^2 + 5n + 2)}{12} \\
    &= \frac{n(n - 1) \times 3(x + 1)(x + 2/3)}{12} \\
    &= \frac{n(n^2 - 1)(3x + 2)}{12}
\end{aligned}
$$

After all this work we have got the direct formula to get the answer:

$$
\begin{aligned}
\varDelta(n) = \frac{n(n^2 - 1)(3x + 2)}{12}, n \in \mathbb{N}
\end{aligned}
$$

Pseudocode for this result is pretty straightforward:

```
limit <- initializing a limit variable
print(limit * (limit ^ 2 - 1) * (3 * limit + 2) / 12)
```