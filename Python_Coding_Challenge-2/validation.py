# Predefined username and password
correct_user = "admin"
correct_pass = "1234"

# Take input
username = input("Enter username: ")
password = input("Enter password: ")

# Verify login
if username == correct_user and password == correct_pass:
    print("Login Successful")
else:
    print("Invalid Credentials")