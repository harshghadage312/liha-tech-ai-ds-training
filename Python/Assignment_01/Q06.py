#Write a Python program to reverse a string without using slicing.
s=input("enter the string: ")
rev=" "
for i in s:
    rev=i+rev
print("reversed string is: ",rev)