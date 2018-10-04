// returns the n-fibonacci number using the Binet formula
// starts from 0, 1, 1, 2, 3, 5...
fibonacci = {
  phi: (1 + Math.sqrt(5)) / 2,
  Phi: (1 - Math.sqrt(5)) / 2,

  getItem(index) {
    let number = Math.ceil((1 / Math.sqrt(5)) * (this.phi ** index - this.Phi ** index));
    return number;
  }
}
