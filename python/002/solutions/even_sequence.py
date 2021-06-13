def fibonacci_sequence_even(limit: int) -> int:
  a, b = 2, 8
  while a < limit:
    yield a
    a, b = b, 4 * b + a
    
def even_fib_sum(limit: int) -> int:
  return sum([ item for item in fibonacci_sequence_even(limit) ])