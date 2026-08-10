"""Write a Python program to calculate product of digits of a number."""
n = int(input("Enter the number: "))
prod_digit = 1

while n > 0:
    digit = n % 10
    prod_digit *= digit
    n //= 10

print("Product of digits is:", prod_digit)