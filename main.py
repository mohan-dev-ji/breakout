from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left,"Left")
screen.onkey(paddle.go_right,"Right")

bricks = []
# Define the grid layout
rows = 4
cols = 10
x_start = -365
y_start = 240
x_offset = 80
y_offset = 30

# Create position the bricks and color each row
for row in range(rows):
    if row == 0:
        row_color = "red"
        row_points = 4
    elif row == 1:
        row_color = "orange"
        row_points = 3
    elif row == 2:
        row_color = "green"
        row_points = 2
    elif row == 3:
        row_color = "yellow"
        row_points = 1
    for col in range(cols):
        x = x_start + col * x_offset
        y = y_start - row * y_offset
        brick = Brick((x, y), row_color, row_points)
        bricks.append(brick)


# detect collision with brick
def check_collision():
    for i in bricks:
        if ball.distance(i) < 20:
            ball.bounce_y()
            i.goto(2000, 2000)
            scoreboard.increase_score(i.points)
            bricks.remove(i)

# Flashing game over function
flashing = False
def flash_game_over():
    global flashing
    flashing = not flashing
    scoreboard.toggle_game_over(flashing)
    if not game_is_on:
        screen.ontimer(flash_game_over, 500)        

# Flashing you win function  
flashing = False
def flashing_you_win():
    global flashing
    flashing = not flashing
    scoreboard.toggle_you_win(flashing)
    if not game_is_on:
        screen.ontimer(flashing_you_win, 500)        

ball = Ball()

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    if ball.ycor() < -400:
        ball.out_of_bounds()
        game_is_on = False
        # scoreboard.game_over()
        
    # detect collision with right paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -250:
        ball.bounce_y()

    # detect collision with walls
    if ball.xcor() > 370 or ball.xcor() < -370:
        ball.bounce_x()
    if ball.ycor() > 270:
        ball.bounce_y()
    
    # detect collision with brick
    check_collision()

    # End the game if all bricks are removed or other end condition
    if not bricks:
        flashing_you_win()

flash_game_over()
screen.exitonclick()