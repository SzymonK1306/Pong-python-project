import turtle
import constatnt

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=constatnt.SCREEN_WIDTH, height=constatnt.SCREEN_HEIGHT)
window.tracer(0)

# Paddle left

paddle_l = turtle.Turtle()
paddle_l.speed(0)  # speed of animation
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=constatnt.PADDLE_HEIGHT, stretch_len=constatnt.PADDLE_WIDTH)  # size of the paddle 1*20
paddle_l.penup()
paddle_l.goto(-constatnt.SCREEN_WIDTH/2 + 50, 0)  # start location

# Paddle right
paddle_r = turtle.Turtle()
paddle_r.speed(0)  # speed of animation
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=constatnt.PADDLE_HEIGHT, stretch_len=constatnt.PADDLE_WIDTH)  # size of the paddle 1*20
paddle_r.penup()
paddle_r.goto(constatnt.SCREEN_WIDTH/2 - 50, 0)  # start location
# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # start location
ball.dx = 0.1
ball.dy = 0.1


# Functions

def paddle_l_up():
    y = paddle_l.ycor()
    if y < (constatnt.SCREEN_HEIGHT/2 - 50):
        y += constatnt.SPEED
        paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    if y > (-constatnt.SCREEN_HEIGHT/2 + 50):
        y -= constatnt.SPEED
        paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    if y < (constatnt.SCREEN_HEIGHT/2 - 50):
        y += constatnt.SPEED
        paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    if y > (-constatnt.SCREEN_HEIGHT/2 + 50):
        y -= constatnt.SPEED
        paddle_r.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_l_up, "w")  # does an action when you use "w"
window.onkeypress(paddle_l_down, "s")
window.onkeypress(paddle_r_up, "Up")
window.onkeypress(paddle_r_down, "Down")

# main loop

while True:
    window.update()

    # Movement of the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > (constatnt.SCREEN_HEIGHT / 2 - 10):
        ball.sety(constatnt.SCREEN_HEIGHT/2 - 10)
        ball.dy *= -1

    if ball.ycor() < (-constatnt.SCREEN_HEIGHT / 2 + 10):
        ball.sety(-constatnt.SCREEN_HEIGHT/2 + 10)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.sety(0)
        ball.setx(0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.sety(0)
        ball.setx(0)
        ball.dx *= -1

    # paddle colision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50):   # right paddle
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() - 50): # left paddle
        ball.setx(-340)
        ball.dx *= -1

