#write a program to check whether the given number is odd or even using function.
#taking input from user
def odd_or_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = odd_or_even(number)

print(f"The number {number} is {result}.")

'''output:
Enter a number: 5
The number 5 is Odd.
Enter a number: 10
The number 10 is Even.
'''