# Generates a random number between 1 and 100 then tells the user if they guessed above or below the number
# 03/17/2019
# CTI-110 P5HW1-Random Number
# Sean Mulvey
################################################################################################################
import random
print("*****This program lets you try to guess a random number between 1 and 100*****")
    # Tells user what the code does

print()

keep_going = input("Would you like to play? [Y/N]: ").upper()
        # Asks user if they would like to play

while keep_going == "Y":
        # Starts the game if the user answers "Y"

    def random_number():
            
        num = random.randint(1,100)
            # Generates a random number between 1 and 100


        return num
            # Tells the program that it will use num in another definition

    num = random_number()
            # Sets the num variable equal to the random number generated in random_number()
        

    def game():
        guess = int(input("Please guess a number between 1 and 100: "))
            # Asks user to make a guess

        total = 1
        

        print()

        while guess != num:
                # Loop to keep going if the guess is wrong
                
            if guess > num:
                print()
                print("Too high, try again!")
                    # Tells the user if their guess was higher than the random number

            else:
                print()
                print("Too low, try again!")
                    # Tells user if their guess was lower than the random number

            print()

            total = total + 1
                # Creates a running total to keep track of attempts

            guess = int(input("Please guess a number between 1 and 100: "))
                # Stops the loop from being infinite

        print()
        print("Congratulations. You guessed the correct number! It took you ",total," attempts!")
            # Tells the user they guessed the correct number and shows number of attempts

    

    game()
    keep_going = input("Would you like to play again? [Y/N]: ").upper()
        # Asks user if they want to play again

print()

print("OK")


