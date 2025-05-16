# Parity

This program will help you determine whether a number is even or odd. It's a
simple exercise to get you comfortable with using conditionals in Python.

## Inputs

Prompt the user to enter the following information:

- An integer number
    - Assume that the user will input only whole numbers, such as `7` or `12`.

## Expected Output

- If you type `7`, your program should output: `7 is odd.`
- If you type `12`, your program should output: `12 is even.`
- If you type `0`, your program should output: `0 is even.`

## Hints

- Recall that `%` is the modulo operator in Python, which gives the remainder of
  a division. For example, `7 % 2` will give `1` (since 7 divided by 2 leaves a
  remainder of 1).
- You can use the modulo operator to check whether a number is even or odd: if
  `number % 2 == 0`, then the number is evenly divisible by 2 and thus it is
  even. Otherwise, it is odd.
- Recall that `input` returns a `str`, per
  [docs.python.org/3/library/functions.html#input](https://docs.python.org/3/library/functions.html#input).
- Recall that `int` can convert a `str` to a `int`, per
  [docs.python.org/3/library/functions.html#int](https://docs.python.org/3/library/functions.html#int).
- Recall that concatenating an number value to a string requres that you convert
  the number to a string using the `str()` function. See [Python's documentation
  on str()](https://docs.python.org/3/library/functions.html#func-str).

## Source
- Adapted from basic programming exercises.
