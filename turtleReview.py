from turtle import *
import math

#setting up screen size
setup (700,500)


#Functions
def whileDrawShape (turtle,sides,color):
    turtle.pencolor (color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides :
        turtle.forward (50)
        turtle.right (angle)
        drawnSides+=1

def forDrawShape (turtle,sides,color) :
    turtle.pencolor (color)
    angle = 360/sides

    for s in range  (sides):
        turtle.forward (50)
        turtle.right (angle)

#Running Code
anah= Turtle () #creates turtle
anah.turtlesize (2,2)
anah.pensize (5)
anah.pendown

another = True

while another ==True:

    print ("How many sides do you want?")
    numSides = int(input ())
    print ("What color do you want?")
    chosenColor = input ()

    forDrawShape (anah,numSides, chosenColor)

    print("do you want to draw another shape?")
    answer = input ()

    if (answer == "no"):
        another = False
    if (answer == "yes"):
        anah.penup ()
        anah.right (150)
        anah.pendown ()
       
#whileDrawShape (anah,4,"blue")
#anah.penup ()
#anah.forward (100)
#anah.pendown ()
#forDrawShape (anah,5,"pink")
#whileDrawShape (diana,5,red)
#closes the turtle window on click
exitonclick ()

