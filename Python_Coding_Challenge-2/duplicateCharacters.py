# Take input
text = input("Enter string: ")

# Track duplicates
seen = []
duplicates = []

for ch in text:
    if ch not in seen:
        seen.append(ch)
    elif ch not in duplicates:
        duplicates.append(ch)

# Print duplicates
print("Duplicates:", " ".join(duplicates))