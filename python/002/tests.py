import unittest

from solutions.generator import even_fib_sum as generator_solution
from solutions.even_sequence import even_fib_sum as even_sequence_solution
from solutions.binet import even_fib_sum as binet_solution

class Problem002Test(unittest.TestCase):
  """
  Test Problem #002 generator solution
  """
  def test_generator_solution(self):
    self.assertEqual(generator_solution(100), 44)
    self.assertEqual(generator_solution(4000000), 4613732)

  """
  Test Problem #002 even sequence solution
  """
  def test_even_sequence_solution(self):
    self.assertEqual(even_sequence_solution(100), 44)
    self.assertEqual(even_sequence_solution(4000000), 4613732)
    
  """
  Test Problem #002 binet solution
  """
  def test_binet_solution(self):
    self.assertEqual(binet_solution(100), 44)
    self.assertEqual(binet_solution(4000000), 4613732)
    
if __name__ == "__main__":
  unittest.main(verbosity=2)