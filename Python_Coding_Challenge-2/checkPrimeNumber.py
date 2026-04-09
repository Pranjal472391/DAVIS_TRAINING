# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Take input
num = int(input("Enter number: "))

# Call function
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")