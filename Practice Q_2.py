"""A website requires the users to input username and password to register. Write a
program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
If the password matches all the criteria print it as Valid password or else print it as
Invalid password."""

password = input("Enter a password: ")

if len(password) < 6 or len(password) > 12:
    print("Invalid password")
else:
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True

if has_lowercase and has_uppercase and has_digit and has_special:
    print("Valid password")
else: 
    print("Invalid password")
