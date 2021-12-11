# Asks user's current age
age = input("What is your current age? ")

# Calculates how many days, weeks, months until we reach 90 years old
days_left = (90 - int(age)) * 365
weeks_left = (90 - int(age)) * 52
months_left = (90 - int(age)) * 12

# Prints days, weeks and months left until 90 years old
print(f"You have {days_left} days, {weeks_left} weeks, or {months_left} months until 90.")