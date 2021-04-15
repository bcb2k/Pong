import turtle
import tkinter

#Screen setup
TK_SILENCE_DEPRECATION=1
wn = turtle.Screen()
wn.title("My first pong")
wn.bgcolor("blue")
wn.setup(width = 800, height = 600)
wn.tracer(0)


#Main game loop
while True:
    wn.update()

#Paddle A
paddle_a = turtle.Turtle()


#Paddle B
paddle_a = turtle.Turtle()


#Ball
