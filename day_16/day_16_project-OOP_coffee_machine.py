from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money_transaction = MoneyMachine()
drinks_menu = Menu()

running = True

while running:
    customer_order = input(
        f"​What would you like? ({drinks_menu.get_items()}): ").lower()
    if customer_order == "off":
        running = False
    elif customer_order == "report":
        coffee_machine.report()
        money_transaction.report()
    else:
        customer_drink = drinks_menu.find_drink(customer_order)
        if coffee_machine.is_resource_sufficient(customer_drink):
            if money_transaction.make_payment(customer_drink.cost):
                coffee_machine.make_coffee(customer_drink)
