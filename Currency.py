amount=int(input("Enter the amount: "))
notes=[2000,500,200,100,50,20,10,5]
notecount=[0,0,0,0,0,0,0,0]
print("Currency Count ")
for i,j in zip(notes,notecount):
   if amount>=i:
       j=amount//i
       amount = amount-j*i
       print(i," : ",j)
