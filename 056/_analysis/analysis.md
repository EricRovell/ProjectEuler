For me, it was a case of choosing practical constraints.

10^m contains m+1 digits.

Solving, 90^99=10^k, k=99log90&#8776;193.5, so 90^99 contains int(99log90)+1=194 digits.
Working on the principle that the average digit is 5 (a uniform distribution of digits), we would expect the sum of digits in 90^99 to be 5?194=970.

Similarly, 90^90 contains int(90log90)+1=176 digits, with an expected sum is 880; and 99^99 contains int(99log99)+1=198 digits, with an expected sum is 990.

Note how quickly our expected sum becomes smaller by comparing 90^99 (970) with 90^90 (880).

Based on this I used (in my view) an excessively modest/safe search, starting with a=90 and b=90.

It is interesting to note that the answer, 99^95, contains int(95log99)+1=190 digits, and its expected sum is 950, whereas its actual digital sum is 972. This suggests either that the mean digit value is about 5.12, or this particular solution is unusually rich in digits exceeding 5.