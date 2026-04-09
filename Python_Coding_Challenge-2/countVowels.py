# Take input string
text = input("Enter string: ").lower()

# Initialize counter
count = 0

# Loop through characters
for ch in text:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        count += 1

# Print result
print("Vowels =", count)