# Take character input
ch = input("Enter character: ").lower()

# Check vowel
if ch in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Not Vowel")