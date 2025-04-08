# Created By: Prathik Veeramachaneni
# Created Date: 12/03/2024
# version = '1.0'
#-------------------------------------------------------------------------------------------------------------
"""Details about the module and for what purpose it was built for."""
#-------------------------------------------------------------------------------------------------------------
#Built in 
import datetime, time
#-------------------------------------------------------------------------------------------------------------
#User made Imports

def concessions_menu():

    total_order_price = 0.00

    while True:
        print("WELCOME TO THE CONCESSIONS MENU.")
        print("These are the concessions options: ")
        concessions = ['1 - Papas Pizzeria', '2 - Papas Freezaria', '3 - A Random French Place', '4 - Italy\'s Finest', '5 - Roblox Gas Station']
        for concession in concessions:
            print(concession)

        user_input = input("Please input a concession stand number. Enter 'quit' to stop: ").strip()

        try:
            if int(user_input) <= 5 and int(user_input) >= 1:
                if int(user_input) == 1:
                    print("Papas Pizzeria is located at the end of the Safari ride. It features some of the best pizzas known to man. Here is a list of its items: ")
                    pizzeria_items = ('1: Olive Pizza - $9.99', '2: Mega Chicken Pizza - $19.99', '3: Veggie Pizza - $5.99', '4: Signature Pepperoni Pizza - $20.99', '5: Super Spice Pizza - $1.99')
                    for pizzeria_item in pizzeria_items:
                        print(pizzeria_item)
                    user_input_a = input("Do you wish to order an item (Yes/No)? ").title()
                    if user_input_a == 'Yes':
                        while True:
                            user_input_b = input("Please input the number of the item that you wish to buy. Enter 'quit' to go back to the concessions menu: ")
                            try:
                                if int(user_input_b) == 1:
                                    print("The Olive Pizza is made up of Olives and Cheese, and is a perfect pizza for those olive lovers.")
                                    user_input_d = input("Do you want to order this (Y/N): ")
                                    if user_input_d.upper() == 'Y':
                                        print("Ordering 1 Olive Pizza.")
                                        total_order_price += 9.99
                                    elif user_input_d.upper() == 'N':
                                        print('Going back to menu.')
                                    else:
                                        print('Invalid Input.')
                                        continue
                                elif int(user_input_b) == 2:
                                    print('The Mega Chicken Pizza is a massive pizza filled with shredded chicken.')
                                    user_input_d = input("Do you want to order this(Y/N): ")
                                    if user_input_d.upper() == 'Y':
                                        print("Ordering 1 Mega Chicken Pizza.")
                                        total_order_price += 19.99
                                    elif user_input_d.upper() == 'N':
                                        print('Going back to menu.')
                                    else:
                                        print('Invalid Input')
                                        continue
                                elif int(user_input_b) == 3:
                                    print('The Mega Chicken Pizza is a medium pizza with all veggies known to Papa.')
                                    user_input_d = input("Do you want to order this(Y/N): ")
                                    if user_input_d.upper() == 'Y':
                                        print("Ordering 1 Veggie Pizza.")
                                        total_order_price += 5.99
                                    elif user_input_d.upper() == 'N':
                                        print('Going back to menu.')
                                    else:
                                        print('Invalid Input')
                                        continue
                                elif int(user_input_b) == 4:
                                    print('The Signature Pepperoni is the first ever pizza Papa ever made.')
                                    user_input_d = input("Do you want to order this(Y/N): ")
                                    if user_input_d.upper() == 'Y':
                                        print("Ordering 1 Signature Pepperoni Pizza.")
                                        total_order_price += 20.99
                                    elif user_input_d.upper() == 'N':
                                        print('Going back to menu.')
                                    else:
                                        print('Invalid Input')
                                        continue
                                elif int(user_input_b) == 5:
                                    print('The Super Spice Pizza is the spiciest pizza ever, and can be fatal if you can\'t handle it. Be careful.')
                                    user_input_d = input("Do you want to order this(Y/N): ")
                                    if user_input_d.upper() == 'Y':
                                        print("Ordering 1 Super Spice Pizza.")
                                        total_order_price += 1.99
                                    elif user_input_d.upper() == 'N':
                                        print('Going back to menu.')
                                    else:
                                        print('Invalid Input')
                                        continue
                            except ValueError:
                                if user_input_b.lower() == 'quit':
                                    print("Going back to concessions menu")
                                    break
                                else:
                                    print("Invalid input, restarting.")
                                    continue
                            user_input_c = input("Do you wish to order another item? ").title()
                            if user_input_c == 'Yes':
                                continue
                            elif user_input_c == 'No':
                                print("YOUR TOTAL ORDER PRICE IS:", total_order_price)
                                current = datetime.datetime.today()
                                t = datetime.timedelta(minutes = 10)
                                service = current + t
                                final_service = service.strftime("%I:%M %p")
                                print("Your order will be served at:", final_service)
                                total_order_price = 0
                                break
                            else:
                                print("Invalid input, restarting.")
                                continue
                    elif int(user_input) == 2:
                        print("Papas Freezaria is located right next to Papas Pizzaria since Papa said it must. Here is a list of its items: ")
                        freezaria_items = ('1: Simple Chocolate Ice Cream - $30.99', '2: Supreme Vanilla Ice Cream - $49.99', '3: Golden Ice Cream - $166.99', '4: Diamond Ice Cream - $200.99', '5: Meteor Ice Cream - $10000000.99')
                        for freezaria_item in freezaria_items:
                            print(freezaria_item)
                        user_input_a = input("Do you wish to order an item (Yes/No)? ").title()
                        try:
                            while True:
                                user_input_b = input("Please input the number of the item that you wish to buy: ")
                                if user_input_b.isdigit():
                                    if int(user_input_b) == 1:
                                        print("Ordering 1 Simple Chocolate Ice Cream.")
                                        total_order_price += 30.99
                                    elif int(user_input_b) == 2:
                                        print("Ordering 1 Supreme Vanilla Ice Cream.")
                                        total_order_price += 49.99
                                    elif int(user_input_b) == 3:
                                        print("Ordering 1 Golden Ice Cream.")
                                        total_order_price += 166.99
                                    elif int(user_input_b) == 4:
                                        print("Ordering 1 Diamond Ice Cream.")
                                        total_order_price += 200.99
                                    elif int(user_input_b) == 5:
                                        print("Ordering 1 Meteor Ice Cream.")
                                        total_order_price += 10000000.99
                                    else:
                                        print("Invalid Item Number, restart.")
                                user_input_c = input("Do you wish to order another item? ").title()
                                if user_input_c == 'Yes':
                                    continue
                                if user_input_c == 'No':
                                    print("YOUR TOTAL ORDER PRICE IS:", total_order_price)
                                    current = datetime.datetime.today()
                                    t = datetime.timedelta(minutes = 10)
                                    service = current + t
                                    final_service = time.strftime("%I:%M %p")
                                    print("Your order will be served at:", final_service)
                                    total_order_price = 0
                                    break
                        except ValueError:
                            print("Invalid Input, restart.")
                            continue
                    elif int(user_input) == 3:
                        print("A Random French Place is located right in front of the Great Fall. Here is a list of its items: ")
                        french_items = ('1: French Onion Soup - 10.99', '2: Chicken Confit - $49.99', '3: Bouillabaisse - $16.99', '4: Chocolate Mousse - $20.99', '5: Escargot - $10.99')
                        for french_item in french_items:
                            print(french_item)
                        user_input_a = input("Do you wish to order an item (Yes/No)? ").title()
                        if user_input_a == 'Yes':
                            while True:
                                user_input_b = input("Please input the number of the item that you wish to buy: ")
                                if user_input_b.isdigit():
                                    if int(user_input_b) == 1:
                                        print("Ordering 1 French Onion Soup.")
                                        total_order_price += 10.99
                                    elif int(user_input_b) == 2:
                                        print("Ordering 1 Chicken Confit.")
                                        total_order_price += 49.99
                                    elif int(user_input_b) == 3:
                                        print("Ordering 1 Bouillabaisse.")
                                        total_order_price += 16.99
                                    elif int(user_input_b) == 4:
                                        print("Ordering 1 Chocolate Mousse.")
                                        total_order_price += 20.99
                                    elif int(user_input_b) == 5:
                                        print("Ordering 1 Escargot.")
                                        total_order_price += 10.99
                                    else:
                                        print("Invalid Item Number, restart.")
                                user_input_c = input("Do you wish to order another item (Yes/No)? ").title()
                                if user_input_c == 'Yes':
                                    continue
                                if user_input_c == 'No':
                                    print("YOUR TOTAL ORDER PRICE IS:", total_order_price)
                                    current = datetime.datetime.today()
                                    t = datetime.timedelta(minutes = 10)
                                    service = current + t
                                    final_service = time.strftime("%I:%M %p")
                                    print("Your order will be served at:", final_service)
                                    total_order_price = 0
                                    break
                    if int(user_input) == 4:
                        print("Italys Finest is located on the Underwater Subway. Here is a list of its items: ")
                        italian_items = [
                            {
                                "name": "1. Polenta - 10.99"
                            },

                            {
                                "2.": "Ribollita - 49.99"
                            },

                            {
                                "3.": "Risotto alla Milanese - 16.99"
                            },

                            {
                                "4.": "Cotoletta all Milanese - 20.99"
                            },

                            {
                                "5.": "Risotto di Seppie all Veneziana - 10.99"
                            }
                        ]
                        for italian_item in italian_items:
                            print(italian_items)
                        user_input_a = input("Do you wish to order an item (Yes/No)? ").title()
                        if user_input_a == 'Yes':
                            while True:
                                user_input_b = input("Please input the number of the item that you wish to buy: ")
                                if user_input_b.isdigit():
                                    if int(user_input_b) == 1:
                                        print("Ordering 1 Polenta.")
                                        total_order_price += 10.99
                                    elif int(user_input_b) == 2:
                                        print("Ordering 1 Ribollita.")
                                        total_order_price += 49.99
                                    elif int(user_input_b) == 3:
                                        print("Ordering 1 Risotto alla Milanese.")
                                        total_order_price += 16.99
                                    elif int(user_input_b) == 4:
                                        print("Ordering 1 Cotoletta alla Milanese.")
                                        total_order_price += 20.99
                                    elif int(user_input_b) == 5:
                                        print("Ordering 1 Risotto di Seppie alla Veneziana.")
                                        total_order_price += 10.99
                                    else:
                                        print("Invalid Item Number, restart.")
                                user_input_c = input("Do you wish to order another item? ").title()
                                if user_input_c == 'Yes':
                                    continue
                                if user_input_c == 'No':
                                    print("YOUR TOTAL ORDER PRICE IS:", total_order_price)
                                    current = datetime.datetime.today()
                                    t = datetime.timedelta(minutes = 10)
                                    service = current + t
                                    final_service = time.strftime("%I:%M %p")
                                    print("Your order will be served at:", final_service)
                                    total_order_price = 0
                                    break
                    if int(user_input) == 5:
                        print("Roblox Gas Station is located at the main entrance. Here is a list of its items: ")
                        gas_station_items = ['1: Golden Bag of Chips - 10.99', '2: Golden Bag of Nerd Clusters - $49.99', '3: Golden Nerds - $16.99', '4: Golden Hot Dogs - $20.99', '5: Golden Taco - $10.99']
                        for gas_station_item in gas_station_items:
                            print(gas_station_item)
                        user_input_a = input("Do you wish to order an item (Yes/No)? ").title()
                        if user_input_a == 'Yes':
                            while True:
                                user_input_b = input("Please input the number of the item that you wish to buy: ")
                                if user_input_b.isdigit():
                                    if int(user_input_b) == 1:
                                        print("Ordering 1 Golden Bag of Chips.")
                                        total_order_price += 10.99
                                    elif int(user_input_b) == 2:
                                        print("Ordering 1 Golden Bag of Nerd Clusters.")
                                        total_order_price += 49.99
                                    elif int(user_input_b) == 3:
                                        print("Ordering 1 Golden Nerds.")
                                        total_order_price += 16.99
                                    elif int(user_input_b) == 4:
                                        print("Ordering 1 Golden Hot Dogs.")
                                        total_order_price += 20.99
                                    elif int(user_input_b) == 5:
                                        print("Ordering 1 Golden Taco.")
                                        total_order_price += 10.99
                                    else:
                                        print("Invalid Item Number, restart.")
                                user_input_c = input("Do you wish to order another item? ").title()
                                if user_input_c == 'Yes':
                                    continue
                                if user_input_c == 'No':
                                    print("YOUR TOTAL ORDER PRICE IS:", total_order_price)
                                    current = datetime.datetime.today()
                                    t = datetime.timedelta(minutes = 10)
                                    service = current + t
                                    final_service = time.strftime("%I:%M %p")
                                    print("Your order will be served at:", final_service)
                                    total_order_price = 0
                                    break
                    else:
                        if user_input_a.title() == 'No':
                            print("Going back to concessions menu.")
                            continue
                        else:
                            print("Invalid concession number, input a new number.")
                            continue
        except BaseException as b:
            print(b)
            if user_input.lower() == 'quit':
                print("Exiting Program....")
                break
            else:
                print("Please input a number.")
                continue

