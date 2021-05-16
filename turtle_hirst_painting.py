import turtle as tim
from random import randint
import random
import colorgram

# colors = colorgram.extract('image.jpg', 20)
#
#
# def color_list(colors):
#     return [(colors[i].rgb[0],colors[i].rgb[1],colors[i].rgb[2]) for i in range(len(colors))]
extracted_colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205),
                    (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157),
                    (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
                    (35, 61, 55), (156, 33, 31), (17, 97, 71)]

screen = tim.Screen()
tim.screensize(2000, 2000, 'white')
tim.speed("fastest")
tim.colormode(255)
tim.hideturtle()
def hirst_painting(size,space_dots):
    for row in range(0,size*space_dots,space_dots):
        tim.penup()
        tim.setpos(-size*space_dots/2,-(size*space_dots/2)+row)
        for col in range(size):
            tim.pendown()
            tim.dot(5, random.choice(extracted_colors))
            tim.penup()
            tim.fd(space_dots)

hirst_painting(50,10)

screen.exitonclick()
