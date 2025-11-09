sentence = input("Enter a sentence: ").lower()
vowels = {'a', 'e', 'i', 'o', 'u'}

for word in sentence.split():
    unique_vowels = set(word) & vowels
    print(f"{word} {', '.join(unique_vowels)}")
