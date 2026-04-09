# Take input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Sort both strings
if sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")