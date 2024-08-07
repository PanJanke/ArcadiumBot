from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y})")

# Set up the listener
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
##  Mouse clicked at (936, 553) < start // choose skip