# CTI-110
#P3T1- Area of Rectangles
#Sean Mulvey
#02/15/2019
#####################################################################
print("*****This program compares the area and length of 2 rectangles.*****")
    # Tells user what the program does

print()

WR1 = float (input("Please enter the WIDTH of Rectangle 1: "))
    # Asks user for the width of Rectangle 1

LR1 = float (input("Please enter the LENGTH of Rectangle 1: "))
    # Asks user for the length of Rectangle 1

print()

WR2 = float (input("Please enter the WIDTH of Rectngle 2: "))
    # Asks user for the width of Rectangle 2
    
LR2 = float (input("please enter the LENGTH of Rectangle 2: "))
    # Asks user for the length of Rectangle 2

print()

AR1 = WR1 * LR1
    # Calculates the area of rectangle 1

AR2 = WR2 * LR2
    # Calculates the area of Rectangle 2

if AR1 > AR2:
    print(" The area of Rectangle 1 is LARGER than the area of Rectangle 2.")

elif AR1 < AR2:
    print("The area of Rectangle 2 is LARGER than the area of Rectangle 1.")

else:
    print("The area of Rectangle 1 is EQUAL to the area of Rectangle 2.")

        # Compares the area of each rectangle to display an output
