import turtle
import math

tu = turtle.Turtle()
tu.speed(10)
x = 10
tu.forward(x)

for i in range(2, 10**10):
    side = x*(math.sqrt(i))
    cos_value = x/side
    angle = 180 - math.degrees(math.acos(cos_value))

    if i == 2:
        tu.left(90)
        tu.forward(x)
        tu.left(angle)
        tu.forward(side)
        tu.backward(side)
    else:
        tu.right(90)
        tu.forward(x)
        tu.left(angle)
        tu.forward(side)
        tu.backward(side)

turtle.done()