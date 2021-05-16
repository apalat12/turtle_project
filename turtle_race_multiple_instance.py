from turtle import Turtle, Screen
from random import randint

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6= Turtle()
t6.penup()
t6.hideturtle()
t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')
t4.shape('turtle')
t5.shape('turtle')
t1.color('red')
t2.color('green')
t3.color('blue')
t4.color('purple')
t5.color('orange')

screen = Screen()
obj_lst = [t1, t2, t3, t4, t5]

def turtle_racing(lst):
    screen.setup(1000, 500)
    user_input = screen.textinput("Who will win the race? ", 'Enter a color(red/green/blue/purple/orange):')
    user_bet = user_input.lower()

    for i in range(len(lst)):
        lst[i].penup()
        lst[i].setpos(-250, (i * 50) - 50)
        lst[i].speed('slowest')

    while (1):
        for i in lst:
            i.fd(randint(1, 5))
            # print(user_bet,i.pos()[0],i.color()[0])
            if int(i.pos()[0]) >= 480:
                if i.color()[0] == user_bet:
                    t6.write("You win!", True, align="center",font=("Arial", 15, "normal"))
                    return "You win!"

                else:
                    t6.write("You lose!{} is the winner".format(i.color()[0]), True, align="center",font=("Arial", 15, "normal"))
                    return "You lose!{} is the winner".format(i.color()[0])


print(turtle_racing(obj_lst))

screen.exitonclick()
