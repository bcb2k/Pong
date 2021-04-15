import turtle
import tkinter

#Screen setup
TK_SILENCE_DEPRECATION=1
wn = turtle.Screen()
wn.title("My first pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.setx(-350)
paddle_a.sety(0)
paddle_a.shapesize(5.0, 0.5, 1.0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.setx(350)
paddle_b.sety(0)
paddle_b.shapesize(5.0, 0.5, 1.0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

#Main game loop
while True:
    wn.update()
