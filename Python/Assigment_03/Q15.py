"""Write a Python program to create a new list containing squares of all elements of a list.
Input [1, 2, 3, 4, 5]
Expected Output [1, 4, 9, 16, 25]"""
input_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in input_list]
print("Squared list:", squared_list)