from spellchecker  import SpellChecker
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    def correct_text(self,text):
        words = text.split()
        corrected_words = []
        for word in words :
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}' ")
                corrected_words.append(corrected_word)
        return " ".join(corrected_words)




    def run (self):
        print("\n-----𝗦𝗽𝗲𝗹𝗹𝗖𝗵𝗲𝗰𝗸𝗲𝗿-----")
        while True:
            text = input("Enter the text to ( or type exit to quit ) : ")
            if text == "exit":
                print("closing the program......")
                break
            corrected_text = self.correct_text(text)
            print(f"Corrected text : {corrected_text}")
if __name__ == "__main__":
    SpellCheckerApp().run()
    
