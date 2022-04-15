# Inicial dictionaries and variables
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def order():
    """Takes customer's order"""
    return input("​What would you like? (espresso/latte/cappuccino): ").lower()


def report():
    """Generates resources report"""
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")


def check_resources(drink):
    """Checks if there are enough resources to make the coffee"""
    for item in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Process the value of the coins inserted"""
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    coins = (quarter * 0.25) + (dimes * 0.10) + \
        (nickles * 0.05) + (pennies * 0.01)
    return coins


def check_transaction(drink):
    """Checks if the user has inserted enough money to purchase the selected drink"""
    global money
    change = process_coins() - MENU[drink]['cost']
    if change > 0:
        money += MENU[drink]['cost']
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def deduct_resources(drink):
    """Deducts the ingredients used to make the drink from resources"""
    for item in MENU[drink]['ingredients']:
        new_value = resources[item] - MENU[drink]['ingredients'][item]
        resources[item] = new_value


def make_coffee():
    """Runs the coffee machine and makes the coffee"""
    status = True
    while status:
        drink = order()
        if drink == "report":
            report()
        elif drink == "off":
            status = False
        else:
            if check_resources(drink):
                if check_transaction(drink):
                    deduct_resources(drink)
                    print(f"Here is your {drink}. Enjoy!")


make_coffee()
