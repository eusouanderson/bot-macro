import pyautogui
from time import sleep

screenWidth, screenHeight = pyautogui.size()
pyautogui.mouseInfo()

while True:
    x, y = pyautogui.position()
    sleep(1)
    print(x, y)


