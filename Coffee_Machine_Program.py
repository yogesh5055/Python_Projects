## Coffee Machine Program
print(r"""
==============WELCOME TO COFFEE MACHINE===================

 (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \
\_____________________/

""")
#RESOURCES

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0

#MENU

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def remaining_amount(total,user_input):
    
    return total-MENU[user_input]['cost']


def coin_count(user_input):
    print("Please insert coins.")
    quarters=int(input("How many quarters?:"))
    dimes=int(input("How many dimes?:"))
    nickles=int(input("How many nickles?:"))
    pennies=int(input("How many pennies?:"))
    total=(0.25*quarters)+(0.10*dimes)+(0.5*nickles)+(0.1*pennies)
    if total>MENU[user_input]['cost']:
        change=remaining_amount(total,user_input)
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {user_input} Enjoy!")
        global money
        money+=MENU[user_input]['cost']
    elif total==MENU[user_input]['cost']:
        print(f"Here is your {user_input} ☕ Enjoy!")
        money+=MENU[user_input]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
        
    
    
def report():
    print(f"Water :{resources['water']}ml\nMilk :{resources['milk']}ml\nCoffee :{resources['coffee']}g\nMoney :${round(money,2)}\n")

    
#Fuction for lette
is_done=False

def flavour(user_input):
    if resources['water']>=MENU[user_input]["ingredients"]['water'] :
        if resources['milk']>=MENU[user_input]["ingredients"]['milk']:
      
            if resources['coffee']>=MENU[user_input]["ingredients"]['coffee'] :
                resources['water']-=MENU[user_input]["ingredients"]['water']
                resources['milk']-=MENU[user_input]["ingredients"]['milk'] 
                resources['coffee']-=MENU[user_input]["ingredients"]['coffee']
                global is_done
                is_done=True
                
            else:
                print("Sorry there is not enough coffee.")
        else: 
            print("Sorry there is not enough milk.")
    else: 
        print("Sorry there is not enough water.")

machine_off=False       
while not machine_off:          
    user_input= input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == 'latte' or user_input == 'espresso' or user_input == 'cappuccino':
        flavour(user_input)
        if is_done:
            coin_count(user_input)
            is_done=False
    elif user_input=='report':
        report()
    elif user_input=="off":
        print("Machine now turn offed........")
        machine_off=True
    else:
        print("Please enter valid keyword.")
        



