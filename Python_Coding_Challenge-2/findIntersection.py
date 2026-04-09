# Take input sets
set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

# Find intersection
intersection_set = set1.intersection(set2)

# Print result
print("Intersection:", intersection_set)