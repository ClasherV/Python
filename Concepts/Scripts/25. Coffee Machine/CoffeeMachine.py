import Resources
import Recipe
def checkResources(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item]>Resources.resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def processCoins():
    print("Enter the Coins: ")
    total=0
    coins_five=int(input("How many RS.5 Coins?: "))
    coins_ten=int(input("How many RS.10 Coins?: "))
    coins_twenty=int(input("How many RS.20 Coins?: "))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def isPaymentSuccessful(payment,coffee_cost):
    if payment>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=payment-coffee_cost
        print(f"Here is Your RS.{change} in Change")
        return True
    else:
        print("Sorry that's not enoug Money. Money Refunded")
        return False
def makeCoffee(coffee_type,coffee_ingredients):
    for item in coffee_ingredients:
        Resources.resources[item]-=coffee_ingredients[item]
    print(f"Here is Your {coffee_type} ☕")
is_on=True
profit=0
while is_on:
    choice=input("What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: ").lower()
    if choice=='off':
        is_on=False
    elif choice=='report':
        print(f"Water: {Resources.resources['water']} ml")
        print(f"Milk: {Resources.resources['milk']} ml")
        print(f"Coffee: {Resources.resources['coffee']} g")
        print(f"Money: {profit}Rs.")
    else:
        coffee_type=Recipe.menu[choice]
        if checkResources(coffee_type['ingredients']):
            payment=processCoins()
            if isPaymentSuccessful(payment,coffee_type['cost']):
                makeCoffee(choice,coffee_type['ingredients'])

""" 
O/p: What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: laTte
     Enter the Coins: 
     How many RS.5 Coins?: 10
     How many RS.10 Coins?: 10
     How many RS.20 Coins?: 10
     Here is Your RS.200 in Change
     Here is Your latte ☕
     What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: Cappuccino
     Enter the Coins: 
     How many RS.5 Coins?: 10
     How many RS.10 Coins?: 10
     How many RS.20 Coins?: 10
     Here is Your RS.150 in Change
     Here is Your cappuccino ☕
     What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: espresso
     Enter the Coins: 
     How many RS.5 Coins?: 10
     How many RS.10 Coins?: 10
     How many RS.20 Coins?: 10
     Here is Your RS.250 in Change
     Here is Your espresso ☕
     What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: report
     Water: 1500 ml
     Milk: 750 ml
     Coffee: 434 g
     Money: 450Rs.
     What would You like to have? (Latte/Espresso/Cappuccino) or Type Report for a Report and Off to Shut down the Machine: off
"""