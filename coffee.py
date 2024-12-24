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



#Check resources when there is an order
#Create deposit for money from user, quarters dimes, penny, nickles
#check if transaction successful and give change if needed or deny
#Make coffee
#Enjoy coffee after drink is made
#turn off button (exit loop)
on = True

espresso = "espresso"
latte = "latte"
cappuccino = "cappuccino"
price = "cost"
def get_cost(coffee):
    return MENU[coffee][price]

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
    #         return False
    # return True
    return score


def make_drink(drink):
    for resource in resources:
        resources[resource] -= get_coffee_resources(drink, resource)


while on:
    # startup()
    current_order = startup()
    if current_order == "report":
        report(resources)
    elif current_order == "refill":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        print("Success. Machine has been refilled!")
        report(resources)

    elif check_resource() == 3:
        make_drink(current_order)
    else:
        print("Please type refill to refill all.")



    report(resources)
