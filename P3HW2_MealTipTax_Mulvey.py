# CTI-110
# P3HW2-MealTipTax
# Sean Mulvey
# 02/19/2019
#############################################

print("*****This program calculates tax and tip percentage of a bill*****")
    # Tells user what the program does

print()

bill = float (input("Please enter the price on the bill: "))
    # Asks user to key in bill

print()

tax = int (input ("Please enther which tip from the recommended percentages below that you would like to give: \n 1. 15% \n 2. 18% \n 3. 20% \n"))
    # Asks user which tip percentage they would like to use

print()

if tax == "1" or "15%":
    print("______________________________ \n Subtotal:      $", format (bill, ".2f") ," \n Tax:           $ ", format (bill * .07, ".2f"),"\n Tip:           $ ",format (bill * .15,".2f"),"\n Total:         $", format ((bill * .07) + (bill * .15) + bill, ".2f"),"\n ______________________________")

elif tax == "2" or "18%":
    print("______________________________ \n Subtotal:      $", format (bill, ".2f") ," \n Tax:           $ ", format (bill * .07, ".2f"),"\n Tip:           $ ",format (bill * .18,".2f"),"\n Total:         $", format ((bill * .07) + (bill * .18) + bill, ".2f"),"\n ______________________________")

elif tax == "3" or "20":
    print("______________________________ \n Subtotal:      $", format (bill, ".2f") ," \n Tax:           $ ", format (bill * .07, ".2f"),"\n Tip:           $ ",format (bill * .2,".2f"),"\n Total:         $", format ((bill * .07) + (bill * .2) + bill, ".2f"),"\n ______________________________")

else:
    print("Please enter one of the choices above")

    # Displays the Subtotal, Tax, Tip, and Total to the user
