#Write a Python program to check whether a character is uppercase or
#lowercase alphabet.
char=input("enter the character: ")
if char.isupper():
    print(char," is uppercase")
elif char.islower():
    print(char," is lowercase")
else:
    print(char," is not an alphabet")