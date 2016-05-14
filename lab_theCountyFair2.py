# Program CountyFair Part 2
# Description:
#      Simulates a trip to the County Fair
#      Part 1 steps:
#          buy tokens
#          ride the Ferris Wheel
# Author: Alexander Solinger
# Date: 15 April 2016
# Revised:
# 	16 April 2016
# 	24 April 2016

# Libraries used
import random
import os

# Global constants
CASH_OUTLAY = 100.00
TOKEN_COST = 0.25
FERRIS_COST = 3
NUM_HORSES = 6
FINISH_LINE = 100
TIME_DELAY = 100
BUY_TOKENS = 1
FERRIS_WHEEL = 2
HORSE_RACE = 3
LEAVE_FAIR = 4
DELAY = 100

# Main Program

def main():

    # Declare variables
    answer = ""

    print("\nCOUNTYFAIR™")
    answer = input("\nWould you like to start a new game? (y/n): ")

    # This makes it easy to keep playing the game
    #  any input except "no" goes back to the fair
    while not ((answer == 'n') or (answer == 'N')):

        goToTheFair(CASH_OUTLAY)

        answer = input("\nWould you like to start a new game? (y/n): ")

    # End While

    input("Press Enter to close the program.")

# End Program

#----------------------------------------------------------------------------------------

# Function goToTheFair
# Description:
#     The "main function" of the trip to the fair
#     buys tokens, calls the appropriate function for each ride
# Calls:
#     buyTokens
#     rideFerrisWheel
# Parameters:
#	    purse Decimal   # all the money you have to spend
# Returns:
#     none

def goToTheFair(purse):

    # Declare Local Variables
    total_tokens = 0
    tokens_purchased = 0
    money_spent = 0
    option = 0
    resources = [purse, total_tokens]

    # Display Opening Message , Purse and Token amoun and Menu
    print("\nHi there and welcome to the County Fair! ")
    input("Press 'Enter' to continue and choose from the menu below: ")


    while (option != 4):

        print("\n---------------")
        print("Tokens:", resources[1])
        print("Purse: $", format(resources[0], '.2f'), sep='')
        print("---------------")

        print("\n****COUNTY FAIR****")
        print("-------------------")
        print("1. $ BUY TOKENS $ ")
        print("2. Ride the Ferris Wheel ")
        print("3. Watch the Horse Race ")
        print("4. Leave the Fair ")

        option = int(input("\nWhat would you like to do? (Enter 1,2,3, or 4): "))

        # Call function and calculate tokens and purse
        # based on user's decision

        if (option == BUY_TOKENS):

            resources = buyTokens(resources)
            # print(resources) # debugging

        elif (option == FERRIS_WHEEL) and (resources[1] >= 6):

            resources = rideFerrisWheel(resources)

            # Calculate tokens left after riding ferris wheel
            # total_tokens = total_tokens - tokens_used

        elif (option == FERRIS_WHEEL) and (resources[1] < 6):

            print("\nSorry. You currenlty have", resources[1], "tokens.")
            print("You need at least 6 tokens for you and" + \
                  "your 'sweetie' to ride the ferris wheel.")
            input("Press 'Enter' to continue. ")

        elif (option == HORSE_RACE):

            print("Good idea! Let's go watch the horse race!!!")
            horseRace()

        else:

            print("See you next time!")

        # End if

    # End while

# End Function

#------------------------------------------------------------------------------------------------------------

# Function buyTokens
# Description:
#     This function lets the user "buy" tokens and gives a value
#     for the amount of tokens the user has
# Calls:
#     none
# Parameters:
#     resources   # all the money you have to spend in tokens and total tokens
# Returns:
#     resources

def buyTokens(resources):

    # Declare Local Variables
    tokens_bought = 0
    money_spent = 0

    print("\nTokens cost $0.25 each." +
          "You currently have $", format(resources[0], '.2f'), sep='')

    # Sell tokens to user and calculate money spent
    tokens_bought = int(input("How many tokens would you like to buy? "))

    money_spent = (tokens_bought * TOKEN_COST)

    # Make sure user has enough money to buy tokens
    if ((resources[0] - money_spent) < 0):

        print("\nSorry, you do not have enough money to buy that many tokens.")
        input("Press 'Enter' to continue. ")

        tokens_bought = 0

    elif (resources[0] - money_spent) >= 0:

        resources[0] = resources[0] - money_spent

        resources[1] = resources[1] + tokens_bought

        print("\n-$", format(money_spent, '.2f'), sep="")
        print("\nThank you. You bought", tokens_bought, "tokens")
        print("You now have $", format(resources[0], '.2f'), " left to spend.", sep='')
        input("\nPress 'Enter' to continue. ")

    # End if

    # Return Values
    return resources

