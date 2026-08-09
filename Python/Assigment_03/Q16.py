"""Write a Python program to rotate a list by n positions.
Input List = [1, 2, 3, 4, 5]

n = 2

Expected Output Rotated list = [3, 4, 5, 1, 2]"""
my_list = [1, 2, 3, 4, 5]
n = int(input("Enter the number of positions to rotate: "))
rotated_list = my_list[n:] + my_list[:n]
print("Rotated list:", rotated_list)