$$
\begin{array}{ccc}
10^{n - 1} &\le& x^n &<& 10^n \\
lg(10^{n - 1}) &\le& lg(x^n) &<& lg(10^n) \\
n - 1 &\le& n \times lg(x) &<& n \\
1 - 1/n &\le& lg(x) &<& 1
\end{array}
$$

$$
\begin{cases}
  lg(x) \ge 1 - 1/n \\
  lg(x) < 1
\end{cases}
\Rightarrow
\begin{cases}
  x \ge 10^{1 - 1/n} \\
  x < 10
\end{cases}
$$

$$
\lim_{n \rightarrow \infty}(1 - 1/n) = 1
\Rightarrow \lim_{n \rightarrow \infty}(10^{1 - 1/n}) = 10^1 = 10
$$

It means that the whole expression will approach 10 as n increases. So we can be sure that at some point we reach a value for n where the lower bound  is larger than 9 and thus lower bound is larger than the upper bound and there are no more solutions for larger values of n. So we know that if we iterate over values of n we have an upper bound at which we can stop.