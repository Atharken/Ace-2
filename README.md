# ACE Programming – Password Strength Checker

A simple Python command-line program that checks the strength of a password based on different requirements.

## 📌 Project Description

The Password Strength Checker asks the user to enter a password and analyzes it to determine whether it is weak or strong.

The program checks whether the password contains:

- Minimum 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

It then gives the password a strength rating based on how many requirements are satisfied.

## 🚀 Features

- Checks minimum password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Gives a strength rating:
  - Very Weak
  - Weak
  - Bit Strong
  - Strong
- Uses a loop so multiple passwords can be checked

## 🧠 Concepts Used

This project uses basic Python concepts:

- Variables
- Strings
- `input()` and `print()`
- `while` loop
- `for` loop
- `if`, `elif`, and `else`
- String methods:
  - `.isupper()`
  - `.islower()`
  - `.isdigit()`
- `string.punctuation`
- Counters
- Basic conditions

## ⚙️ How It Works

1. The user enters a password.
2. The program first checks whether the password has at least 8 characters.
3. If the password is long enough, the program checks each character.
4. It counts whether the password contains:
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters
5. Each satisfied requirement adds 1 point to the total score.
6. The final score determines the password strength.

### Strength System

| Requirements Satisfied | Rating |
|---|---|
| 1 | Very Weak |
| 2 | Weak |
| 3 | Bit Strong |
| 4 | Strong |

A password must have at least 8 characters before it is evaluated.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python password_strength_checker.py