from resource import MENU, resources


is_on = True

profit = 0


def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        return resources[item]
    print(f"Here is your drink {drink}")


def is_resources_sufficient(ingredients):
    """ Return resources are sufficient or not"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_payment_sufficient(drink_cost, payment_received):
    """ Return payment is sufficient or not"""
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is your change ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry Not enough money, going to refund money")
        return False


def process_coins():
    """ Return calculated Total from process coins"""
    print("Please insert coins")
    total = int(input("How many quarters ?")) * 0.25
    total += int(input("How many dimes ?")) * 0.10
    total += int(input("How many nickles ?")) * 0.05
    total += int(input("How many pennies ?")) * 0.01
    return total


while is_on:
    userOrder = input("What would you like? (espresso/latte/cappuccino):").lower()
    if userOrder == "off":
        is_on = False
    elif userOrder == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        productIngredients = MENU[userOrder]["ingredients"]
        productCost = MENU[userOrder]["cost"]

        if is_resources_sufficient(productIngredients):
            customerPayment = process_coins()
            paymentStatus = is_payment_sufficient(productCost, customerPayment)

            if paymentStatus:
                valueee = make_coffee(userOrder, productIngredients)
