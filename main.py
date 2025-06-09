import turtle
from turtle import Turtle, Screen
import random

# we have alot of codes that generate alot of different outputs when commented out 

johnny = Turtle()
turtle.colormode(255)

johnny.shape("triangle")
johnny.color("red")

# for n in range(4):
#     johnny.forward(100)
#     johnny.right(90)

# for n in range(15):
#     johnny.forward(10)
#     johnny.penup()
#     johnny.forward(10)
#     johnny.pendown()

# colors = ["green", "yellow", "blue", "pink", "salmon", "bisque", "purple"]

#
# def draw_angle(shape_size):
#     angle = 360 / shape_size
#     for n in range(shape_size):
#         johnny.forward(100)
#         johnny.right(angle)
#
#
# for num_of_sides in range(3, 30):
#     johnny.color(random.choice(colors))
#     draw_angle(num_of_sides)

# for n in range(5):
#     johnny.color("yellow")
#     johnny.forward(100)
#     johnny.right(72)
#
# for n in range(6):
#     johnny.color("blue")
#     johnny.forward(100)
#     johnny.right(60)
#
# for n in range(7):
#     johnny.color("pink")
#     johnny.forward(100)
#     johnny.right(51.4)
#
# for n in range(8):
#     johnny.color("salmon")
#     johnny.forward(100)
#     johnny.right(45)
#
# for n in range(9):
#     johnny.color("bisque")
#     johnny.forward(100)
#     johnny.right(40)
#
# for n in range(10):
#     johnny.color("purple")
#     johnny.forward(100)
#     johnny.right(36)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_colors = (r, g, b)
    return my_colors


# johnny.speed(0)
# move = [0, 90, 180, 270]
#
#
# for moves in range(200):
#     johnny.pensize(15)
#     johnny.forward(50)
#     johnny.setheading(random.choice(move))
#     johnny.color(random_colors())

def draw_spirograph(graph_size):
    for n in range(int(360 / graph_size)):
        johnny.speed(0)
        johnny.circle(100)
        johnny.setheading(johnny.heading() + graph_size)
        johnny.color(random_colors())


draw_spirograph(5)


screen = Screen()
screen.exitonclick()