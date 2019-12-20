num = int(input(" Enter the Number: "))
for n in range(1,num):
        Sum = 0
        for i in range(1, n):
            if(n % i == 0):
                Sum = Sum + i
        if (Sum == n):
             print(n," is a Perfect Number")

                
