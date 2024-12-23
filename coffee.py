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
    if order == "report":
        report()
    else:
        return order

#Print report on resources
def report():
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
    return MENU[coffee]["ingredients"][liquid]

def get_resource(liquid):
    return resources[liquid]

def check_resource():
    for i in resources:
        check_resource = resources[i]
        check_coffee = get_coffee_resources(latte, i)
        if check_resource > check_coffee:
            continue
        else:
            print(f"Not enough {i}. Try again later.")
            return False

while on:
    # startup()
    current_order = startup()
    if current_order =="latte":
        print("Preparing order...Please wait")
        #checking resources
        check_resource()
        if check_resource() != False:
            print("Here is your drink! ()]")
            for i in resources:
                resources[i] -= get_coffee_resources(latte, i)
        else:
            print("Please refill machine.")

        report()
