from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            print("Sorry, that drink is not available. Please choose a valid option.")
        else:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


# print(select)
