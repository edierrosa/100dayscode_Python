# Prints a greeting message and asks user to input data
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Calculates the bill
bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
else:
    if size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

# Prints user's final bill
print(f"Your final bill is {bill}")
