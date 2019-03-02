# This program adds up number of bugs collected each day
# 03/2/2019
# CTI-110
# Sean Mulvey
############################
print("*****This program adds up how many bugs you collected this week.*****")
    # Tells user what the program does
    
total_bugs = 0
    # Sets total bugs to 0 

for day in range(1,6):
    print("How many bugs did you collect on day ",day,"?:")
        # Runs the above code 5 times to gather number of bugs each day
    bugs = int(input())
    total_bugs = total_bugs + bugs
        # Sets total bugs variable to a running total of all 5 entries
    
print("You have collected " ,total_bugs, " bugs this week.") 
    # Displays total number of bugs over 5 days to the user
