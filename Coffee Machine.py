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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def total():
    print('Please insert coins.')
    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickles = float(input('How many nickles?: '))
    pennies = float(input('How many pennies?: '))
    total = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    if total < MENU[CHOICE]["cost"]:
        print("Sorry that's not enough money. Money Refunded.")
    elif total > MENU[CHOICE]["cost"]:
        change = (total - MENU[CHOICE]["cost"]) 
        rounded = round(change, 2)
        print(f"Here is ${rounded} in change.")
        print(f"Here is your {CHOICE}. Enjoy")


coffee_machine = True

while coffee_machine is True:
    CHOICE = input("What would you like? (espresso/latte/cappuccino):")

    if CHOICE == "off":
        coffee_machine = False
    elif CHOICE == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif CHOICE == "espresso":
        if resources["water"] < MENU[CHOICE]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU[CHOICE]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            total()
            resources["water"] = resources["water"] - MENU[CHOICE]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[CHOICE]["ingredients"]["coffee"]
            profit = MENU[CHOICE]["cost"]
    elif CHOICE == "latte":
        if resources["water"] < MENU[CHOICE]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU[CHOICE]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU[CHOICE]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            total()
            resources["water"] = resources["water"] - MENU[CHOICE]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[CHOICE]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[CHOICE]["ingredients"]["coffee"]
            profit = MENU[CHOICE]["cost"]
    elif CHOICE == "cappuccino":
        if resources["water"] < MENU[CHOICE]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU[CHOICE]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU[CHOICE]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            total()
            resources["water"] = resources["water"] - MENU[CHOICE]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU[CHOICE]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU[CHOICE]["ingredients"]["coffee"]
            profit = MENU[CHOICE]["cost"]
