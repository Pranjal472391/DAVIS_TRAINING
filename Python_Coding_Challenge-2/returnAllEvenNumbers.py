# Function to get even numbers
def get_even(nums):
    result = []
    for i in nums:
        if i % 2 == 0:
            result.append(i)
    return result

# Input
nums = list(map(int, input("Enter numbers: ").split()))

# Call function
print("Even numbers:", get_even(nums))