# Take input
n = int(input("Enter number: "))

# Loop from 1 to n
for i in range(1, n + 1):
    # Check even number
    if i % 2 == 0:
        print(i, end=" ")