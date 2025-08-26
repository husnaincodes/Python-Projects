
import random
while True:
    choice = input("Roll the Dice? choose (Yes/No) : ").lower()
    if choice=="yes" or choice=="YES":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"{dice1},{dice2}")
    elif(choice=="no"or choice=="NO"):
        print("Thank You!")
        break
    else:
        print("Something went wrong!")
