from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0,-270)

    def go_left(self):
        # print("go up")
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())