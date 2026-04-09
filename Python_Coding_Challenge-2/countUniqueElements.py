# Take input
nums = list(map(int, input("Enter numbers: ").split()))

# Create unique list
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

# Print count
print("Unique count =", len(unique))