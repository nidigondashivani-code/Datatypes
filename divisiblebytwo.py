number = int(input("Enter a number:"))
if(number % 2 ==0):
  print(f"{number} is divisible by 2")
elif(number %3 ==0):
  print(f"{number} is divisible by 3")
elif(number % 6==0):
  print(f"{number} is divisible by 6")
else:
  print(f"{number} is not divisible by 2,3 and 6")
