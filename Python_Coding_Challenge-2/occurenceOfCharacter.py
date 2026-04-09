# Take input
text = input("Enter string: ")
char = input("Enter character to count: ")

# Initialize counter
count = 0

# Loop through string
for ch in text:
    if ch == char:
        count += 1

# Print result
print("Occurrences =", count)