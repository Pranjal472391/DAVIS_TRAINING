# Take input
text = input("Enter string: ").lower()

# Initialize result
result = ""

# Replace vowels
for ch in text:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        result += "*"
    else:
        result += ch

# Print result
print("Result:", result)