# Asks user's height and weight values
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Calculates BMI
bmi = float(weight) / (float(height) ** 2)

# Prints user's BMI
print(f"Your BMI is {int(bmi)}")
