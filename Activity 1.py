import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num = 6
side = 70
angle = 360.0 / num

for i in range(num):
    polygon.forward(side)
    polygon.right(angle)

turtle.done()