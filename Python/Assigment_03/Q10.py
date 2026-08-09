"""Write a Python program to search for an element in a list.
Input List = [10, 20, 30, 40]
Search = 30
Expected Output 30 found at index 2"""
my_list=[10,20,30,40]
search_element=30
if search_element in my_list:
    index=my_list.index(search_element)
    print(search_element,"found at index",index)
    
