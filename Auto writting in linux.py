import pyautogui as auto
import time


auto.press("win")
time.sleep(1)


auto.write("LibreOffice Writer", interval=0.2)
time.sleep(1)
auto.press("enter")


time.sleep(8)

# Click center of screen to focus document
screenWidth, screenHeight = auto.size()
auto.click(screenWidth / 2, screenHeight / 2)

time.sleep(1)


auto.write("""Hi, I’m Husnain Tayab you can find me online as husnaincodes. I’m an undergraduate FinTech student and an aspiring Data Scientist who loves exploring Python, Pandas, and Machine Learning. I also know the basics of HTML, CSS, and C++, which help me combine logic with creativity. I enjoy learning through hands-on projects, experimenting with new ideas, and sharing my progress here on GitHub.
""",interval=0.2)
auto.press("enter")
