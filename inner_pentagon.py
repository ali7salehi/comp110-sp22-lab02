"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor("red")

# draw the pentagon
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)
sat.forward(50)
sat.left(72)

# create a turtle and set the pen color "Green"

sat.pencolor("green")
sat.penup()

#sat.setheading()
sat.goto(10)
sat.setheading(15)
sat.pendown()
sat.setheading(0)


# draw the pentegan.

sat.forward(40)
sat.left(72)
sat.forward(40)
sat.left(72)
sat.forward(40)
sat.left(72)
sat.forward(40)
sat.left(72)
sat.forward(40)
sat.left(72)

turtle_window = turtle.Screen()
turtle_window.exitonclick()
