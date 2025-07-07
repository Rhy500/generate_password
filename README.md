# generate_password

# 🔐 Password Generator Program Report

## 1. Purpose of the Program

This program is designed to generate a random password with a user-defined length. The password consists of a combination of:

- Uppercase and lowercase letters
- Digits
- Special characters

If no input is provided, the default password length is **12 characters**, and the recommended **minimum length is 8 characters**.

---

## 2. Code Description

The program uses the following Python modules:

- `random` – to randomly select characters
- `string` – to access predefined character sets (letters, digits, punctuation)

### 🔧 Function: `gen(length)`

Generates a random password string of the specified length using the full character set.

### 🧩 Function: `main()`

- Prompts the user to input the desired password length.
- If no input is provided, sets the default length to 12.
- If the input length is less than 8, displays a warning.
- If the input is not a valid number, shows an error message.
- Displays the generated password on the screen.

---

## 3. Execution Frequency

There is **no limit** on how many times the password can be generated. Users can run the program:

- As many times as they want
- Each run will produce a **new, unique password**

The `gen()` function is reusable and can be executed in any loop or user session without restrictions.

---

## 📌 Example Output

```bash
Input: 10
Output: your password is : T8@h2Zk1!P

Input: 10
Output: your password is : r#8T6mPwZQ


----
## How to Run the Program

You have to download python, and if you want to run it, open terminal or cmd
```bash
python pass1.py
