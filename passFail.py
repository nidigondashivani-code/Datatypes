phy = int(input("Enter your Physics marks:"))
maths = int(input("Enter your Mathematics marks:"))
chem = int(input("Enter your Chemistry marks:"))
if(phy >=35):
  if(maths >=35):
    if(chem >=35):
      print("pass")
    else:
      print("Fail")
  else:
    print("Fail")
else:
  print("Fail")
