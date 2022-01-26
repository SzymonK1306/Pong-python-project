import turtle

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle left

paddle_l = turtle.Turtle()
paddle_l.speed(0)       # speed of animation
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(5, 1)    # size of the paddle 1*20
paddle_l.penup()
paddle_l.goto(-350, 0)  # start location


# Paddle right
paddle_r = turtle.Turtle()
paddle_r.speed(0)       # speed of animation
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(5, 1)    # size of the paddle 1*20
paddle_r.penup()
paddle_r.goto(350, 0)  # start location
# Ball
ball = turtle.Turtle()
ball.speed(0)       # speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # start location
# main loop

while True:
    window.update()




