import pyautogui as auto
import time

auto.press("win")
time.sleep(1)
# change libraoffice into notepad it works without error

auto.write("LibreOffice Writer",interval=0.2) 
auto.press("enter")

time.sleep(1)
auto.write("Hello world",interval=0.2)
auto.press("enter")

auto.write("python",interval=0.2)
auto.press("enter")