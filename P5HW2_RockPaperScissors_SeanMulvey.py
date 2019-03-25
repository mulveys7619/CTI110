# Creates a game of rock, paper, scissors
# 03/25/2019
# CTI-110 P5HW2-Rock, Paper, Scissors Game
# Sean Mulvey
#################################################################################################
import random

print("*****This program lets you play Rock, Paper, Scissors against the computer*****")
        # Tells user what the program does

print()

loss_total = 0
win_total = 0
draw_total = 0


def random_number():
            # This definition creates a random number

    comp_hand = random.randint(1,3)
            # Sets comp_hand equal to a random number between 1 and 3

    return comp_hand
            # Tells the program I am going to use comp_hand in another definition
    
def user_input():
            # This definiton receives the choice the user makes
        

    user_hand =input("Please choose Rock, Paper, or Scissors: ").upper()
            # Asks user to choose ROCK, PAPER, or SCISSORS

    return user_hand
            # Tells the program I'm going to use user_hand in another definition

def action():
                # This definiton displays what the computer chose

                    

    if comp_hand == 1:
        print("The Computer Chose ROCK")
                # If the randint was 1 it displays ROCK

    elif comp_hand == 2:
        print("The Computer Chose PAPER")
                # If the randint was 2 it displays PAPER

    else:
        print("The Computer Chose SCISSORS")
                # If the randint was not 1 or 2 it displays SCISSORS


def result():
                # This definition displays the result of what the user and computer chose
        

        if user_hand == "ROCK" and comp_hand == 2:
            print("PAPER covers ROCK. THE COMPUTER WINS!")
                # Displays result if user chose ROCK and computer chose PAPER
            loss_total += 1
            
            

        elif user_hand == "ROCK" and comp_hand == 3:
            print("ROCK crushes SCISSORS. YOU WIN!")
                # Displays result if user chose ROCK and computer chose SCISSORS
            win_total += 1
            
                    
        elif user_hand == "PAPER" and comp_hand == 3:
            print("SCISSORS cuts PAPER. THE COMPUTER WINS!")
                # Displays result if user chose PAPER and computer chose SCISSORS
            loss_total += 1
            

        elif user_hand == "PAPER" and comp_hand == 1:
            print("PAPER covers ROCK. YOU WIN!")
                # Displays result if user chose PAPER and computer chose ROCK
            win_total += 1
           

        elif user_hand == "SCISSORS" and comp_hand == 2:
            print("SCISSORS cuts PAPER. YOU WIN!")
                # Displays result if user chose SCISSORS and computer chose PAPER
            win_total += 1
            
            

        elif user_hand == "SCISSORS" and comp_hand == 1:
            print("ROCK crushes SCISSORS. THE COMPUTER WINS!")
            # Displays result if user chose SCISSORS and computer chose ROCK
            loss_total += 1
            

        else:
            print()

            print("Its a draw. Please try again.")
                # Displays a draw if the user and computer have the same result

            draw_total += 1

            print()

        return draw_total, win_total, loss_total

        

    

keep_going = input("Wins   Losses   Draws \n ------------------------- \n", win_total,"   ", loss_total,"   ",draw_total,"Would you like to play?[Y/N]: ").upper()
        # Asks user if they want to play
        
while keep_going == "Y":
        # Starts loop if users inputs "Y"

    print()

                        
    comp_hand = random_number()
                # Sets comp_hand equal to the definition random_number

    print()



    user_hand = user_input()
                # Sets user_hand equal to the definition user_input

    print()



                        

    action()
                    # Ends the definition

    print()



            
            

draw_total, win_total, loss_total= result()# Ends the result definition

    
print("OK")
        # Displays if the user says they don't want to play

def total():

    print("Okay")

total()


