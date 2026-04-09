# Take marks input
marks = int(input("Enter marks: "))

# Assign grade
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")