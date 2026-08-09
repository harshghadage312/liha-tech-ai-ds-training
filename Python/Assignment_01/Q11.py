#Write a Python program to check whether two strings are anagrams of each other.
str1=input("enter the sring 1: ")
str2=input("enter the string 2: ")
if sorted(str1) == sorted(str2):
    print("strings are anagrams")
else:
    print("string are not anagrams")
    