# Take number input
num = int(input("Enter number: "))

# Check divisibility
if num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")