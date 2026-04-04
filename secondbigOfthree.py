a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if((a > b and a<c) or (a>c and a<b)) :
  print(f"{a} is biggest")
elif((b>a and b <c) or (b>c and b<a)):
  print(f"{b} is biggest")
else:
  print(f"{c} is biggest")
