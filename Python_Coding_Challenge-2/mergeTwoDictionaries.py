
# Input dictionaries
d1 = {"a": 1}
d2 = {"b": 2}

# Merge dictionaries
merged = {}

# Add first dictionary
for key in d1:
    merged[key] = d1[key]

# Add second dictionary
for key in d2:
    merged[key] = d2[key]

# Print result
print("Merged dictionary:", merged)