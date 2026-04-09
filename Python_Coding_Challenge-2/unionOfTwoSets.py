# Take input sets
set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

# Find union
union_set = set1.union(set2)

# Print result
print("Union:", union_set)