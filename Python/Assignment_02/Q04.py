#Write a Python program to check whether a number is divisible by 5 and 11
#or not.
num=int(input("enter the number: "))
if num%5==0 and num%11==0:
    print(num," is divisible by both 5 and 11")
else:
    print(num," is not divisible by both 5 and 11")