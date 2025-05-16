# Gross Pay Calculator

> "A penny saved is a penny earned." 
>
> — Benjamin Franklin

Ever wondered how much your paycheck would be if you worked a little extra? This
program will help you calculate your gross pay based on your hours worked and
hourly rate, including overtime pay for those extra hours.

Write a Python program to compute your gross pay. The program should ask you for
the number of hours you worked and your hourly rate. It will then calculate your
pay, paying the regular rate for up to 40 hours and 1.5 times the hourly rate
for any hours worked beyond 40.

## Inputs

Prompt the user to enter the following information:

- Hours worked (float)
    Assume that the user will input only numeric values, such as: `45` for 45
    hours or `38.5` for 38.5 hours.
- Hourly rate (float)
    Assume that the user will input only numeric values, such as: `10.50` for
    $10.50 per hour or `15.75` for $15.75 per hour.

## Expected Output
- If user enter negative numbers for either hours worked, hourly rate or both,
  print exactly this message: `Hours and rate should be positive`
- Otherwise calculate and print the gross pay in the form:
    `Your gross pay is $AMOUNT`

Examples:
- If you type `45` for the hours and type `10.5` for the rate, your program
  should output: `Your gross pay is $498.75`
  * This is base + OT or (40.0 * 10.5) + (5.0 * (10.5 * 1.5))
- If you type `30` for the hours and type `20` for the rate, your program should
  output: `Your gross pay is $600.0`
  * This is just base or (30.0 * 20.0)

> NOTE: we are again just letting decimal places run wild, so `$600.0` instead
> of `$600.00` is expected.

## Source
- Adapted from PY4E
