# Take two lists as input
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

# Find common elements
common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

# Print result
print("Common elements:", common)