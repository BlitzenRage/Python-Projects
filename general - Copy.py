# Created By: [MY NAME WAS HERE]
# Date: 12/03/24
# version = '1.0'
#-------------------------------------------------------------------------------------------------------------
"""Details about the module and for what purpose it was built for."""
# This module provides information about a theme park, including rules, lost and found services, first aid stations, and park hours.
#-------------------------------------------------------------------------------------------------------------
# Built in Imports
from datetime import time, date, timedelta 
#-------------------------------------------------------------------------------------------------------------
# User made Imports

def park_information():
    # Function to display park information and handle user interactions
    while True:  # Infinite loop to keep the menu active until the user decides to exit
        print("Welcome to the Theme Park.")
        print('''RULES: 
            1 - No outside food is allowed into the park.
            2 - No skipping lines for anything.
            3 - All medicine must be declared before entering the park.
            4 - Do not enter restricted areas. These are clearly marked with a sign.
            5 - Do not disturb any animals in any rides.''')
        print('''EXTRA INFORMATION: 
            1 - Shows lost and found services information.
            2 - Shows first aid stations information.
            3 - Shows Park Hours.''')
        
        # Prompting user to select a page or go back to the main page
        user_selection_a = input("Please select a page. Enter 'back' to go back to the main page: ")

        try:
            # Check if the user input is a valid page number
            if int(user_selection_a) <= 4 and int(user_selection_a) >= 1:
                if int(user_selection_a) == 1:
                    # Display lost and found services information
                    print('''LOST AND FOUND SERVICES:
                          The Theme Park is equipped with Lost and Found Station.
                          If you have lost any items, you come to the Lost and Found Station to get it.
                          This station can be found at the main entrance, at the side.''')
                    t1 = time(hour=8, minute=0)  # Opening time
                    t2 = time(hour=20, minute=0)  # Closing time
                    print('The station is open from', t1, 'to', t2)
                    continue  # Continue to the next iteration of the loop
                if int(user_selection_a) == 2:
                    # Display first aid stations information
                    print('''FIRST AID STATIONS: 
        First Aid Stations are scattered across the whole park.
        These are clearly marked with a red cross with big letters say 'First Aid Stations.'
        When the box is opened, an alarm will ring to alert park and EMS personnel to the location.
        These are open 24/7.                  ''')                  
                    continue  # Continue to the next iteration of the loop
                if int(user_selection_a) == 3:
                    # Display park hours based on the current day
                    d = date.today().weekday()  # Get the current day of the week (0=Monday, 6=Sunday)
                    t1 = time(hour=8, minute=0)  # Opening time
                    t2 = time(hour=20, minute=0)  # Closing time
                    if d == 6 or d == 5:  # Check if today is Saturday (5) or Sunday (6)
                        print("THE PARK IS ONLY OPEN ON WEEKDAYS.")
                    else:
                        d = date.today()  # Get the current date
                        print(f'''PARK HOURS: 
                        The current date is {d} and the park will be open from {t1} to {t2}.''')
                else:
                    # Handle invalid input for page selection
                    print("Invalid input, please input a page number.")
                    continue  # Restarts loop.
        
        except ValueError:
            # Handle non-integer input
            if user_selection_a == 'back':
                print("Going back to the main page....")  # Tell the user they are going back
                break  # Exit the loop.
            else:
                print("Please input a number.")  # Prompt the user to input a valid number
                continue  # Restarts loop.
