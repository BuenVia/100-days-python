from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_list = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

is_active = True

while is_active:
    user_choice = input(f"What would you like to drink? {menu_list.get_items()}: ")

    if user_choice == 'off':
        print("Machine switched off.")
        is_active = False
    elif user_choice == 'report':
        maker.report()
        money.report()
    else:
        drink = menu_list.find_drink(user_choice)
        if not drink:
            is_active = False
        else:
            resource = maker.is_resource_sufficient(drink)
            if resource:
                payment = money.make_payment(drink.cost)
                if payment:
                    maker.make_coffee(drink)