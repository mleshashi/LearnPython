from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()

# for i in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)


# for i in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()


# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]


colormode(255)
my_turtle.pen(pensize=3)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(number_of_side, side_length):
    angle = 360 / number_of_side
    for i in range(number_of_side):
        my_turtle.forward(side_length)
        my_turtle.left(angle)


for number_of_side in range(3, 11):
    my_turtle.color(random_color())
    draw_shape(number_of_side, 100)
