# This code converts kilometers to miles
# 03/10/2019
# CTI-110 P5T1_KilometerConverter
# Sean Mulvey
##################################################
print("*****This code converts kilometers into miles*****")
    # Tells the user what the program does
def KiloMiles():
        # Sets up the below as a function
    print()

    kilo = float (input("Please enter the distance of kilometers: "))
        # Asks user to input a value for kilometers
    print()

    mile = kilo * .6214
        # Sets the equation to convert from kilometers to miles

    print(kilo," kilometers is equal to ", format(mile,".2f")," miles")
        # Displays the result

KiloMiles()
        # Calls the function KiloMiles
