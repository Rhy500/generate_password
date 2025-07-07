# generate_password

PASSWORD GENERATOR PROGRAM REPORT
1. Purpose of the Program
This program is designed to generate a random password with a user-defined length. The password consists of a combination of uppercase and lowercase letters, digits, and special characters. The default password length is 12 characters if no input is provided, and the recommended minimum length is 8 characters.

2. Code Description
The code uses the following modules:

random – to randomly select characters.

string – to access predefined character sets (letters, digits, punctuation).

Function: gen(length)
This function generates a random password string of a specified length using the character set.

Function: main()
Prompts the user to input the desired password length.

If no input is provided, the default is set to 12 characters.

If the length is less than 8, a warning is displayed.

If the input is not a number, an error message is shown.

The generated password is printed to the console.

3. Execution Frequency
The password generation is not limited to a fixed number of times. Users can run the program:

As many times as they want.

Each time, it will generate a unique random password.

There is no limit on how often the gen() function can be used.
