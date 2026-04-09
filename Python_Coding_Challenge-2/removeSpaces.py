# Take input
text = input("Enter string: ")

# Remove spaces
result = ""

for ch in text:
    if ch != " ":
        result += ch

# Print result
print("Without spaces:", result)