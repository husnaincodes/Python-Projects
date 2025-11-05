sentence = input("Enter a sentence: ").lower()
words = sentence.split()
unique_words = set(words)

for word in unique_words:
    print(f"{word}: {words.count(word)}")
