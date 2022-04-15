# Import art and os
import calculator_art
import os


# Defines addition function
def add(n1, n2):
    return n1 + n2


# Defines subtration function
def sub(n1, n2):
    return n1 - n2


# Defines multiplication function
def mult(n1, n2):
    return n1 * n2


# Defines division function
def div(n1, n2):
    return n1 / n2


# Creates a operations dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}


# Defines calculation function
def calculate(num1=None):
    # Asks for input
    if num1 == None:
        num1 = float(input("What's the first number? "))
    op = input(
        f"Choose an operation ({', '.join(key for key in operations)}): ")
    num2 = float(input("What's the next number? "))
    # Performs the calculation
    answer = operations[op](num1, num2)
    # Prints result
    print(f"{num1} {op} {num2} = {answer}")
    return answer


# Run the calculator
running = True
number = None
while running:
    if number == None:
        print(calculator_art.logo)
        number = calculate()
    else:
        run = input(
            f"Type 'y' to continue calculating with {number}, 'n' to start a new calculation, or any other key to exit: ")
        if run == "y":
            number = calculate(num1=number)
        elif run == "n":
            number = None
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            running = False
