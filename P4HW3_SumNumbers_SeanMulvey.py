# This program keeps a running total of positive numbers
# 03/5/2019
# CTI-110 P4HW3 - Sum of Numbers
# Sean Mulvey
####################################################
print("*****This program records positive numbers and adds them together*****")
    # Tells user what the program does

print()

end = -1
    # Sets end to -1

total = 0
    # Sets total to 0

num = int (input("Please enter a positive number. [To exit and see total enter -1]:"))
    # Asks user to enter a numer



while num > end:
        # Repeats loop as long as the input is greater than end

    total = total + num
        # Sets total as a running total
    num = int (input("Please enter a positive whole number. [To exit and see total enter -1]:"))
        # Statement that prevents loop from being infinite   


print("The total is ", total)
    # Displays the total

    
          
        
