sub1=int(input("Enter the Mark for sub1:"))
sub2=int(input("Enter the Mark for sub2:"))
sub3=int(input("Enter the Mark for sub3:"))
sub4=int(input("Enter the Mark for sub4:"))
sub5=int(input("Enter the Mark for sub5:"))
total=(sub1+sub2+sub3+sub4+sub5)/5
print(total)
if (total>=90):
 print("you got A Grade")
elif(total>=80):
  print("you got B Grade")
elif(total>=70):
  print("you got C Grade")
elif(total>=60):
  print("you got D Grade")
elif(total>=50):
  print("you got E Grade")
else:
  print("you got F Grade")