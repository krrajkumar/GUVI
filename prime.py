list=[]
print("Enter the number ")
number = int(input())
for i in range(0,number):
 val=int(input())
 list.append(val)
 
 if val>1:
  for i in range(2,val):
   if(val%i)==0:
    print(val,"is not a prime number")
    break
   else:
    print(val,"is prime")
    break
 else:
  print(val,'is not prime')
print(list)
