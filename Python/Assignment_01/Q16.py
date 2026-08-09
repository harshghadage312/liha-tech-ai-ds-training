#Write a Python program to capitalize the first letter of every word in a sentence without using title().
sentence=input("enter the sentence: ")
words=sentence.split()
capitalized_words=[]
for word in words:
    capitalized_words.append(word.capitalize())
capitalized_sentence=" ".join(capitalized_words)
print("sentence with capitalized first letters is : ",capitalized_sentence)