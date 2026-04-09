# Take input
num = int(input("Enter number: "))

# Store original number
original = num

# Reverse number
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

# Check palindrome
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")