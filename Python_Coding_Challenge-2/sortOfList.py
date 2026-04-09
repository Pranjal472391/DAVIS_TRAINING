# Take input
nums = list(map(int, input("Enter numbers: ").split()))

# Bubble sort logic
for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            # Swap
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Print sorted list
print("Sorted list:", nums)