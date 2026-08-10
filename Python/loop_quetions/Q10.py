"""Write a Python program to print multiplication table of any number. Take
user input."""
n=int(input("take a number table: "))
for i in range(11):
    if i==0:
        print("multipliaction table of : ",n)
    else:
       
       print(i*n)