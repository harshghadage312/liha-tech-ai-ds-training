#Write a Python program to count the frequency of a given character in a string.
s=input("enter the string: ")
c=input("enter the character to count: ")
count=0
for i in s:
    if i==c:
        count+=1
print("frequency of character ",c," in string is: ",count)