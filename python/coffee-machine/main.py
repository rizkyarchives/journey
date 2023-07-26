#A coffee machine program, my first program using OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

print("WELCOME TO THE COFFEE MACHINE KINDA THING! YEAAHH")
can_create_latte = True
can_create_espresso = True
can_create_cappucino = True
drink_list = menu.get_items()

while not (can_create_latte == False and can_create_cappucino == False and can_create_espresso == False):
    user_choice = input(f"What would you like? {drink_list}\n>")
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffeemaker.report()
        continue
    else:
        drink = menu.find_drink(user_choice)
        if drink == None:
            print("Your drink choice is not on our menu!")
            continue
        else:
            ingredient_sufficiency = coffeemaker.is_resource_sufficient(drink)
            if not ingredient_sufficiency:
                if drink.name == "latte":
                    can_create_latte = False
                elif drink.name == "espresso":
                    can_create_espresso = False
                elif drink.name == "cappuccino":
                    can_create_cappucino = False
                continue
            else:
                print(f"A {drink.name} costs ${drink.cost}.")
                paid = moneymachine.make_payment(drink.cost)
                if not paid:
                    continue
                else:
                    coffeemaker.make_coffee(drink)

print("We've either ran out of ingredients or you have chosen to turn off the machine.")
coffeemaker.report()
moneymachine.report()
print("Thank you for using the COFFE MACHINE KINDA THING!")