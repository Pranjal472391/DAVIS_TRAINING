# Take number of elements from user
n = int(input("Enter how many numbers: "))

# Create empty list
nums = []

# Take inputs from user
for i in range(n):
    num = int(input("Enter number: "))
    nums.append(num)   # Add number to list

# Assume first element is maximum
max_val = nums[0]

# Compare all elements
for i in nums:
    if i > max_val:
        max_val = i   # Update maximum

# Print result
print("Maximum =", max_val)