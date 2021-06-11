/*
  Even though the problem includes work with permutations,
    it is not necessary to permute each and every cube to solve
    the problem. This approach would take too much time and resources.

  To explain the approch, let's take two arrays with the same elements
    but in different order: [1, 2, 3] and [3, 2, 1]. By checking the
    permutations of each list can be concluded that sets of permutations
    are the same.

  Using the uniqueness of the set of permutations, we can using the
    following algorithm:

    - Initialize and integer for generating cubes;
    - Initialize an empty dictionary for permutations storage;
    - Start an infinite while loop:
      - Transform a cube to the sorted string representation, ex: 3210 -> "0123"
      - Check if the dictionary contains permutation string:
        - No: store a {key:value} as {permutation string: integer, 1}
          Integer meant to be the number that formed the cube, it is usefull
          as the problem asks for the smallest cube; and the "1" means number
          of occurrences for the given permutation;
        - Yes: Increment the number of occurrences;
      - Check if the permutation string occured as much times as the problem asks for;
        - Yes: the problem solved, get the smallest number from the dictionary and
          BREAK out of the loop;
      - Increment the integer to generate the next cube;

  The approach works 6 times as fast against "using lists" approach on my machine.  
*/

const cubicPermutations = permutations => {
  let number = 0
  const cubes = {};

  while (true) {
    const cubePermutation = [ ...(number ** 3).toString() ].sort().join("");

    if (!cubes.hasOwnProperty(cubePermutation)) {
      cubes[cubePermutation] = [ number, 1 ];
    } else {
      //console.log(cubePermutation);
      cubes[cubePermutation][1] += 1;
    }

    if (cubes[cubePermutation][1] === permutations) {
      return cubes[cubePermutation][0] ** 3;
    }
    
    number++;
  }
};

//console.log(cubicPermutations(3));
//console.log(cubicPermutations(5));
