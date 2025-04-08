# Created By: [MY NAME WAS HERE]
# Created Date: 12/03/24
# version = '2.0'
#-------------------------------------------------------------------------------------------------------------
"""This is a system is a module of main.py. It allows the user to select a ride to ride. """
#-------------------------------------------------------------------------------------------------------------
# Built in Imports
import time, datetime  # Importing time and datetime modules.
#-------------------------------------------------------------------------------------------------------------
# User made Imports
#-------------------------------------------------------------------------------------------------------------

def rides_selections():
    # List of rides with their names and descriptions
    rides = [
        {
            "name": "Scenic River Cruise",
            "description": (
                "The River Cruise. A one hour journey across the beautiful river. "
                "Filled with only the noises of nature, this ride is sure to calm you down, and become one with nature."
            )
        },
        {
            "name": "Carnival Carousel",
            "description": (
                "Step right up into the Carnival Carousel, an enchanting ride into a world filled with fantasy. "
                "When you get onto the carousel, you will be given a choice of 30 beautiful steeds, all ready for you to ride them in this Fantasy World."
            )
        },
        {
            "name": "Jungle Adventure Water Splash",
            "description": (
                "Step right into the coaster of the Jungle Adventure Water Splash. Once you buckle your seat belt, "
                "you can go into an adventure throughout the jungle."
            )
        },
        {
            "name": "Downhill Mountain Run",
            "description": (
                "Step into the Downhill Mountain. It has some of the steepest slopes in the world, perfect for a roller coaster."
            )
        },
        {
            "name": "The Regurgitator",
            "description": (
                "The Regurgitator is perhaps one of our most infamous rides. "
                "It is a roller coaster filled with sharp turns and twists, along with sickening drops."
            )
        },
        {
            "name": "The Reapers Swing",
            "description": (
                "Introducing, the Reapers Swing. The Reapers swing is a state of the art giant swing that can go a full 360 degrees through the air."
            )
        },
        {
            "name": "The Great Fall",
            "description": (
                "The Great Fall starts off with your coaster being raised up along a tower. "
                "Then, you will be launched into the ground."
            )
        },
        {
            "name": "The Underwater Subway",
            "description": (
                "We present you the 'Underwater Subway.' It is a high-speed bullet train that combines luxury with wonder."
            )
        },
        {
            "name": "The Spaceship",
            "description": (
                "The Spaceship simulates what it is like to be in a rocket and in space. "
                "You will be able to control your launch into space."
            )
        },
        {
            "name": "The Safari",
            "description": (
                "The Safari is a 3 hour ride through our very own Desert. It is home to some of the most exotic animals in the world."
            )
        }
    ]

    while True:  # Starts an infinite loop for ride selection
        print("Welcome to our Theme Park Ride Selection.")  # Welcomes user.
        print()
        print('These are the available rides: ')  # Starts showing available rides.
        for index, ride in enumerate(rides, start=1):  # Goes through ride dictionary.
            print(f"{index} - {ride['name']}")  # Print ride number and name

        ride_number = input("Please select the number of the ride (Type 'quit' to exit): ")  # Prompt for user input

        try:  # Try block to handle potential errors
            if int(ride_number) >= 1 and int(ride_number) <= 10:  # Check if input is a valid ride number
                # Ride Number 1 - Scenic River Cruise
                if int(ride_number) == 1:  # Check if the ride_number is 1
                    print("You have selected the Scenic River Cruise.") # Tells user what they  have selected.
                    print()

                    print(rides[0]['description'])  # Print the description of the selected ride
                    print()
                    current_time = datetime.datetime.today()  # Get the current date and time
                    current_hours = current_time.hour  # Extract the current hour
                    if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                        print("The current waiting time is 30 minutes.")  # Display waiting time
                    continue  # Restart the loop

                else:  # If the user didn't select the Scenic River Cruise, asks user to input age.
                    while True:
                        try:
                            age = int(input("Please input your age: "))  # Ask for user's age
                            if age <= 0 or age >= 122:  # Checks age input
                                print("Please input a valid age.")  # Has user input a valid age.
                                continue
                        except ValueError:
                            print("Please input a valid input.")  # If there is a ValueError, it does this.
                        else:
                            break  # Exit the loop if age is good.

                    # Ride Number 2 - Carnival Carousel
                    if int(ride_number) == 2:  # Check if the ride_number is 2
                        print("You have selected the Carnival Carousel.")  # Confirm selection
                        print()

                        if age >= 3:  # Check if user is old enough for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print()
                            print(rides[1]['description'])  # Print the description of the selected ride
                            current_time = datetime.datetime.today()  # Get the current date and time
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        else:  # If age is too low
                            print(f"Age Verification: {age} - Your age is too low, you cannot ride this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 3 - Jungle Adventure Water Splash
                    if int(ride_number) == 3:  # Check if the ride_number is 3
                        print("You have selected the Jungle Adventure Water Splash.")  # Confirm selection
                        print()

                        if age >= 6:  # Check if user is old enough for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print()
                            print(rides[2]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 6:  # If age is too low
                            print(f"Age Verification: {age} - Your age is too low, you cannot ride this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 4 - Downhill Mountain Run
                    if int(ride_number) == 4:  # Check if the ride_number is 4
                        print("You have selected the Downhill Mountain Run")  # Confirm selection
                        print()

                        if age >= 12:  # Check if user is old enough for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print()
                            print(rides[3]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 12:  # If age is too low
                            print(f"Age Verification: {age} - Your age is too low, you cannot ride this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 5 - The Regurgitator
                    if int(ride_number) == 5:  # Check if the ride_number is 5
                        print("You have selected The Regurgitator")  # Confirm selection
                        print()

                        if age >= 12 and age < 70:  # Check if user is within the age range for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print()
                            print(rides[4]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 12 or age >= 70:  # If age is too low or too high
                            print(f"Age Verification: {age} - Your age is too low or too high, you cannot ride this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 6 - The Reapers Swing
                    if int(ride_number) == 6:  # Check if the ride_number is 6
                        print("You have selected the Reapers Swing.")  # Confirm selection
                        print()

                        if age >= 14 and age < 65:  # Check if user is within the age range for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print(rides[5]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 14 or age >= 65:  # If age is too low or too high
                            print(f"Age Verification: {age} - You are not allowed onto this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 7 - The Great Fall
                    if int(ride_number) == 7:  # Check if the ride_number is 7
                        print("You have selected The Great Fall.")  # Confirm selection
                        print()

                        if age >= 13 and age < 65:  # Check if user is within the age range for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print(rides[6]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 13 or age > 65:  # If age is too low or too high
                            print(f"Age Verification: {age} - You are not allowed onto this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 8 - Underwater Subway
                    if int(ride_number) == 8:  # Check if the ride_number is 8
                        print("You have selected The Underwater Subway.")  # Confirm selection
                        print()

                        if age >= 5:  # Check if user is old enough for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print(rides[7]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 5:  # If age is too low
                            print(f"Age Verification: {age} - You are not allowed onto this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 9 - The Spaceship
                    if int(ride_number) == 9:  # Check if the ride_number is 9
                        print("You have selected The Spaceship.")  # Confirm selection
                        print()

                        if age >= 12 and age < 80:  # Check if user is within the age range for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print(rides[8]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 12 or age > 80:  # If age is too low or too high
                            print(f"Age Verification: {age} - You are not allowed onto this ride.")  # Inform user
                            continue  # Restart the loop

                    # Ride Number 10 - The Safari
                    if int(ride_number) == 10:  # Check if the ride_number is 10
                        print("You have selected The Safari.")  # Confirm selection
                        print()

                        if age >= 12 and age < 70:  # Check if user is within the age range for the ride
                            print(f"Age Verification: {age} - You are allowed onto this ride.")  # Confirms if rider can go ride.
                            print(rides[9]['description'])  # Print the description of the selected ride
                            current_hours = current_time.hour  # Extract the current hour
                            if current_hours == 10 or current_hours == 12 or current_hours == 15:  # Check for specific hours
                                print("The current waiting time is 30 minutes.")  # Display waiting time
                            continue  # Restart the loop
                        if age < 12 or age > 70:  # If age is too low or too high
                            print(f"Age Verification: {age} - You are not allowed onto this ride.")  # Inform user
                            continue  # Restart the loop
            else:  # If the input is not a valid ride number
                print("INPUT A VALID RIDE NUMBER.")  # Prompt for valid input
                continue  # Restart the loop

        except ValueError:  # Handle value errors from input
            if str(ride_number).lower() == 'quit':  # Check if the user wants to exit
                print("Exiting Program....")  # Confirm exit
                break  # Exit the loop
            else:
                print("PLEASE INPUT A NUMBER.")  # Prompt for valid number input
                continue  # Restart the loop
