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

quarter = 0.25
dime = 0.10
penny = 0.01
nickle = 0.05
on = True
espresso = "espresso"
latte = "latte"
cappuccino = "cappuccino"
price = "cost"
#Ask user what they would like
def startup():
    print("Welcome to the best Coffee Machine!")
    order = input("We offer espresso, cappuccino, and latte! Pick from the 3 and type what you want!")
    # if order == "report":
    #     report(resources)
    # else:
    return order

#Print report on resources
def report(resources):
    print(f"You have water: {resources["water"]} ml")
    print(f"You have milk: {resources["milk"]} ml")
    print(f"You have coffee: {resources["coffee"]} ml")

def get_cost(coffee):
    return MENU[coffee][price]

def get_payment():
    paid = 0
    print("Please insert coins to pay. We only accept quarters, dimes, nickles, and pennies.")
    quarter_count = int(input("How many quarters will you insert:"))
    dime_count = int(input("How many dimes will you insert:"))
    nickle_count = int(input("How many nickles will you insert:"))
    penny_count = int(input("How many pennies will you insert:"))
    paid = (quarter_count * quarter) + (dime_count * dime) + (nickle_count * nickle) + (penny_count * penny)
    return paid

def get_coffee_resources(coffee, liquid):
    if liquid not in MENU[coffee]["ingredients"]:
        return 0
    return MENU[coffee]["ingredients"][liquid]

def get_resource(liquid):
    return resources[liquid]

def check_resource():
    score = 0
    for resource in resources:
        check_resources = resources[resource]
        check_coffee = get_coffee_resources(current_order, resource)
        if check_resources >= check_coffee:
            score += 1
        else:
            print(f"Not enough {resource}. Try again later.")
    return score

def make_drink(drink):
    for resource in resources:
        resources[resource] -= get_coffee_resources(drink, resource)
    print("\n" * 5)
    print("Enjoy your drink!!!!")

while on:
    current_order = startup()
    if current_order == "report":
        report(resources)
        
    elif current_order == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Success. Machine has been refilled!")
        report(resources)
    elif current_order == "off":
        print("Machine turning off....")
        break

    elif check_resource() == 3:
        total = get_cost(current_order)
        print(f"Your total is ${total}")
        paid = get_payment()
        if total == paid:
            make_drink(current_order)
        elif total < paid:
            change = paid - total
            change = round(change, 2)
            print(f"Here is your change ${change}")
            make_drink(current_order)
        else:
            print("Not enough monnies. Try again")
            continue

    else:
        print("Please type refill to refill all.")
        print("Current Report: \n")
        report(resources)
