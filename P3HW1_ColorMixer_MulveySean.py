# CTI-110
# P3HW1 - Color Mixer
# Sean Mulvey
# 02/18/2019
###########################################
print("*****This program displays the resulting color of mixing two primary colors together.*****")
    # Tells the user what the code does

print()

Color_1 = input ("Please enter one of the following colors to mix: \n Red \n Blue \n Yellow \n").upper()
    # Asks user for the first color they would like to mix

print()

Color_2 = input ("Please enter the second color you would like to mix: \n Red \n Blue \n Yellow \n").upper()
    # Asks user for the second color they would like to mix

print()

if (Color_1 == "RED") and (Color_2 == "RED"):
    print("RED")

elif (Color_1 == "BLUE") and (Color_2 == "BLUE"):
    print("BLUE")

elif (Color_1 == "YELLOW") and (Color_2 == "YELLOW"):
    print("YELLOW")

elif (Color_1 == "RED") and (Color_2 == "BLUE") or (Color_1 == "BLUE") and (Color_2 == "RED"):
    print("Purple")

elif (Color_1 == "RED") and (Color_2 == "YELLOW") or (Color_1 == "YELLOW") and (Color_2 == "RED"):
    print("Orange")

elif (Color_1 == "BLUE") and (Color_2 == "YELLOW") or (Color_1 == "YELLOW") and (Color_2 == "BLUE"):
    print("Green")

else:
    print("Please make sure you entered one of the above colors.")

    # Displays the different color combinations
