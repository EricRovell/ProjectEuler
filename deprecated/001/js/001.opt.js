const multSum = ({ limit, divisors }) => {

  const divSum = divisor => {
    const lastMult = Math.floor((limit - 1) / divisor);
    return Math.floor(
      divisor * (1 + lastMult) * lastMult / 2
    );
  };

  console.log(divisors[0]);

  return divSum(divisors[0]) + divSum(divisors[1]) - divSum(divisors[0] * divisors[1]);

};

console.log(multSum({ limit: 100, divisors: [3, 5] }));