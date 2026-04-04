maths = int(input("Enter your maths marks:"))
phy= int(input("Enter your Physics marks:"))
chem = int(input("Enter your Chemistry marks:"))

if(maths >=35 and phy >=35):
  print("Pass")
elif(maths>=35 and chem >=35):
  print("pass")
elif(chem>=35 and phy >=35):
  print("pass")
else:
  print("Fail")
