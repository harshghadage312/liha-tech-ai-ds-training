"""Write a Python program to reverse a list without using the reverse() method.
Input [10, 20, 30, 40]
Expected Output [40, 30, 20, 10]"""
my_list=[10, 20, 30, 40]
reversed_list=[]
for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])
print(reversed_list)