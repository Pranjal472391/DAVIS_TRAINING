# Take input
n = int(input("Enter number: "))

# Initialize factorial
fact = 1

# Calculate factorial
for i in range(1, n + 1):
    fact *= i

# Print result
print("Factorial =", fact)