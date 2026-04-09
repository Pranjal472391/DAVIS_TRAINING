# Take input list
nums = list(map(int, input("Enter numbers: ").split()))

# Create empty dictionary
freq = {}

# Count frequency
for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Print result
print("Frequency:", freq)