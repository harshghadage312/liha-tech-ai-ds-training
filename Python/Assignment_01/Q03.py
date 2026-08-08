#Write a Python program to count the number of vowels and consonants in a given string.
s=input("enter the string: ")
vowels=0
consonents=0
for i in s:
    if i in "aeiouAEIOU":
        vowels+=1
    elif i.isalpha():
        consonents+=1
print("number of vowels in string is: ",vowels)
print("number of consonents in string is: ",consonents)