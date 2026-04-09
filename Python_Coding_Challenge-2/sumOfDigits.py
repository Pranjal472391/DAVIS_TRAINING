# Take input
num = int(input("Enter number: "))

# Initialize sum
total = 0

# Calculate sum of digits
while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

# Print result
print("Sum of digits =", total)