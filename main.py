import turtle
from turtle import Turtle, Screen

jim = Turtle()
jim.color("green")
screen = Screen()


def move_forwards():
    jim.forward(10)


def move_backwards():
    jim.bk(10)


def move_right():
    jim.right(25)


def move_left():
    jim.left(25)


def clear_canvas():
    jim.clear()
    jim.penup()
    jim.home()
    jim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_canvas)
screen.exitonclick()

