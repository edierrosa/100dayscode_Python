# Import modules
import random 

# Asks for input and split the string into a list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Selects the index of who's going to pay the bill
index = random.randint(0, len(names) - 1)

# Prints the name of who is going to pay
# Alternative print(f"{random.choice(names)} is going to buy the meal today!")
print(f"{names[index]} is going to buy the meal today!")


