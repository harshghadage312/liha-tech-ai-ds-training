#Write a Python program to find the most frequently occurring character in a string.
string=input("enter the string: ")
count={}
for char in string:
    count[char]=count.get(char,0)+1
max_count=0
most_frequent_char=''
for char in count:
    if count[char]>max_count:
        max_count=count[char]
        most_frequent_char=char

print("most frequently occurring character is : ",most_frequent_char)
print("frequency is : ",max_count)
