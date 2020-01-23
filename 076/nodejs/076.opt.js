const summations = int => {
  const ways = [ 1, ...new Array(int).fill(0)];
  for (let number = 1; number < int; number++) {
    for (let addend = number; addend <= int; addend++) {
      ways[addend] += ways[addend - number];
    }
  }

  return ways[int];
}; 

//console.log(summations(100));
