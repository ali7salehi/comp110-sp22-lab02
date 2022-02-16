"""
Ali Salehi
Asalehi@sandiego.edu
02/15/2022

"""
# importing the turtle
import turtle

# Assigning name to the turtle
ali=turtle.Turtle()

# Pick your background color
turtle.Screen().bgcolor("black")

# Can change the shape of turtle to circle, arrow, square or triangle
ali.shape("turtle")

# Pick your pen color
ali.pencolor("green")

# Change pen size  using one of the provided methods. #ali.width()
ali.pensize(1)

ali.up()    #lifts pen 
ali.backward(130) # Turtles moves backwards. integer should be assigned.
ali.left(75)    # Changes the direction of the turtle
ali.down()     # Pen is down and starts recording the movements until whenever we want it to.
ali.forward(250)
ali.right(150)
ali.forward(250)
ali.penup()
ali.backward(75)
ali.left(75)
ali.pendown()
ali.backward(90)
ali.hideturtle()
ali.penup()
ali.forward(90)
ali.right(75)
ali.forward(75)
ali.showturtle()
ali.left(75)
ali.forward(40)
ali.left(90)
ali.pendown()
ali.forward(225)
ali.penup()
ali.backward(225)
ali.right(90)
ali.pendown()
ali.forward(60)
ali.penup()
ali.forward(35)
ali.pendown()
ali.left(90)
ali.forward(225)
ali.penup()

ali.left(90)
ali.backward(12)
ali.pendown()
ali.forward(24)
ali.penup()
ali.backward(12)
ali.right(90)
ali.backward(225)
ali.left(90)
ali.backward(12)
ali.pendown()
ali.forward(24)
ali.hideturtle()

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()
