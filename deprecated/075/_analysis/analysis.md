# #075: Singular integer right triangles

## The problem

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm <- (3,4,5), \
24 cm <- (6,8,10), \
30 cm <- (5,12,13), \
36 cm <- (9,12,15), \
40 cm <- (8,15,17), \
48 cm <- (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm <- (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

---

## Berggren's Linear Transformations

By a result of Berggren (1934), all primitive Pythagorean triples can be generated from the (3, 4, 5) triangle by using the three linear transformations below, where a, b, c are sides of a triple:

$$
\begin{array}{c|ccc}
T & \text{a} & \text{b} & \text{c} \\
\hline
T_1 & +a - 2b + 2c & +2a - b + 2c & +2a - 2b + 3c \\
T_2 & +a + 2b + 2c & +2a + b + 2c & +2a + 2b + 3c \\
T_3 & -a + 2b + 2c & -2a + b + 2c & -2a + 2b + 3c
\end{array}
$$

In other words, every primitive triple will be a "parent" to three additional primitive triples. Starting from the initial node with a = 3, b = 4, and c = 5, transformations produce new triples:

$$
(3, 4, 5) \mapsto
\begin{cases}
  (5, 12, 13) \\ 
  (21, 20, 29)\\ 
  (15, 8, 17)
\end{cases}
$$

The linear transformations $T_1, T_2$ and $T_3$ have a geometric interpretation in the language of quadratic forms. They are closely related to (but are not equal to) reflections generating the orthogonal group of $x2 + y2 − z2$ over the integers.

Using these transformations it is possible to get all the primitive Pythagorean triples the problem asks for. The next step is to generate all non-primitive triples by simple multiplication:

$$
\begin{aligned}
  (3, 4, 5) & \xrightarrow{\times 2} (6, 8, 10) \\
  (3, 4, 5) & \xrightarrow{\times 3} (9, 12, 15) \\
  (3, 4, 5) & \xrightarrow{\times 4} (12, 16, 20)
\end{aligned}
$$
