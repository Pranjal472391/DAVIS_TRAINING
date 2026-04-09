# Take input list
nums = list(map(int, input("Enter numbers: ").split()))

# Find expected sum
n = len(nums) + 1
expected_sum = n * (n + 1) // 2

# Actual sum
actual_sum = sum(nums)

# Missing number
missing = expected_sum - actual_sum

print("Missing number =", missing)