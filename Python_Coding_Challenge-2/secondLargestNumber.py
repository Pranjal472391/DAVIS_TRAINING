# Take input
nums = list(map(int, input("Enter numbers: ").split()))

# Remove duplicates
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)

# Find largest and second largest
max_val = unique[0]
second = unique[0]

for i in unique:
    if i > max_val:
        second = max_val
        max_val = i
    elif i > second and i != max_val:
        second = i

# Print result
print("Second largest =", second)