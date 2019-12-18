units=int(input("please enter the number of units: "))
if (units<100):
    amount=units*1
    fixedcharge=30
elif(units<=200):
    amount=100+((units-100)*2)
    fixedcharge=40
elif(units<=300):
    amount=300+((units-200)*3)
    fixedcharge=50
elif(units<=400):
    amount=600+((units-300)*4)
    fixedcharge=55
elif(units<=500):
    amount=1000+((units-400)*5)
    fixedcharge=60
else:
    amount=1500+((units-500)*5.5)
    fixedcharge=70
total=amount+fixedcharge
print("the electricity bill = %.2f" %total)
