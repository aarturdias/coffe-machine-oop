from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drink = Menu()
resources = CoffeeMaker()
payment = MoneyMachine()
is_on = True

while is_on:

    choice = (input("Choose your drink: (espresso/latte/cappuccino): "))
    if choice == "off":
        is_on = False
    elif choice == "report":
        resources.report()
        payment.report()
    else:
        chosen_drink = drink.find_drink(choice)
        if resources.is_resource_sufficient(chosen_drink) and payment.make_payment(chosen_drink.cost):
            resources.make_coffee(chosen_drink)
