num=int(input("Enter the number to Count:"))
count=0
while(num>0):
    count+=1
    num=num//10
print(count)
