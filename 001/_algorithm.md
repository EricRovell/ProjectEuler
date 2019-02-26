# Unoptimized solution 

In order to solve this problem for **any number of divisors**:

*We can use iterable (set, list, or array) 
filled with desired number of divisors and unpack them as function arguments.*

1. Initialize a variable for storing sum value with initial value as zero.
2. Using outer loop iterate over all natural numbers up to the desired limit.
3. Using inner loop iterate over divisors.
4. if 
   `number mod (divisor) = 0` for any divisor:
   - add the number's value to sum
   - break out of the inner loop, there is no need to check for any other divisors.
5. After both loops terminated -> return the sum value.

# Optimized approach

Checking every number for divisibility for huge ranges might take quite a while. We can solve this problem more directly without checking every number.

Assume for example we have a range up to 1000: $[1, 1000)$

Numbers divisible by some exact divisor forms an arithmetic series:

For $divisor = 3:$
> $3, 6, 9, 12, 15, 18, 21...$

We should find the sum of all this numbers. Let's factor out the divisors to simplify the summation:
> $3 * (1 + 2 + 3 + 4 + 5 + 6 + 7...)$

More generally:
> $divisor * (1 + 2 + 3 + ... + N)$,
> 
where $N = \lfloor (limit - 1) / divisor \rfloor$ - the last divisible number less than a limit.

Writing down using Sigma operator:

> $divisor$ * $\sum_{number=1}^{N} number$

Finally, using the arithmetic series formula:

> $Sum = divisor * (1 + N) * \frac{N}{2}$

Our result can be written as program like this:

```
function multSum(limit, divisor) {
  lastMultiple = floor((limit - 1) / divisor);
  return divisor * (1 + lastMultiple) * lastMultiple / 2
}
```

In the problem statement we have 2 natural numbers for which the sum of all their divisors should be evaluated.

We might think at first that the solution might me quite simple, using the function definition above:

```
multSum(limit, divisor1) + multSum(limit, divisor2)
```

But actually there are some numbers that are divisible by **divisor1** AND **divisor2**. So we count them twice. Quite a problem, is it not?

After some thinking we can come to conclusion that it can be avoided by subtracting these numbers from sum of divisible numbers for both divisors:

```
multSum(limit, divisor1) + multSum(limit, divisor2) - multSum(limit, divisor1 - divisor2)
```

For more than 2 different divisors the subtraction might get more and more complicated because we should subtract all possible products from all divisors. 
---