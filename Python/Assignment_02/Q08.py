#Write a Python program to input any alphabet and check whether it is
#vowel or consonant.
char=input("enter the character: ")
if char in "aeiouAEIOU":
    print(char," is vowel")
else:
    print(char," is consonant")