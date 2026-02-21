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


auto.write("""Dear Ma’am,

I hope you are doing well.

I sincerely apologize for forgetting to submit the assignment on the given deadline. I have now attached the completed assignment with this email for your kind review.

I will also submit the physical (hard copy) of the assignment on **Wednesday**, as required.

I kindly request you to please consider my submission. I will be very careful with deadlines in the future.

Thank you so much for your time and understanding.

Best regards,
Husnain
""",interval=0.2)
auto.press("enter")
