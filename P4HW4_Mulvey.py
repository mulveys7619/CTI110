# Creates a snowflake
# 03/05/2019
# CTI - 110 P4HW4 Nested Loops
# Sean Mulvey
###########################################
import turtle
    # Enables turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(10)
t.shape("turtle")
t.pencolor("orange")
    # Sets the formatting of the sketch


for diag in range(0,2):
                # Creates 'X' formation
    for base in range(0,4):
                # Creates '+' formation
        for flake in range(0,1):
                # Creates flakes at the tips
            t.forward(100)
            t.right(45)
            t.forward(50)
            t.backward(50)
            t.left(90)
            t.forward(50)
            t.backward(50)
            t.right(45)
            t.forward(75)
            t.backward(50)
            t.right(45)
            t.forward(50)
            t.backward(50)
            t.left(90)
            t.forward(50)
            t.backward(50)
            t.left(135)
            t.forward(125)

        t.right(90)

    t.right(45)
    
