import turtle
import random

# Turtles
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtles = []

for i in range(6):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.speed(1)
    t.setposition(x=-330, y=-50 * i)
    t.name = colors[i]
    turtles.append(t)

# Setup
screen = turtle.Screen()
screen.setup(width=700, height=700)

# User input
user_choice = screen.textinput("Turtle Race", "Enter your turtle:").lower()

# Main loop
while True:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() > 330:
            print("You won!") if t.name == user_choice else print("You lost!")
            break
    else:
        continue
    break

screen.exitonclick()