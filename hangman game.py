import random
with open("words.txt", "r") as f:
    data = f.read() 
words = data.split()

word = random.choice(words).upper()

total_chance = 10
guessed_word ="_"*len(word)

while total_chance!=0:

    print(guessed_word)

    letter = input("GUESS A LETTER : ").upper()
    if letter in word:
        for  index in range(len(word)):
            if word[index] == letter: 
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
        if guessed_word == word:
            print("🎉 Congratulation you won the game !!!!!")
            break
    else:
        total_chance-=1
        print("❌ Incorrect guess!!!!!")
        print(f"Remaining chance is :{total_chance}")
else:
    print("💀 Game Over!!!!")

    print("You lose!!!")

print(f"The correct word is :{word}")































