from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as f:
            scores = f.readlines()
            self.high_score = int(scores[-1])
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def get_high_score(self):
        with open("data.txt", "r") as f:
            scores = f.readlines()
            self.high_score = scores[-1]
            print(f"the current high score is: {self.high_score}")
            
    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "a") as f:
                f.write(f"\n{self.score}")
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.reset()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
