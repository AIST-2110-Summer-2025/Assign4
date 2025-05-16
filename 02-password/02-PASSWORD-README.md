# Password Matcher

In this exercise, you’ll write a program that checks if a user’s password and
its confirmation match. This is a fundamental step in ensuring that users don’t
accidentally mistype their passwords when creating accounts.

## Inputs

Prompt the user to enter the following information:

- A password
- A confirmation of the password

## Expected Output
- If the password and confirmation match, your program should output: `Passwords match.`
- If the password and confirmation do not match, your program should output: `Passwords do not match.`

## Hints
- Use simple string comparison with `==` to check if the two inputs are identical.

## Challenge (optional)

- Copy the contents of `password.py` to `password_challenge.py`. In the second
  script, enhance the program to check if the FIRST password entered is at least
  8 characters long. If it’s not, then tell them the password is too short and
  exit immediately without askinf for the password confirmation.

  > _**HINT**: The len function returns the length of a string. E.g.,
  > `len("python")` would return 6._

## Source
- Inspired by real-world scenarios in account creation processes.
