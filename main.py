from resources import resources
from resources import MENU

machine_on = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
profit = 0.00


def print_report():
    """Displays the current available resources"""
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"${profit}")


def check_resources(drink_type, water, milk, coffee):
    """Based on the drink_type, this will compare the available water, milk,
     and coffee resources to what is needed for the drink"""
    resource_sufficient = True
    if water < drink_type["ingredients"]["water"]:
        print("Not enough water. Please add more.")
        resource_sufficient = False
    if drink_type != MENU["espresso"]:
        if milk < drink_type["ingredients"]["milk"]:
            print("Not enough milk. Please add more.")
            resource_sufficient = False
    if coffee < drink_type["ingredients"]["coffee"]:
        print("Not enough coffee. Please add more.")
        resource_sufficient = False

    return resource_sufficient


def process_coins(money):
    """Allows the user to insert coins, which are then added to the user's available 'money'"""
    coins = input("Please insert your coins (Separated by commas):\n")
    for coin in coins.split(', '):
        if coin == "quarter" or coin == 'q':
            money += 0.25
        elif coin == "dime" or coin == 'd':
            money += 0.10
        elif coin == "nickle" or coin == 'n':
            money += 0.05
        elif coin == "penny" or coin == 'p':
            money += 0.01
    return money


def check_transaction_successful(drink_type, money):
    """Checks the amount of money put in and runs that against the cost of the drink"""
    cost = drink_type["cost"]
    refund = 0.00
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        money = 0.00
        return money
    elif money == cost:
        return money
    elif money > cost:
        refund += round(money - cost, 2)
        print(f"You paid ${round(money, 2)}, and the cost was ${round(cost, 2)}.")
        money -= refund
        print(f"Your refund is ${refund}.")
        return money


# make_coffee()


while machine_on:
    money = 0.00
    user_input = (input("What would you like? (espresso/latte/cappuccino)\n")).lower()
    if user_input == "espresso":
        drink_type = MENU[user_input]
        resource_availability = check_resources(drink_type, water, 0, coffee)
        if resource_availability:
            print("Can make your espresso")
            money += round(process_coins(money), 2)
            profit += round(check_transaction_successful(drink_type, money), 2)
            # make_coffee()
        else:
            break
    elif user_input == "latte":
        drink_type = MENU[user_input]
        resource_availability = check_resources(drink_type, water, milk, coffee)
        if resource_availability:
            print("Can make your latte")
            money += round(process_coins(money), 2)
            profit += round(check_transaction_successful(drink_type, money), 2)
            # make_coffee()
        else:
            break
    elif user_input == "cappuccino":
        drink_type = MENU[user_input]
        resource_availability = check_resources(drink_type, water, milk, coffee)
        if resource_availability:
            print("Can make your cappuccino")
            money += round(process_coins(money), 2)
            profit += round(check_transaction_successful(drink_type, money), 2)
            # make_coffee()
        else:
            break
    elif user_input == "off":
        print("Goodbye")
        machine_on = False
    elif user_input == "report":
        print_report()
    else:
        print("You did not enter a valid choice. Please enter your option again.")