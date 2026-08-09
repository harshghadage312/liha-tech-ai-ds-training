"""Write a Python program to remove duplicate elements from a list.
Input [1, 2, 2, 3, 1, 4]
Expected Output [1, 2, 3, 4]"""
my_list=[1,2,3,3,4,5,6,6]
for i in my_list:
    if my_list.count(i)>1:
        my_list.remove(i)
print(my_list)
#we can also use set() like list(set(my_list))
