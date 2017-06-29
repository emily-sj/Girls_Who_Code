from turtle import *
import math

#setting up screen size
setup (700,500)

#Functions
def whileDrawnSides (turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 60

#Running Program
em = Turtle ()
em.turtlesize (2,2)
em.pendown ()

print ("Which direction do you want to move?")

answer = input ()
if (answer=="right"):
    em.pendown ()
    em.pencolor ("red")
    em.right (150)
if (answer=="left") :
    em.pencolor ("blue")
    em.pendown ()
    em.left (150)
if (answer=="up"):
    em.pencolor ("pink")
    em.pendown ()
    em.up (150)
if (answer=="down"):
    em.pencolor ("black")
    em.pendown ()
    em.down (150)
        
    




#exit window screen
exitonclick ()
