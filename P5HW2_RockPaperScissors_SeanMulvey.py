# Creates a game of rock, paper, scissors
# 03/17/2019
# CTI-110 P5HW2-Rock, Paper, Scissors Game
# Sean Mulvey
#################################################################################################
import random
print("*****This program lets you play Rock, Paper, Scissors against the computer*****")

print()


keep_going = input("Would you like to play?[Y/N]: ").upper()


    

       
while keep_going == "Y":

    print()

    def random_number():

        comp_hand = random.randint(1,3)

        return comp_hand
                    
    comp_hand = random_number()

    print()

    def user_input():

        user_hand =input("Please choose Rock, Paper, or Scissors: ").upper()

        return user_hand

    user_hand = user_input()

    print()

    def action():

                    

        if comp_hand == 1:
            print("The Computer Chose ROCK")

        elif comp_hand == 2:
            print("The Computer Chose PAPER")

        else:
            print("The Computer Chose SCISSORS")

                    

    action()

    print()

    def result():
        

        if user_hand == "ROCK" and comp_hand == 2:
            print("PAPER covers ROCK. THE COMPUTER WINS!")
            
            

        elif user_hand == "ROCK" and comp_hand == 3:
            print("ROCK crushes SCISSORS. YOU WIN!")
            
            
                    
        elif user_hand == "PAPER" and comp_hand == 3:
            print("SCISSORS cuts PAPER. THE COMPUTER WINS!")
            
            

        elif user_hand == "PAPER" and comp_hand == 1:
            print("PAPER covers ROCK. YOU WIN!")
            
           

        elif user_hand == "SCISSORS" and comp_hand == 2:
            print("SCISSORS cuts PAPER. YOU WIN!")
            
            

        elif user_hand == "SCISSORS" and comp_hand == 1:
            print("ROCK crushes SCISSORS. THE COMPUTER WINS!")
            
            

        else:
            print()

            print("Its a draw. Please try again.")

            print()

            
            

    result()

    

else:
    print("OK")






            


    

        


        





    

