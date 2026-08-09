#Write a Python program to count total number of notes in given amount.using if else.
amount=int(input("enter the amount: "))
if amount>=2000:
    notes_2000=amount//2000
    amount=amount%2000
    print("number of 2000 notes are: ",notes_2000)
if amount>=500:
    notes_500=amount//500
    amount=amount%500
    print("number of 500 notes are: ",notes_500)
if amount>=100:
    notes_100=amount//100
    amount=amount%100
    print("number of 100 notes are: ",notes_100)
if amount>=50:
    notes_50=amount//50
    amount=amount%50
    print("number of 50 notes are: ",notes_50)
if amount>=20:
    notes_20=amount//20
    amount=amount%20
    print("number of 20 notes are: ",notes_20)
