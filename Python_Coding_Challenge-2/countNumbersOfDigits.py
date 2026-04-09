# Take input
num = int(input("Enter number: "))

# Initialize counter
count = 0

# Count digits
while num > 0:
    num = num // 10
    count += 1

# Print result
print("Digits =", count)