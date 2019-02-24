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