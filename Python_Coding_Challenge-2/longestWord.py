# Take input
text = input("Enter sentence: ")

# Split into words
words = text.split()

# Assume first word is longest
longest = words[0]

# Compare lengths
for word in words:
    if len(word) > len(longest):
        longest = word

# Print result
print("Longest word:", longest)