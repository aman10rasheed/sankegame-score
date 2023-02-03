from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align='center', font=('Arial', 10, 'normal'))


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align='center', font=('Arial', 10, 'normal'))


    def gameover(self):
        self.color("red")
        self.goto(0,0)
        self.write("GAME OVER",align='center', font=('Arial', 10, 'normal'))
