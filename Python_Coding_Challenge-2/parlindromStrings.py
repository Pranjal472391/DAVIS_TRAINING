# Take input
text = input("Enter string: ")

# Reverse string using slicing
rev = text[::-1]

# Check palindrome
if text == rev:
    print("Yes")
else:
    print("No")