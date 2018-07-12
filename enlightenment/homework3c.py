# draw a polygon from user choice
import turtle
import math
#return the degree turn when drawing next side
def getAngle(sides):
    return 360/sides
#return the small integer from windows height and window width
def mySize():
    if turtle.window_height()>turtle.window_width():
        return turtle.window_width()*0.9
    else :
        return turtle.window_height()*0.9
#return the length of side so each polygon has same size
def getSide(sides):
    return math.pi*mySize()/sides

number_of_sides = int(input("what shape do you want me to draw? "))

if number_of_sides > 100 :
    print("this number is too big")
elif number_of_sides < 3 :
    print("good gried, I can't draw shape with " + str(number_of_sides) + " sides")
else :
    turtle.Screen().bgpic('xlb.gif')
    turtle.color('red','yellow')
    turtle.penup()
    angle = getAngle(number_of_sides)
    side_length = getSide(number_of_sides)
    turtle.speed(9)
    turtle.setposition(0-side_length/2,0-turtle.window_height()*0.9/2)
    turtle.pendown()
    turtle.begin_fill()
    for x in range (number_of_sides):
        turtle.forward(side_length)
        turtle.left(angle)
    turtle.end_fill()
    turtle.hideturtle()
