
def adventure_game():
    
    print("Welcome! to the Adventure Game")

    name = input("Enter your name please : ")

    print(f"{name}! You are standing at the entrance of a dark forest. ")

    print("You have two options: Go RIGHT or LEFT.")

    choice = input("Where do you want to go? (right/left): ").strip().lower()
    
    if choice== "left":
        print("\nYou walk left and reach a river.")

        print("You can either SWIM across or BUILD a raft.")
        choice2 = input("What do you do? (swim/raft): ").strip().lower()

        if choice2 == "swim":
            print("\nYou try to swim, A crocodile eats you . Game Over!")

        elif(choice2=="raft"):
            print("\nYou build a raft and cross safely. On the other side, you find a treasure chest! 🎉 You win!")
        else:
            print("Invalid choice")   

    elif choice == "right":
        print("\nYou walk right and see a tall mountain.")

        print("You can either CLIMB it or GO around it.")

        choice2 = input("What do you do? (climb/around): ").strip().lower()

        if choice2 == "climb":
            print("\nYou climb the mountain and find a wise sage . He gives you a magical sword. You win!")


        elif choice2 == "around":

            print("\nYou go around the mountain but get lost in the forest forever... Game Over ")
        else:
            print("Invalid choice! A wolf attacks you . Game Over!")

    else:
        print("You stand still and do nothing... A wild bear finds you . Game Over!")
adventure_game()
