import turtle
import time
import random


WIDTH ,HEIGHT = 500,500
COLORS = ["red","green","green","yellow","blue","cyan","brown","pink","orange","purple"]

def get_number_of_racers():
    racers = 0

    while True:
        racers = input("Enter a number between (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Try Again ..... ")
            continue

        if 2<=racers<=10:
            return racers
        else:
            print("Number not in range (2-10). Try again...")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!")


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            x,y = racer.pos()
            if y >=HEIGHT//2-10:
                return colors[turtles.index(racer)]
            
            
def create_turtles(colors):
    turtles = []
    spacing = WIDTH//(len(colors)+1)
    for i ,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2+(i+1)*spacing,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)

print("The winner of the turtle with color:",winner)
time.sleep(5)