# End Function

#-------------------------------------------------------------------------------------------------------------

# Function rideFerrisWheel
# Description:
#     This function lets the user ride the ferris wheel with
#     their 'sweetie' with the tokens they have bought
# Calls:
#     none
# Parameters:
#     tokens  # all the tokens the user has
# Returns:
#     tokens_used

def rideFerrisWheel(resources):

    # Declare Local Variables
    tokens_used = 0
    waiting = 'y'
    position = 0

    # Display Welcome Message
    input("\nWelcome to the Ferris Wheel!!! Press 'Enter' to get in line.")

    # Determine when the user gets to ride the ferris wheel
    while (waiting == 'y') and (position != 6):

        position = random.randrange(1, 13, 1)

        if (position == 6):

            waiting = 'n'

            print("\nGreat! It's time for you and your 'sweetie' to get on. Have fun!")

            # Recalculate the total amount of tokens after
            # tokens are paid for ferris wheel
            # The cost for the user and their 'sweetie' to ride
            tokens_used = (FERRIS_COST * 2) 
            resources[1] = resources[1] - tokens_used
            
            print("\nYou paid ", tokens_used, "tokens to the ride attendant.")
            input("\nPress 'Enter' to get on the Ferris Wheel: ")

        else:

            waiting = 'y'

            print("\n*sigh* STILL WAITING")

            tokens_used = 0
            
        # End if

    # End While

    # Dertimine if the user gets a kiss from their 'sweetie'
    # and when they get off the ride
    while (waiting == 'n'):

        position = random.randrange(1,13,1)

        if (position == 11) or (position == 12) or (position == 1):

            print("\nYou and your 'sweetie' are at the top of the Ferris Wheel!")
            kiss = input("Would you like to give your 'sweetie' a kiss? (y/n) ")

            if (kiss == 'y'):

                # Generate random response to kiss
                kiss_response = random.randrange(1,5,1)

                if (kiss_response == 1):
                    
                    print("\n*MUAH* !!!HOT STUFF!!!")

                elif (kiss_response == 2):

                    print("\n*SMOOCH* !!!HOW ROMANTIC!!!")

                elif (kiss_response == 3):

                    print("\nSweetie: 'WOWZERS! You're a GREAT KISSER!' ")

                else:

                    print("\nSweetie: 'Don\'t push your luck!'")

                # End if

            else:

                print("\nIt sure is quiet up here. Great view, though")

            # End if
                
        elif (position == 6):

            print("\nThe ride is over and it's your" +
                  " turn to get off. Come back anytime!")

            waiting = 'y'

        else:

            print("\nWhat a great view!")

        # End if

    # End while
    
    # Return Values
    return resources

# End Function

#-----------------------------------------------------------------------------------------------------

# Function: horseRace
# Descritpion:
#     This function simulates a horse race
#     for viewing pleasure.
# Calls:
#     None
# Parameters:
#     None
# Return:
#     None

def horseRace():

    # Declare variables
    count = 0
    spaces = 0
    wait = 0
    tickTock = 0
    horses = [0] * NUM_HORSES
    winner = False

    while (winner != True):

        # some form of this will clear the screen
        #os.system('cls' if os.name == 'nt' else 'clear')
        #os.system('cls')
        os.system('clear')
        #print('\|', end = '')

        # Display the horse race           
        print(' ', end = '')
        print()
        print("Horse Number: ")
        print("[#1, #2, #3, #4, #5, #6]")
        print("------------------------")
        print(horses)

        num = random.randint(0,5)

        horses[num] += 1

        # Determine the winner
        if (horses[num] == FINISH_LINE):

            horses[num] = "WINNER"

            print()
            print("Horse Number: ")
            print("[#1, #2, #3, #4, #5, #6]")
            print("------------------------------")
            print(horses)

            winner = True

        # End If

    # End While

        # print('@')
        
        for wait in range(DELAY):
            tickTock = tickTock
        #End For

    print("\nWe have a winner!!!")
    input("Press Enter to continue")

#End Function
    
main()

        

        
      

    
