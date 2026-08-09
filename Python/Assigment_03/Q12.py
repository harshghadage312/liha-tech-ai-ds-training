"""Write a Python program to delete all occurrences of a given element from a list.
Input List = [1, 2, 3, 2, 4, 2]
Delete = 2
Expected Output [1, 3, 4]"""
my_list=list(input("enter the list: "))
delete_element=int(input("enter the element to delete: "))
while delete_element in my_list:
    my_list.remove(delete_element)
print("list after deleting all occurences of : ",delete_element,"is: ",my_list)