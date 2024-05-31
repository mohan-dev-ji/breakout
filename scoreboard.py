from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        # self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 30, "normal"))
        

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("red")
        self.write(f"Game Over", align="center", font=("Courier", 80, "normal"))
        self.goto(0,-80)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 50, "normal"))

    def toggle_game_over(self, visible):
        self.clear()
        if visible:
            self.game_over()

    def you_win(self):
        self.clear()
        self.goto(0,0)
        self.color("green")
        self.write(f"You Win", align="center", font=("Courier", 80, "normal"))

    def toggle_you_win(self, visible):
        self.clear()
        if visible:
            self.you_win()
    