"""
Problem #009: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# returns the existing pythagorean triplets that gives the sum "m"
# a + b + c = m 
def pythagorean_triplet(m):

  for a in range(1, m):
    for b in range(1, m):
      for c in range(1, m):
        
        #triangle inequality
        if c < a + b and a < b + c and b < a + c:
          # pythagorean triangle
          if a ** 2 + b ** 2 == c ** 2:
            # desired perimeter
            if a + b + c == m:
            
              return f'({a}, {b}, {c}) => with product {a * b * c}.'

# test
print(pythagorean_triplet(1000))