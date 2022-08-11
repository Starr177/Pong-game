import turtle as t
import os
    
# The games score
player_A_score = 0
player_B_score = 0

# Window set up
drawing_area = t.Screen()  # making the playing window 
drawing_area.setup(width= 800, height = 600) # the size of the window
drawing_area.bgcolor("DodgerBlue") # window background color
drawing_area.tracer(0)
drawing_area.title("My first game")


# Creating right paddle 

left_paddle = t.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.shapesize(stretch_len=1,stretch_wid=5.5)
left_paddle.color("yellow")
left_paddle.penup()
left_paddle.goto(-350,0)


# Creating left paddle 

right_paddle = t.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_len=1,stretch_wid=5.5)
right_paddle.color("yellow")
right_paddle.penup()
right_paddle.goto(350,0)


# Creating simplified functions to move the paddles

def playerRight():
    y = left_paddle.ycor()
    y = y + 30
    left_paddle.sety(y)
def playerLeft():
    y = left_paddle.ycor()
    y = y - 30
    left_paddle.sety(y)
    
def playerUp():
    y = right_paddle.ycor()
    y = y + 30
    right_paddle.sety(y)
def playerDown():
    y = right_paddle.ycor()
    y = y - 30
    right_paddle.sety(y)

t.listen()
t.onkeypress(playerRight,"w")
t.onkeypress(playerLeft, "s")
t.onkeypress(playerUp, "Up")
t.onkeypress(playerDown,"Down")

# Creating the ping pong ball
ball = t.Turtle()
ball.speed = 10
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0,0)
ball_dx = 4    # Setting up the pixels for the ball movement(speed)
ball_dy = 4


# Creating a pen to update the score for player A & B

pen = t.Turtle()
pen.speed(0)
pen.color("Darkviolet")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0",align="center",font=("Comic Sans MS",24,"normal"))
pen.goto(0,-260)
pen.write("Player B: 0",align="center",font=("Comic Sans MS",24,"normal"))


# these lines keep the game window open 
while True:
    drawing_area.update()
    
    #Setting up the ball movement visualization
    ball.setx(ball.xcor()+ ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    
#setting up the border
    if ball.ycor() > 290:   # right top side border
        ball.sety(290)
        ball_dy = ball_dy * -1
        
        
    if ball.ycor() < -290:  # Left top side Border
         ball.sety(-290)
         ball_dy = ball_dy * -1
         
    if ball.xcor() > 390:   # an if statement when the ball passes the pedal
         ball.goto(0,0)
         ball_dx = ball_dx * -1
         player_A_score = player_A_score + 1
         pen.clear()
         pen.goto(0,260)
         pen.write("Player A: {}  ".format(player_A_score),align="center",font=("Comic Sans MS",24,"normal"))
         pen.goto(0,-260)
         pen.write("Player B: {}  ".format(player_B_score),align="center",font=("Comic Sans MS",24,"normal"))


    if (ball.xcor()) < -390: # an if statement when the ball passes the pedal
         ball.goto(0,0)
         ball_dx = ball_dx * -1
         player_B_score = player_B_score + 1
         pen.clear()
         pen.goto(0,-260)
         pen.write("Player B: {}  ".format(player_B_score),align="center",font=("Comic Sans MS",24,"normal"))
         pen.goto(0,260)
         pen.write("Player A: {}  ".format(player_A_score),align="center",font=("Comic Sans MS",24,"normal"))
         
   
   
    
    # the ball colliding with the pedals 
    
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
         ball.setx(340)
         ball_dx = ball_dx * -1
      

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
         ball.setx(-340)
         ball_dx = ball_dx * -1
       
         
        
