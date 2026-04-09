# Take day input
day = input("Enter day: ").lower()
# Check ticket price
if day in ['saturday', 'sunday']:
    print("Ticket Price: $20")
elif day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print("Ticket Price: $10")
else:
    print("Invalid day")
        