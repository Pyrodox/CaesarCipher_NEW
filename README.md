# CaesarCipher_NEW -> CaesarCipher.py is the MAIN file.

This cipher shifts 15 to the right for the alphabet and 3 to the right for numbers.
Make sure to create an __init__.py file for the Restart_Function module.

This Caesar Cipher alphabetically shifts 15 to the right and converts the letter to a different case (lower case or upper case). The numbers shift to the right 3 units. The comma encrypts into a period, and a period is encrypted into a comma.

I originally got the idea from a friend who also had an encryption program on their repl.it profile. I used this website to come up with a dictionary for my program, which included a shift 15 alphabetical: https://crypto.interactive-maths.com/caesar-shift-cipher.html

The encryptor/decryptor includes:

encoding/decoding function based on what the user chooses
user can also restart the program or break the program after their message is encrypted/decrypted.
If user enters a wrong input for their message that will get converted, question that asks to encrypt/decrypt, or the question that asks to restart or quit, then the program prints "Invalid Input. Please try again." and loops back.
2 different dictionaries for encrypt and decrypt
useage of while True loops for many sections of the user's usage of the tool.
New module to shorten the code in the main.
A class added to practice OOP.
