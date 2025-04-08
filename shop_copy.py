# Created By: Prathik Veeramachaneni
# Created Date: 12/03/2024
# version = '1.0'
#-------------------------------------------------------------------------------------------------------------
"""Allows user to buy items from the Theme Park shop, can be accessed from main menu."""
#-------------------------------------------------------------------------------------------------------------
#Built in Imports
#-------------------------------------------------------------------------------------------------------------
#User made Imports

def shop_menu():

    total_order_price = 0
    shirt_orders = []
    backpack_orders = []
    souvenir_orders = []

    while True:
        print("Welcome to the Shop Menu.")
        print("Here are the items offered: ")
        items = ['1. Shirts', '2. Backpacks', '3. Souvenirs']
        for item in items:
            print(item)

        user_input = input("Please input the item number that you wish to look into. Enter 'quit' to exit: ")

        try:
            if int(user_input) == 1:
                print("Shirt Options: ")
                shirts = [
                    {
                        "name": "Subway Rider T-Shirt",
                        "price": 6.99
                    },
                    {
                        "name": "Great Falls Survivor T-Shirt",
                        "price": 10.99
                    },
                    {
                        "name": "Safari Adventurer T-Shirt",
                        "price": 12.99
                    },
                    {
                        "name": "Carnival Enthusiast T-Shirt",
                        "price": 13.99
                    },
                ]
                for index, shirt in enumerate(shirts, start = 1):
                    print(f"{index} - {shirt["name"]}")
                user_input_a = input("Do you wish to order an item (Y/N)? ").upper()
                if user_input_a == 'Y':
                    while True:
                        user_input_b = input("Please input the number of the item that you wish to buy. Enter 'quit' to stop: ")
                        if user_input_b.isdigit():
                            if int(user_input_b) == 1:
                                print("Ordering 1 Subway Rider T-Shirt.")
                                total_order_price += shirts[0]["price"]
                                shirt_orders.append('Subway Rider T-Shirt')
                            elif int(user_input_b) == 2:
                                print("Ordering 1 Great Falls Survivor T-Shirt.")
                                total_order_price += shirts[1]["price"]
                                shirt_orders.append('Great Falls Survivor T-Shirt')
                            elif int(user_input_b) == 3:
                                print("Ordering 1 Safari Adventurer T-Shirt.")
                                total_order_price += shirts[2]["price"]
                                shirt_orders.append('Safari Adventurer T-Shirt')
                            elif int(user_input_b) == 4:
                                print("Ordering 1 Carnival Enthusiast T-Shirt.")
                                total_order_price += shirts[3]["price"]
                                shirt_orders.append('Carnival Enthusiast T-Shirt')
                            else:
                                print("Invalid Item Number, restart.")
                                continue
                        elif str(user_input_b) == 'quit':
                            print('Exiting this menu....')
                            total_order_price = 0
                            shirt_orders.clear()
                            break
                        else:
                            print("Invalid Item Number, restart.")
                            continue
                        
                        user_input_c = input("Do you wish to order another item(Y/N)? ").title()
                        if user_input_c == 'Y':
                            continue
                        elif user_input_c == 'N':
                            print("These are your current orders: ")
                            for shirt_order in shirt_orders:
                                print(f"- {shirt_order}")
                            user_input_d = input("Do you wish to proceed(Y/N)? If you type Y, you will have your payment confirmed. If you press N, you will be able to add more items, and will remove the item you have just ordered: ").upper()
                            if user_input_d == 'Y':
                                print("YOUR TOTAL ORDER PRICE IS:", total_order_price,'. THANK YOU FOR SHOPPING WITH US.')
                                total_order_price = 0
                                shirt_orders.clear()
                                break
                            elif user_input_d == 'N':
                                print("Going back to ordering system.")
                                del shirt_orders[-1]
                                total_order_price -= shirts[int(user_input_b) - 1]["price"]
                                continue
                            else:
                                print("Invalid input. Please restart.")
                                continue
                        else:
                            print("Invalid Response, restarting.")
                            continue
                elif user_input_a == 'N':
                    print("Going back to main shop menu...")
                    continue           
                else:
                    print("Invalid Response, restarting.")
                    continue       
            elif int(user_input) == 2:
                print("Backpack Options: ")
                backpacks = [
                    {
                        "name": "Safari Scout Backpack",
                        "price": 30.99
                    },
                    {
                        "name": "Divers Backpack",
                        "price": 20.99
                    },
                    {
                        "name": "River Sack",
                        "price": 12.99
                    }
                ]
                for index, backpack in enumerate(backpacks, start = 1):
                    print(f"{index} - {backpack["name"]}")
                user_input_a = input("Do you wish to order an item (Y/N)? ").upper()
                if user_input_a == 'Y':
                    while True:
                        user_input_b = input("Please input the number of the item that you wish to buy. Enter 'quit' to stop: ")
                        if user_input_b.isdigit():
                            if int(user_input_b) == 1:
                                print("Ordering 1 Safari Scout Backpack.")
                                total_order_price += backpacks[0]["price"]
                                backpack_orders.append('Safari Scout Backpack')
                            elif int(user_input_b) == 2:
                                print("Ordering 1 Divers Backpack.")
                                total_order_price += backpacks[1]["price"]
                                backpack_orders.append('Divers Backpack')
                            elif int(user_input_b) == 3:
                                print("Ordering 1 River Sack.")
                                total_order_price += backpacks[2]["price"]
                                backpack_orders.append('River Sack')
                            else:
                                print("Invalid Item Number, restart.")
                                continue
                        
                        else:
                                print("Invalid Item Number, restart.")
                                continue
                        user_input_c = input("Do you wish to order another item(Y/N)? ").title()
                        if user_input_c == 'Y':
                            continue
                        if user_input_c == 'N':
                            print("These are your current orders: ")
                            for backpack_order in backpack_orders:
                                print(f"- {backpack_order}")
                            user_input_d = input("Do you wish to proceed(Y/N)? If you type Y, you will have your payment confirmed. If you press N, you will be able to add more items, and will remove the item you have just ordered: ").upper()
                            if user_input_d == 'Y':
                                print("YOUR TOTAL ORDER PRICE IS:", total_order_price,'. THANK YOU FOR SHOPPING WITH US.')
                                total_order_price = 0
                                backpack_orders.clear()
                                break
                            if user_input_d == 'N':
                                print("Going back to ordering system.")
                                del backpack_orders[-1]
                                continue
                            else:
                                print("Invalid input. Please restart.")
                                continue
                        else:
                            print("Invalid Response, restarting.")
                            continue
                if user_input_a == 'N':
                    print("Going back to main shop menu...")
                    continue           
                else:
                    print("Invalid Response, restarting.")
                    continue     
            elif int(user_input) == 3:
                print("Souvenir Options: ")
                souvenirs = ('1 - Mini Aquarium - $5.99', '2 - \'I Survived The Great Falls\' Plaque - $10.99', '3 - Collectible River Boat - $12.99')
                for souvenir in souvenirs:
                    print(souvenir)
                user_input_a = input("Do you wish to order an item (Y/N)? ").upper()
                if user_input_a == 'Y':
                    while True:
                        user_input_b = input("Please input the number of the item that you wish to buy: ")
                        if user_input_b.isdigit():
                            if int(user_input_b) == 1:
                                print("Ordering 1 Mini Aquarium.")
                                total_order_price += 5.99
                                souvenir_orders.append('Mini Aquarium')
                            elif int(user_input_b) == 2:
                                print("Ordering 1 \'I Survived The Great Falls\' Plaque.")
                                total_order_price += 10.99
                                souvenir_orders.append('\'I Survived The Great Falls\' Plaque')
                            elif int(user_input_b) == 3:
                                print("Ordering 1 Collectible River Boat.")
                                total_order_price += 12.99
                                souvenir_orders.append('Collectible River Boat')
                            else:
                                print("Invalid Item Number, restart.")
                        else:
                                print("Invalid Item Number, restart.")
                        user_input_c = input("Do you wish to order another item(Y/N)? ").title()
                        if user_input_c == 'Y':
                            continue
                        if user_input_c == 'N':
                            print("These are your current orders: ")
                            for souvenir_order in souvenir_orders:
                                print(f"- {souvenir_order}")
                            user_input_d = input("Do you wish to proceed(Y/N)? If you type Y, you will have your payment confirmed. If you press N, you will be able to add more items, and will remove the item you have just ordered: ").upper()
                            if user_input_d == 'Y':
                                print("YOUR TOTAL ORDER PRICE IS:", total_order_price,'. THANK YOU FOR SHOPPING WITH US.')
                                total_order_price = 0
                                souvenir_orders.clear()
                                break
                            if user_input_d == 'N':
                                print("Going back to ordering system.")
                                del souvenir_orders[-1]
                                continue
                            else:
                                print("Invalid input. Please restart.")
                                continue
                        else:
                            print("Invalid Response, restarting.")
                            continue
                if user_input_a == 'N':
                    print("Going back to main shop menu...")
                    continue           
                else:
                    print("Invalid Response, restarting.")
                    continue     
            else:
                print("Invalid item number, please input a valid number.")
                continue
        except BaseException as b:
            print(b)
            if user_input.lower() == 'quit':
                print("Exiting Program.....")
                break

            else:
                print("Please input a valid item number.")
                continue
                    