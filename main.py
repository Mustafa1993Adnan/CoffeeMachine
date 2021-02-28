# import coffee types
from coffee_types import MENU, resources
# TODO: declare water,milk,coffee,profit
water = 0 ; milk = 0 ; coffee =0 ; profit = 0

# TODO: When the user enters “report” to the prompt
def resorces():
    print(f'water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\ncoffee: {resources["coffee"]}g\nmoney: {profit} ')
# TODO: Check resources sufficient
def sufficient_resources(water,milk,coffee):
    if water <= resources["water"] and milk <= resources["milk"] and coffee <= resources["coffee"] :
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee
        return True
    else:
        return False
# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino): and check the user input ”
def order_check(order):
    items = []
    for item in MENU:
        items.append(item)

    if order.isnumeric() and int(order) <= len(items):
        order = int(order) - 1
        order = items[order]
        order = order.replace("'", "")
        return order
    elif order.isnumeric() and int(order) > len(items) or order not in items:
        return False
    elif order in items:
        return order
# TODO: change the dictionary to list
def change_to_list():
    items = []
    for item in MENU:
        items.append(item)
    replace = '\''
    all_menu = str(items)[1:-1].replace(replace, "")
    return all_menu
# TODO : Running the programm
def coffee_machine():
    coffee_machine_status = True
    while coffee_machine_status:
        order = input(f'What would you like? ({change_to_list()}): ')
        if order == "report":
            resorces()
        elif order == "off":
            print("the coffee machine in the mantinance break.")
            coffee_machine_status = False
        else:
            order = (order_check(order))
            if order != False:
                total = coins_process()
                water = MENU[order]["ingredients"]["water"]
                milk = MENU[order]["ingredients"]["milk"]
                coffee = MENU[order]["ingredients"]["coffee"]
                if sufficient_resources(water,milk,coffee):
                    if total >= MENU[order]["cost"]:
                        change = round(total - MENU[order]["cost"],2)
                        global profit
                        profit += MENU[order]["cost"]
                        print(f"Here is your change: $ {change}")
                        print(f"Enjoy your coffee {order}")
                    else:
                        print("Sorry that's not enough money.")
                else:
                    print("Sorry there is not enough resources. money refunded")
            else:
                print(f"your order is out of range or not in the list ")



# TODO: Process coins.
def coins_process():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# call the program
coffee_machine()
