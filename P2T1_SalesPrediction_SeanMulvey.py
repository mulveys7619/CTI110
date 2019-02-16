# Estimates predicted profit from sales
#02/15/2019
#CTI-110 P2T1 - Sales Prediction
#Sean Mulvey
###########################################

total_sales = float (input("Please enter projected sales: "))
    # Asks user for total amount of sales

print()

profit = total_sales * 0.23
    # Calculates projected profit

print("The profit is $", format(profit,".2f"))
    # Displays predicted profit
