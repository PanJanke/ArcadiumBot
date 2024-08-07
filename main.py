import pyautogui
import time

def click_and_drag():
    # Move to the starting position (you can adjust these coordinates) (936, 553)
    start_x, start_y = 936, 553
    pyautogui.moveTo(start_x, start_y)
    pyautogui.click()
    pyautogui.click()

    # Press and hold the left mouse button
    pyautogui.mouseDown(button='left')

    # Move the mouse left and right
    try:
        while True:
            pyautogui.moveRel(50, 0, duration=0.25)  # Move right
            pyautogui.moveRel(-50, 0, duration=0.25) # Move left
    except KeyboardInterrupt:
        # Release the mouse button on interrupt (Ctrl+C)
        pyautogui.mouseUp(button='left')
        print("Mouse button released")

if __name__ == "__main__":
    # Give the user a few seconds to switch to the game window
    print("Starting in 3 seconds...")
    time.sleep(3)
    click_and_drag()


##Mouse clicked at (709, 143)
Mouse clicked at (1210, 150)
Mouse clicked at (1207, 66)