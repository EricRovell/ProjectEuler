---
created: 10-06-2021
last-updated: 11-06-2021
---

# Задача #001: Числа, кратные 3 или 5

*Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.*

*Найдите сумму всех чисел меньше 1000, кратных 3 или 5.*

## Вычислительный подход

Попробуем решить задачу, вычислив сумму всех множителей напрямую, всё же тысяча - смехотворный объем работы для современной вычислительной техники.

Для решения задачи создадим переменную для хранения значения суммы кратных чисел. С помощью цикла, совершим обход натуральных чисел, проверяя делимость на 3 или 5 остатком от деления. Если остаток равен нулю - добавляем значение к нашей переменной. После окончания обхода задача решена.

### Пример реализации на Python

```python
def multiples_sum(limit):
  total = 0
  for number in range(limit):
    if number % 3 == 0 or number % 5 == 0:
      total += number
  return number
```

Можно попробовать решить задачу с помощью **list comprehension**:

```python
  multiples_sum = lambda limit: sum([ number for number in range(limit) if number % 3 == 0 or number % 5 == 0 ])
```

### Пример реализации на JavaScript

```js
function multiplesSum(limit) {
  let total = 0;
  for (let number = 1; number < limit; number++) {
    if (total % 3 === 0 || total % 5 === 0) {
      total += number;
    }
  }
  return total;
}
```

## Поиск оптимального решения

Пусть прямолинейное решение и работает молниеносно, сложность всё же составляет **O(n)**, другими словами, чем больше поле поиска, тем больше проверок. Попробуем решить поставленную задачу другим, более оптимальным способом со сложностью **O(1)**. В этом нам поможет школьный курс алгебры!

Выписав кратные для 3, заметим, что они образуют *арифметическую прогрессию*:

$$3, 6, 9, 12, 15, 18...$$

Её можно заметно упростить, вынеся тройку за скобку:

$$3 \times (1 + 2 + 3 + 4 + ... + N)$$

Для нахождения суммы в скобках понадобится формула суммы арифметической прогрессии, запишем её:

$$S_n = \frac{a_1 + a_n}{2} \times n$$

С помощью формулы суммы, можем найти сумму всех кратных чисел 3 и 5 по отдельности, а потом сложить. Верно? Не совсем. Торопясь, можно упустить небольшую деталь. Некоторые числа являются кратными как для 3, так и для 5. Например, 15. Говоря на математическом языке, множества кратных чисел имеют пересечение. Взяв сумму двух прогрессий, некоторые значения дублируются.

Воспользуемся тем же оружием, найдем сумму прогрессии чисел, кратных 3 и 5. Полученную сумму вычтем из общей суммы.

В итоге, мы получили математическое выражение для решения задачи. Сложность алгоритма **O(1)**!

## Реализация на Python

```python
arithmetic_sum(divisor, limit):
  last_multiple = floor((limit - 1) / divisor)
  return divisor * (1 + last_multiple) * last_multiple / 2

multiples_sum(limit):
  return arithmetic_sum(3, limit) + arithmetic_sum(5, limit) - arithmetic_sum(3 * 5, limit)
```