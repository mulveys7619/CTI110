# CTI-110
# P3HW1 - Color Mixer
# Sean Mulvey
# 02/15/2019
###########################################
print("*****This program displays the resulting color of mixing two primary colors together.*****")
    # Tells the user what the code does\

print()

Color_1 = input ("Please enter one of the following colors to mix: \n Red \n Blue \n Yellow \n")
    # Asks user for the first color they would like to mix

print()

Color_2 = input ("Please enter the second color you would like to mix: \n Red \n Blue \n Yellow \n")
    # Asks user for the second color they would like to mix

print()

if (Color_1 == "Red") and (Color_2 == "Red"):
    print("Red")

elif (Color_1 == "Blue") and (Color_2 == "Blue"):
    print("Blue")

elif (Color_1 == "Yellow") and (Color_2 == "Yellow"):
    print("Yellow")

elif (Color_1 == "Red") and (Color_2 == "Blue") or (Color_1 == "Blue") and (Color_2 == "Red"):
    print("Purple")

elif (Color_1 == "Red") and (Color_2 == "Yellow") or (Color_1 == "Yellow") and (Color_2 == "Red"):
    print("Orange")

elif (Color_1 == "Blue") and (Color_2 == "Yellow") or (Color_1 == "Yellow") and (Color_2 == "Blue"):
    print("Green")

else:
    print("Please make sure you entered one of the above colors.")

    #Displays the different color combinations
