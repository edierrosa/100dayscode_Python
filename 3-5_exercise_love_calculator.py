# Asks user's crush name and name
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names = (name1 + name2).lower()

# Check for the number of times the letters in the words TRUE and LOVE occurs
true_num = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_num = names.count("l") + names.count("o") + names.count("v") + names.count("e")

# Combines to calculate the score
score = int(str(true_num) + str(love_num))

# Interpres the score
if score < 10 and score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score <= 50 and score >= 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
