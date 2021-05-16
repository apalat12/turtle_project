# from turtle import Turtle, Screen
import turtle as tim
from random import randint
import random
# tim = Turtle()
screen = tim.Screen()

# screen.setup(5000,500,)
#
# tim.shape("turtle")
# tim.color('black')
# tim.penup()
# tim.setx(-1500)
# for _ in range(25):
#     for _ in range(5):
#         tim.pendown()
#         tim.forward(5)
#         tim.penup()
#         tim.forward(5)
#     tim.penup()
#     tim.forward(20)
tim.shape('classic')

def shapes(n):
    tim.colormode(255)
    tim.penup()
    # tim.setx(-100)
    tim.sety(500)
    tim.pendown()

    for i in range(n):
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        for _ in range(3 + i):
            tim.forward(100)
            tim.right(360 / (3 + i))


# shapes(10)
import time

def random_walk():
    tim.colormode(255)
    tim.pensize(7)
    directions = [0,90,180,270]
    # tim.speed("fastest")
    win_width, win_height, bg_color = 2000, 2000, 'white'
    tim.setup()
    tim.screensize(win_width, win_height, bg_color)

    while True:
        i= randint(2,1000)
        tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
        tim.forward(randint(10, 50))
        tim.setheading(random.choice(directions))
random_walk()

screen.exitonclick()
