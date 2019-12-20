n=int(input("Enter the number:"))

for val in range(1, n + 1):  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val)
           
