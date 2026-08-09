#Write a Python program to remove duplicate characters from a string while preserving the original order.
string=input("enter the string: ")
unique_chars=" "
for char in string:
    if char not in unique_chars:
        unique_chars+=char
print("string after removing duplicate characters is : ",unique_chars)