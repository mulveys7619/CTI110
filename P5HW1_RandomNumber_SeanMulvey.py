# Generates a random number between 1 and 100 then tells the user if they guessed above or below the number
# 03/11/2019
# CTI-110 P5HW1-Random Number
# Sean Mulvey
################################################################################################################
import random
print("*****This program lets you try to guess a random number between 1 and 100*****")

print()

def random_number():
    num = random.randint(1,100)


    return num

num = random_number()

def game():
    guess = int(input("Please guess a number between 1 and 100: "))



    print()

    while guess != num:
        
        if guess > num:
            print()
            print("Too high, try again!")

        else:
            print()
            print("Too low, try again!")

        print()

        guess = int(input("Please guess a number between 1 and 100: "))

    print()
    print("Congratulations. You guessed the correct number!")

game()

def repeat():
    keep_going = input("Would you like to play again? [Y/N]: ").upper()

   while keep_going == "Y":
       num = random_number()
       game()
        





