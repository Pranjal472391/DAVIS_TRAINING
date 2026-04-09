# Take input list
nums = list(map(int, input("Enter numbers: ").split()))

# Rotate list
last = nums[-1]  # Store last element

for i in range(len(nums) - 1, 0, -1):
    nums[i] = nums[i - 1]

nums[0] = last

# Print result
print("Rotated list:", nums)