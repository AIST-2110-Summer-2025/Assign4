# Grade Calculator

This program will help you determine your grade for a quiz. Simply provide the
number of questions, how many you got right. The program will then calculate the
score as a percent and assign a letter grade. The letter grade will be based on
the following table:

| Score   | Grade |
|:-------:|:-----:|
| >= 90%  |   A   |
| >= 80%  |   B   |
| >= 70%  |   C   |
| >= 60%  |   D   |
|  < 60%  |   F   |

## Inputs

Prompt the user to enter the following information:

- Total number of questions (int)
- Number of correct answers (int)

## Expected Output

- You should calculate and print the score and letter grade in the format:

  `CORRECT out of TOTAL is SCORE% (LETTER)`

  > _Remember that the score will be correct divided by total. But that to get
  > the percent formatted correctly you must also multiply this by 100._

- Examples:

    - If you enter `10` for total and `10` for correct, the program should print:

      `10 out of 10 is 100.0% (A)`

    - If you enter `20` for total and `16` for correct, the program should print:

      `16 out of 20 is 80.0% (B)`

    - If you enter `12` for total and `9` for correct, the program should print:

      `9 out of 12 is 75.0% (C)`

    - If you enter `13` for total and `8` for correct, the program should print:

      `8 out of 13 is 61.53846153846154% (D)`

    - If you enter `5` for total and `0` for correct, the program should print:

      `0 out of 5 is 0.0% (F)`

## This Program STINKS

Yes, this program will be...bad. Enter a 0 for number of questions? KABOOM!!!
Enter a negative value for either? That's nonsense but it gives you something.
Get 1000 correct answers on a 10 question test? No problem!! Those percents with
all those decimal places? UGLY!!! We'll revisit this one in a later assignment,
so just hold your nose as you test this one.

## Source
- Adapted from PY4E
