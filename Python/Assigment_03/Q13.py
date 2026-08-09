"""Write a Python program to separate positive and negative numbers from a list.
Input [-5, 3, -2, 7, 0, -1]
Expected Output Positive = [3, 7]
Negative = [-5, -2, -1]"""
my_list = [-5, 3, -2, 7, 0, -1]
positive = []
negative = []
for num in my_list:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print("Positive numbers:", positive)
print("Negative numbers:", negative)