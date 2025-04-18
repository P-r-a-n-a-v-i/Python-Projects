MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients) :
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough water{item}")
            return False
    return True        

def is_transanction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is your change Rs.{change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's not enough money. money refunded.")
        return False

def process_coins():
    print("pls insert coin ")
    total = 0
    total = int(input("enter 5ru. coins"))
    total = int(input("enter 10ru. coins"))
    total = int(input("enter 20ru. coins"))
    return total   

def make_cofee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")    

is_on = True

while is_on:
  choice = input("what would you like? (espresso/cappuccino/latte): ")
  if choice == "off":
     is_on = False
  elif choice == "report":
    print(f"water = {resources['water']}ml")
    print(f"milk = {resources['milk']}ml")
    print(f"cofee = {resources['coffee']}g")
    print(f"money= Rs{profit}")
  else:
      drink = MENU[choice]
      if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if is_transanction_successful(payment, drink["cost"]):
            make_cofee(choice, drink["ingredients"])

      


    
        


