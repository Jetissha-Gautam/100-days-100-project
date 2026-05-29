from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
Menu=Menu()
CoffeeMaker=CoffeeMaker()
MoneyMachine=MoneyMachine()
ON=True
while ON:
    print("What would you like to have?")
    print(Menu.get_items())
    choice=input().lower()
    x=Menu.find_drink(choice)
    if choice=='report':
        CoffeeMaker.report()
        MoneyMachine.report()    

    elif CoffeeMaker.is_resource_sufficient(x):
        if MoneyMachine.make_payment(x.cost) :
            CoffeeMaker.make_coffee(x)
    elif choice=="off":
        ON=False
