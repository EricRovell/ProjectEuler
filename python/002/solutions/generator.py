# fibonacci generator
def fibonacci_sequence(limit: int) -> int:
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b
    
def even_fib_sum(limit: int) -> int:
  return sum([ item for item in fibonacci_sequence(limit) if item % 2 == 0 ])