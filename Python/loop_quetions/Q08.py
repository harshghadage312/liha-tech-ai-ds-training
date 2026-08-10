"""Write a Python program to find sum of all odd numbers between 1 to n."""
n=int(input("enter the number: "))
sum=0
for i in range(n+1):
    if i %2!=0:
        sum+=i
print("addition of odd number is : ",sum)