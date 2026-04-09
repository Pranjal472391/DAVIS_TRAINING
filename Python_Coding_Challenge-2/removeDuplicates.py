# Take input list
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Create empty list for unique elements
unique = []

# Remove duplicates
for i in nums:
    if i not in unique:
        unique.append(i)

# Print result
print("Without duplicates:", unique)