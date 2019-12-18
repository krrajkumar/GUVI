even=[]
odd=[]
n=int(input("Enter the number of digits:"))
for i in range(0,n):
  num=int(input())
  if (num%2==0):
    even.append(num)
  else:
    odd.append(num)
print("Even number list" ,even)
print("odd number list",odd)
print("Sum of Even numbers",sum(even))
print("Sum of Odd numbers",sum(odd))

