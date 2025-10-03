

import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    try:
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")

    
if __name__== "__main__":
    speak("Initializing Gaara......")
    print("Starting voice recognition...")
    while True:
        try:
             with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration =1)  
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            
                print("Recognizing wake word...")
                word = recognizer.recognize_google(audio).lower() 
                print(f"Wake word detected: {word}")
                if(word.lower()=="Gaara"):
                    speak("Gaara is listening")
                    try:
                          with sr.Microphone() as source:
                            print("Gaara Active....")
                            recognizer.adjust_for_ambient_noise(source, duration=1)
                          
                            audio = recognizer.listen(source ,timeout=5, phrase_time_limit=5)
                            print("Recognizing command...")

                            command = recognizer.recognize_google(audio)

                            print(f"Command recognized: {command}")

                            speak(f"You said {command}")

                            if command.lower() in ["exit", "quit", "stop"]:
                                speak("Shutting down Gaara...")

                                print("Exiting program.")
                                break
                    except sr.UnknownValueError:

                        print("Sorry, I could not understand.")
                    except sr.RequestError:

                        print("Network error. Check your internet.") 
        except sr.UnknownValueError:

            print("Sorry, could not understand the wake word.")

            # Optionally, don't speak here to avoid repetitive feedback
        except sr.RequestError as e:
            print(f"Network error in wake word recognition: {e}")

            speak("Network error. Please check your internet.")

        except Exception as e:
            print(f"Error (possibly microphone): {e}")
            
            speak("Error with microphone or audio. Please check your microphone.")
            continue  # Continue to retry after error



