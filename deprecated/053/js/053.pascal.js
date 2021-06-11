const pascalsTriangle = rows => {
  // contructs a pascal's triangle with a given number of rows
  // triangle's represenations is an array of arrays
  const triangle = [];
  
  for (let n = 0; n < rows; n++) { 
    triangle[n] = new Array(n + 1);
    
    for (let k = 0; k < n + 1; k++) {            
      triangle[n][k] =
        (k === 0 || k === n) 
          ? 1
          : triangle[n - 1][k - 1] + triangle[n - 1][k];
    }
  }
  
  return triangle;
};

const overLimit = ({ n, limit }) => {
  // calculates how many values pascal's triangle
  // are greater than the given limit
  const triangle = pascalsTriangle(n);

  let counter = 0;
  for (let row of triangle) {
    for (let value of row) {
      if (value > limit) counter++;
    }
  }

  return counter;
}

// assert 4075
// n = 101: triangle's row counts from 0
console.log(overLimit({
  n: 101,
  limit: 1000000
}));