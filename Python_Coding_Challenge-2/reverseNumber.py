# Take input
num = int(input("Enter number: "))

# Initialize reverse
rev = 0

# Reverse logic
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

# Print reversed number
print("Reversed =", rev)