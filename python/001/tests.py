import unittest

from solutions.brute import multiples_sum as brute_force_solution
from solutions.brute_lambda import multiples_sum as brute_force_solution_lambda
from solutions.constant_time import multiples_sum as constant_time_solution

class Problem001Test(unittest.TestCase):
  """
  Test Problem #001 brute force solution
  """
  def test_brute_solution(self):
    self.assertEqual(brute_force_solution(10), 23)
    self.assertEqual(brute_force_solution(1000), 233168)
    
  """
  Test Problem #001 brute force lambda solution
  """
  def test_brute_lambda_solution(self):
    self.assertEqual(brute_force_solution_lambda(10), 23)
    self.assertEqual(brute_force_solution_lambda(1000), 233168)
    
  """
  Test Problem #001 constant time solution
  """
  def test_constant_time_solution(self):
    self.assertEqual(constant_time_solution(10), 23)
    self.assertEqual(constant_time_solution(1000), 233168)
    
if __name__ == "__main__":
  unittest.main(verbosity=2)