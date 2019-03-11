# This program usess a unction to convert feet to inches
# 03/11/2019
# CTI-110 P5T2_FeetToInches
# Sean Mulvey
############################################################
print("*****This program converts feet to inches*****")
    # Tells the user what the program does

print()

def feet_to_inches():
        # Sets up the below as a function

    feet = float(input("Please enter the distance in feet: "))
        # Asks user to input the distance in feet

    print()

    inch = feet * 12
        # Defines the equation to convert feet to inches

    print(feet, " feet is equal to ", format(inch,".2f")," inches")
        # Displays the result

feet_to_inches()
    # Calls the above function to be executed
