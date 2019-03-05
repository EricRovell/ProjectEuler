# Even Fibonacci Numbers

## Brute force

The direct translation of the problem is to generate all Fibonacci numbers up to the given value limit and check every member of the sequencefor parity:

1. Initiate a **limit** variable with desired value for this problem.\
  $limit \leftarrow value$
2. Initiate a **sum** variable with value of zero (identity element).\
  $sum \leftarrow 0$
3. Initiate variables **a** and **b** both equal to **1** as seed values for generating Fibonacci sequence. (**a = 0** and **b = 1** also possible, the difference is the starting index of the sequence).\
   $a \leftarrow 1$, </br>
   $b \leftarrow 1$.
4. While **b** is less than **limit**, repeat:
   - **if** $b \bmod 2 = 0$, update the **sum** value: </br>
    $sum \leftarrow sum + b$
   - generate next terms of the Fibonacci sequence: </br>
    $a \leftarrow b$, </br>
    $b \leftarrow a + b$

---

## Even-fibonacci sequence solution, recursive

Checking every fibonacci number takes a lot of computing power and might be unnecessary. Let's try to get rid of this excessive testing for parity in the sequence. After looking at sequence itself we might see:

>$1, 1,$ $\color{red}2$ $, 3, 5,$ $\color{red}8$, 13, 21, $\color{red}34$ $, 55, 89,$ $\color{red}144...$

that every 3rd member is even.  

This reduces our sequence to:

> $F_{even} = \{F_{k}: k = 3n, n \ni \N \}$

With this information let's try to find recursive relation for even Fibonacci numbers:
 
$$\begin{aligned}
F_{n} &= F_{n-1} + F_{n-2}\\
&= F_{n-2} + F_{n-3} + F_{n-2}\\
&= 2 F_{n-2} + F_{n-3}\\
&= 2 (F_{n-3} + F_{n-4}) + F_{n-3}\\
&= 2 F_{n-3} + 2 F_{n-4} + F_{n-3}\\
&= 3 F_{n-3} + 2 F_{n-4}\\
&= 3 F_{n-3} + F_{n-4} + F_{n-4}\\
&= 3 F_{n-3} + F_{n-4} + F_{n-5} + F_{n-6}\\
&= 3 F_{n-3} + (F_{n-4} + F_{n-5}) + F_{n-6}\\
&= 3 F_{n-3} + F_{n-3} + F_{n-6}\\
&= 4 F_{n-3} + F_{n-6}\\
\end{aligned}$$