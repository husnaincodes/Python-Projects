
word = input("Enter a word: ").lower()
repeated = []

for letter in set(word):
    if word.count(letter) > 1:
        repeated.append(letter)

print(", ".join(repeated))
