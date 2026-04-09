# Take dictionary input
students = {"A": 80, "B": 95, "C": 78}

# Assume first student is highest
top_student = list(students.keys())[0]

# Compare marks
for key in students:
    if students[key] > students[top_student]:
        top_student = key

# Print result
print("Top student =", top_student)