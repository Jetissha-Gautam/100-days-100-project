resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}
MENU = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.5
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
ON=True
while ON:
    cost=0
    choice=input(("What would you like? (espresso/latte/cappuccino):")).lower()
    if choice=="off":
        break
    if choice == 'report':
        for i in resources:
            print(i,resources[i])
        continue
    for i in coins:
        cost+=coins[i]*int(input("How many "+i+" ?"))
    change=cost-MENU[choice]['cost']
    if change>=0:
        print("Your change:",change)
        made=True
        for i in resources:
            if i!="money":   
                if resources[i]<MENU[choice][i]:
                    print("There are not enough resources")
                    print("Here's your refund",MENU[choice]['cost'])
                    made = False
                else:
                    resources[i]-=MENU[choice][i]
        if made:
            resources['money']+=MENU[choice]['cost']
            print("Here's your",choice,"!")
        
    else:
        print("Sorry! the money is not enough")