# draw a polygon from user choice
import turtle
import math
#return the degree turn when drawing next side
def getAngle(sides):
    return 360/sides

number_of_sides = int(input("what shape do you want me to draw? "))
angle = getAngle(number_of_sides)

if number_of_sides > 100 :
    print("this number is too big")
else :
    print(number_of_sides)
    for x in range (1,number_of_sides+1):
        turtle.forward(45)
        turtle.left(angle)
    turtle.hideturtle()
