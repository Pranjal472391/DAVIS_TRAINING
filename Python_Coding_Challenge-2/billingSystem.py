# Function to calculate total
def total_bill(items):
    total = 0
    for price in items:
        total += price
    return total

# Take input
nums = list(map(int, input("Enter prices: ").split()))

# Call function
print("Total Bill =", total_bill(nums))