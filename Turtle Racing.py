import turtle
import time
WIDTH ,HEIGHT = 500,500

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


racers = get_number_of_racers()
init_turtle()
racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.left(90)
racer.backward(100)

time.sleep(5)
