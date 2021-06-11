/*
  This is not optimised solution!

  Even though the problem includes work with permutations,
    it is not necessary to permute each and every cube to solve
    the problem. This approach would take too much time and resources.

  To explain the approch, let's take two arrays with the same elements
    but in different order: [1, 2, 3] and [3, 2, 1]. By checking the
    permutations of each list can be concluded that sets of permutations
    are the same.

  Using the uniqueness of the set of permutations, we can using the
    following algorithm:

    - Generate a cube
    - Transform a cube to the sorted string representation (or list)
    - Include sorted string into list
    - Check if the list contains the given string as much times as the
        problem asks
    - If not -> increment a number to generate next cube.
    - Repeat

  The approach works but not really good one: it takes space for each
    permutation to store and checking the number of occurences is expensive.  
*/

const cubicPermutations = permutations => {
  let number = 0;
  const cubes = [];

  while (true) {
    const cube = [ ...(number ** 3).toString() ].sort().join("");
    cubes.push(cube);

    const countCubes = cubes.reduce((total, el) =>
      (el === cube) ? total + 1 : total, 0);

    if (countCubes === permutations) {
      return cubes.indexOf(cube) ** 3;
    }
    number++;
  }
};

// assertions
//console.log(cubicPermutations(3))
//console.log(cubicPermutations(5))
