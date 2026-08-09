#Write a Python program to replace all occurrences of a specified word in a sentence with another word.
sentence=input("enter the sentence: ")
word_to_replace=input("enter the word to replace: ")
replacement_word=input("enter the word to replacewith: ")
new_sentence=sentence.replace(word_to_replace,replacement_word)
print("orignal sentence is : ",sentence)
print("new sentence is : ",new_sentence)