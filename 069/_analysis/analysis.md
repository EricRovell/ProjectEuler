# #069: Totient maximum

Euler's Totient function, $\phi(n)$, sometimes called the phi function, is used to determine the number of numbers less than $n$ which are relatively prime to $n$. For example, as $1, 2, 4, 5, 7$, and $8$, are all less than nine and relatively prime to nine, $\phi(9) = 6$.

$$
\begin{array}{c|l|c|c}
n & \text{Relatively Prime} & \text{$\phi(n)$} & \text{$n / \phi(n)$} \\
\hline
2	& 1	& 1	& 2 \\
3	& 1,2	& 2	& 1.5 \\
4	& 1,3	& 2	& 2 \\
5	& 1,2,3,4	& 4	& 1.25 \\
6	& 1,5	& 2	& 3 \\ 
7	& 1,2,3,4,5,6	& 6	& 1.1666... \\
8	& 1,3,5,7	& 4	& 2 \\
9	& 1,2,4,5,7,8	& 6	& 1.5 \\
10 & 1,3,7,9 & 4 &	2.5 \\
\end{array}
$$

It can be seen that $n = 6$ produces a maximum $n / \phi(n)$ for $n ≤ 10$.

Find the value of $n ≤ 1,000,000$ for which $n / \phi(n)$ is a maximum.

## Brute Force

## Optimised solution

$$\phi(n) = n \prod_{p|n} \left(1 - \frac{1}{p} \right)$$

$$
\begin{aligned}
\frac{n}{\phi(n)} &= \frac{n}{n \prod_{p|n} \left(1 - \frac{1}{p} \right)} \\
&= \frac{\cancel{n}}{\cancel{n} \prod_{p|n} \left(1 - \frac{1}{p} \right)} \\
&= \frac{1}{\prod_{p|n} \left(1 - \frac{1}{p} \right)}
\end{aligned}
$$