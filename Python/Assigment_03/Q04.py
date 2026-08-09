"""Write a Python program to count even and odd numbers in a list.
Input [1, 2, 3, 4, 5, 6]
Expected Output Even count = 3, Odd count = 3"""
my_list=[1,2,3,4,5,6,7,8,9,10]
even_count=0
odd_count=0
for num in my_list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even count =",even_count,"odd count=  ",odd_count)
