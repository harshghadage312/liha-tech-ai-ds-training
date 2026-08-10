"""11. Write a Python program to count number of digits in a number."""
num=int(input("enter the number: "))
count=0
while num>0:
    num=num//10
    count+=1
print("number of digits in the number is:", count)
