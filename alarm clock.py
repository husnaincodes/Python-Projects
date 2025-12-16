from pygame import mixer
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
 
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play(-1)   

    print("Alarm ringing! Press ENTER to stop.")
    input()              
    mixer.music.stop()     

minutes = int(input("How many minutes to wait?: "))
seconds = int(input("How many seconds to wait?: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
