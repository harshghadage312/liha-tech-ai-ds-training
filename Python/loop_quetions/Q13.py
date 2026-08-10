"""Write a Python program to find first and last digit of a number."""
num=int(input("enter the number: "))
last_digit=int(num%10)
while num>10:
    num=num//10
first_digit=int(num)
print("sum of first and last digit is : ",int(first_digit+last_digit))