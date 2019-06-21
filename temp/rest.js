function rest(a, b, ...[params]) {
  console.log(a);
  console.log(b);
  console.log(params);
  const {limit, period} = params;
  console.log(limit, period);
}

rest(1, 2, {limit: true, period: false});

