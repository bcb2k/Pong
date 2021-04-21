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
ball.dx = 0.3
ball.dy = 0.3

#paddle a movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#paddle b movement
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard bind
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")

wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")

#player points system
player1_points = 0
player2_points = 0

#Main game loop
while True:
    wn.update()

    #ball update
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        player2_points += 1
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        player1_points += 1
        ball.goto(0, 0)
        ball.dx *= -1

    #paddle collisions
    if ball.xcor() <= -340:
        if (paddle_a.ycor() - 50) < ball.ycor() < (paddle_a.ycor() + 50):
            ball.dx *= -1

    if ball.xcor() >= 340:
        if (paddle_b.ycor() - 50) < ball.ycor() < (paddle_b.ycor() + 50):
            ball.dx *= -1

