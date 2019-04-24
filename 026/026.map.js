// Not the best approach if asked the result itself.
// Can be done more straightforwards actually.
// Still, it was interesting to write (the ratio -> the decimal) converter.

function toDecimal(numerator, denominator, limit = null, getPeriod = false) {
  /**
   * Converts the given ratio to decimal form.
   * @param {int} numerator - the 1st member of the ratio.
   * @param {int} denominator - the 2nd member of the ratio.
   * @param {int} limit - limits the number of decimal digits to get,
   *                      default value: null -> returns the full decimal.
   * @param {boolean} getPeriod - if 'true' -> returns the period of the ratio instead.
   *                              default value: 'false'.
   * @returns {string} - if the decimal is reccuring -> '1.02(35)',
   * @returns {float}  - if the decimal is non-reccuring -> 2.5,
   * @returns {string} - if getPeriod = true, returns period if the ratio,
   *                     no period -> '0' is returned.   
   */
  let unit = ~ ~ (numerator / denominator);
  let divident = 10 * (numerator - unit * denominator);
  let decimal = `${unit}.`;
  // long division, searching for the same divident
  // stores information as {divident: index}
  // so we will be able to spot a period
  states = {};
  while (divident && limit || limit == null)
  {
    let previousIndex = states[divident]
    if (previousIndex) {
      let repetendStart = previousIndex;
      let nonRepeating = decimal.slice(0, repetendStart);
      let period = decimal.slice(repetendStart);
      if (getPeriod) {
        // return period if asked
        return period;
      }
      // reccuring decimal -> return
      return `${nonRepeating}(${period})`   
    }
    states[divident] = decimal.length;
    unit = ~ ~ (divident / denominator);
    decimal += unit.toString();
    divident = 10 * (divident - unit * denominator);
    if (limit) { limit--; };
    if (limit === 0) { break; }
  }
  // period is asked, but the ratio has not one
  if (getPeriod) { return '0'; }
  // the decimal is non-reccuring, return float
  return Number(decimal);
}

// solving the problem
search = (denominatorLimit) => {
  // Searches for the longest period of the fractions of form 1/denominator,
  //  where denominator is in [1, denominatorLimit)
  let [number, period] = [0, 0];
  for (let denominator = 1; denominator < denominatorLimit; denominator++)
  {
    let currentPeriod = toDecimal(1, denominator, undefined, true).length;
    if (currentPeriod > period) {
      [number, period] = [denominator, currentPeriod];
    }
  }
  return `The longest period length ${period} has denominator ${number}`;
};

// results
console.log(search(1000));