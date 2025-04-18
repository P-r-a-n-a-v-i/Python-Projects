import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour


direction = [0,90,180,270]
tim.pensize(25)
tim.speed("fastest")
for _ in range(100):
    tim.setheading(random.choice(direction))
    tim.forward(36)
    tim.color(random_colour())
