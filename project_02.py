
import random
number = random.randint(1,100)

try:
        while True:
            choice = int(input("Gusse the number between 1 to 100 : "))
   
            if(choice<number):
                print(" Your number is low")
        
            elif(choice>number):
             print(" Your number is  high")
       
            elif(choice==number):
                print(f"Congratulation! You gusse the correct number: {number}")
        
                break
except ValueError:
        print("Please enter a valid number!")