"""Write a Python program to find common elements between two lists.
Input List 1 = [1, 2, 3, 4]
List 2 = [3, 4, 5, 6]
Expected Output Common elements = [3, 4]"""
l1=[1,2,3,4]
l2=[3,4,5,6]
common_elements=[]
for element in l1:
    if element in l2:
        common_elements.append(element)
print("common elements are: ",common_elements)