#Write a Python program to count uppercase letters, lowercase letters, digits, and special characters in a
s=input("enter the string: ")
uppercase=0
lowercase=0
digits=0
special_chr=0
for i in s:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        digits+=1
    else:
        special_chr+=1
print("number of uppercase letters in string is: ",uppercase)
print("number of lowercase letters in string is: ",lowercase)
print("number of digits in string is: ",digits)
print("number of special characters in string is: ",special_chr)