# Take input
text = input("Enter string: ")

# Initialize result
result = ""

# Convert manually
for ch in text:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)  # Convert to uppercase
    else:
        result += ch

# Print result
print("Uppercase:", result)