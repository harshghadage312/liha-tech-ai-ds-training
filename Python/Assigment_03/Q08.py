"""Write a Python program to find the second largest number in a list.
Input [10, 40, 20, 30, 50]
Expected Output Second largest = 40"""
my_list=[10,40,20,30,50]
my_list.sort()
print("Second largest =", my_list[-2])