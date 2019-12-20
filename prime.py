val=int(input("Enter the number:"))

if val > 1: 
       for n in range(2, val):
             if (val % n) == 0:
                print(val,"is not prime")
                break
       else: 
           print(val,'is prime')
    
