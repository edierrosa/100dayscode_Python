# Prints greeting message
print("Welcome to the tip calculator.")

# Asks user for the total bill, percentage tip and number of people
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

# Calculates how much each person should pay
tip = total_bill * (percentage_tip / 100)
total_amount = total_bill + tip
split_bill = total_amount / num_people
## alternative: split_bill = (total_bill * (1 + (percentage_tip /100))) / num_people

# Prints how much each person should pay
print(f"Each person should pay: ${split_bill:.2f}")