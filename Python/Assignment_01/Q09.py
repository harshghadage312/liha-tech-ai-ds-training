#Write a Python program to find the first occurrence and last occurrence of a character in a string.
s=input("enter the string: ")
c=input("enter the character to find: ")
first=1
last=-1
for i in range(len(s)):
    if s[i]==c:
        if first==1:
            first=i
        last=i
if first==1:
    print("character not found in string")
else:
    print("first occurrence of character ",c," is at index: ",first)
    print("last occurrence of character ",c," is at index: ",last)