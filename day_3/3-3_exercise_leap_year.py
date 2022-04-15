# Asks user which year to check
year = int(input("Which year do you want to check? "))

# Checks if the given year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("Not a leap year.")