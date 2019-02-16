# This code is a suggested tip percentage calculator
# 02/11/2019
#CTI-110 P2HW2-Meal Tip Calculator
#Sean Mulvey
#############################################

print("This is a tip percentage calculator.")
    # Tells user what the code does

print()

Bill = float (input ("What was the total cost of your bill?: "))
    # Asks user to enter amount of bill

print()

print ("Suggested tips: \n 15%:",format (Bill*.15,'.2f'),"\n 18%:",format (Bill*.18,'.2f'),"\n 20%",format (Bill*.2,'.2f'))
    # Calcualtes and displays recommended tips based on bill total
