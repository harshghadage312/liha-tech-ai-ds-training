#Write a Python program to calculate profit or loss. Input is selling cost and
#actual cost.
selling_cost=int(input("enter the selling cost: "))
actual_cost=int(input("enter the actual cost: "))
if selling_cost>actual_cost:
    profit=selling_cost-actual_cost
    print("profit is: ",profit)
elif actual_cost>selling_cost:
    loss=actual_cost-selling_cost
    print("loss is: ",loss)
else:
    print("no profit, no loss")