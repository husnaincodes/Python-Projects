import pyautogui as auto
import time

auto.press("win")
time.sleep(1)

auto.write("LibreOffice Writer",interval=0.2)
auto.press("enter")
