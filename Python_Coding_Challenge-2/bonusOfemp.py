#Write a python program to calculate the bonus amount of an employee based on the following criteria:
#input:45000
#Output Bonus = 3150
def calculate_bonus(salary):  
    if salary <= 50000:
        bonus = salary * 0.05     
    else:

        bonus = salary * 0.07
    return bonus
salary = float(input("Enter the salary of the employee: "))
bonus_amount = calculate_bonus(salary)
print("Bonus = ", bonus_amount)
    