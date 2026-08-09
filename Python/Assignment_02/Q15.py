"""Write a Python program to input electricity unit charges and calculate total
electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.25/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 17% is added to the bill"""
units=int(input("enter the number of units: "))
if units<=50:
    bill=units*0.5
elif units<=150:
    bill=50*0.5+(units-50)*0.75
elif units<=250:
    bill=50*0.5+100*0.75+(units-150)*1.25
else:
    bill=50*0.5+100*0.75+100*1.25+(units-250)*1.50

# Adding surcharge
total_bill=bill+bill*0.17
print("Total electricity bill: Rs.", total_bill)