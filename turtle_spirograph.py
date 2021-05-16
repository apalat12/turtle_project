# draw a spirograph


import turtle as tim
from random import randint
import random
screen = tim.Screen()
tim.screensize(2000,2000,'white')
tim.speed("fastest")
tim.pensize(1)
def spirograph():
    tim.colormode(255)
    for i in range(90):
        tim.color(randint(0,255),randint(0,255),randint(0,255))
        tim.setheading(i*4)
        tim.circle(200)


spirograph()
screen.exitonclick()