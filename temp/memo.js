const memento = func => {
  const history = {};
  return (input) => {
    return history[input] || (history[input] = func(input));
  };
};

const factorial = memento((number) => {
  if (number < 0) {
    throw new Error("Number must be positive.");
  }
  if (number === 0 || number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
});

console.log(factorial(30));