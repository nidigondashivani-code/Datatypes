number = int(input("Enter a number: "))

is_square = False

for i in range(1, number + 1):
    if i * i == number:
        is_square = True
        break

if is_square:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
