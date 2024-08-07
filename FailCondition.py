import pyautogui
from PIL import Image
import time


def image_matches(screen_region, image_path, threshold=0.9):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=screen_region)

    # Open the reference image
    reference_image = Image.open(image_path)

    # Compare the images
    screenshot = screenshot.convert("RGB")
    reference_image = reference_image.convert("RGB")

    # Ensure the images are the same size
    if screenshot.size != reference_image.size:
        return False

    # Get the pixel data
    screenshot_data = list(screenshot.getdata())
    reference_data = list(reference_image.getdata())

    # Calculate the similarity ratio
    match_count = sum(1 for s, r in zip(screenshot_data, reference_data) if s == r)
    similarity_ratio = match_count / len(reference_data)

    return similarity_ratio >= threshold


# Define the screen region (left, top, width, height)
screen_region = (709, 50, 500, 90)  # Adjust this to your needs
image_path = "Screenshots/gameOver.png"  # Path to the reference image

# Check periodically
while True:
    if image_matches(screen_region, image_path):
        print("The images match!")
    else:
        print("The images do not match.")

    # Wait before checking again
    time.sleep(1)
