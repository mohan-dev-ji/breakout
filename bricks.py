from turtle import Turtle

class Brick(Turtle):
    
    def __init__(self, position, color, points):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        self.color(color)
        self.points = points
        