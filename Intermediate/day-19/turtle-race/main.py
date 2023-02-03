from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
screen.title("Turtle Race")
user_bet = screen.textinput("make a bet", "who do you think will win the race? (red, orange, yellow, green, blue, purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []
is_race_on = False
places = []

for i in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y_positions[i])
    turtles.append(tim)

if user_bet:
    is_race_on = True

def end_game():
    print("here are the places:")
    for i in range(0, 6):
        print(f"{i + 1}. {places[i].pencolor()}")

    print(f"\nyour selection: {user_bet}")

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle not in places:
                places.append(turtle)
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    if len(places) == 6: 
        is_race_on = False
        end_game()


screen.exitonclick()