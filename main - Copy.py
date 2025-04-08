# Created By: [MY NAME WAS HERE]
# Created Date: 12/03/24
# version = '1.0'
#-------------------------------------------------------------------------------------------------------------
"""Details about the module and for what purpose it was built for."""
#-------------------------------------------------------------------------------------------------------------
#Built in Imports
#-------------------------------------------------------------------------------------------------------------
#User made Imports
import rides, general, concessions, shop
#-------------------------------------------------------------------------------------------------------------

# Creates a while loop.
while True:
    # Creates a password input.
    password = input("Please input the password to access this program: ").lower()
    # If the password is right, it will break and move on to the next loop.
    if password == '1234':
        break
    # Forces user to try again if they get it wrong.
    else:
        print("WRONG PASSWORD, TRY AGAIN")
        continue


# Creates a while loop.
while True:
    print("Welcome to the Main Theme Park Interface.")
    print('''Here is a list of our current pages:
          1. Rides Selection - Allows you to select a theme park ride.
          2. General Page - Shows information about the park.
          3. Concessions - Allows you to find locations of food stalls
          4. Shop - Allows you to buy items from our shop.''')
    # Has user input a page number. They can input quit if they want to stop.
    user_selection = input("Please select a page. Enter 'quit' to end: ")
    
    # Checks if the input is a digit.
    if user_selection.isdigit():
        # Checks if the input is between 1 and 4.
        if int(user_selection) <= 4 and int(user_selection) >= 1:
            # If the user_selection is 1, it calls the rides_selections() function.
            if int(user_selection) == 1:
                rides.rides_selections()
                continue
            # If the user_selection is 2, it calls the park_information() function.
            if int(user_selection) == 2:
                general.park_information()
                continue
            # If the user_selection is 3, it calls the concessions_menu() function.
            if int(user_selection) == 3:
                concessions.concessions_menu()
                continue
            # If the user_selection is 4, it calls the shop_menu() function.
            if int(user_selection) == 4:
                shop.shop_menu()
                continue
        # If the input is not between 1 and 4, it will have the user put in a actual page number.
        else:
            print("Invalid input, please input a page number.")
            continue
    # If the user enters quit, the program stops.
    elif user_selection == 'quit':
        print("EXITING PROGRAM")
        break
    # If none of the other conditions are fulfilled, then it ask the user to input a number, and then continues.    
    else:
        print("Please input a number.")
        continue

# Last line of code
if __name__ == "__main__":
    pass # enter the function name for the code on this page
