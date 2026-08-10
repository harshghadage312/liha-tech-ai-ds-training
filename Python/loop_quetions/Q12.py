"""Write a Python program to find first and last digit of a number."""
num=int(input("enter the number: "))
last_digit=num%10
while num>=10:
    num=num//10
first_digit=num
print("first digit of the number is:", first_digit)
print("last digit of the number is:", last_digit)