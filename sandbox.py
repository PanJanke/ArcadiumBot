import pyautogui
from PIL import Image
import time



time.sleep(1)
# Define the screen region (left, top, width, height)
screen_region = (709, 50, 500, 90)
screenshot = pyautogui.screenshot(region=screen_region)
screenshot.save('gameOver.png')
