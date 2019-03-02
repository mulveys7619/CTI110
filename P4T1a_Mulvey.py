# CTI-110
# Sean Mulvey
# P4T1a
# 03/1/2019
######################################

import turtle
    # Enables turtle

t = turtle.Turtle()
    # Lets us shorten the turtle command throughout the rest of the code

t.pensize(10)
    # Changes line width to 10

t.shape("turtle")
    # Changes the cursor shape into a turtle

t.pencolor("purple")
    # Changes the pen color to purple

for square in (1,2,3,4):
    t.forward(200)
    t.left(90)
        # Repeats the two commands above 4 times


for triangle in (1,2,3):
    t.forward(240)
    t.left(120)
        # Repeats the two commands above 3 times
