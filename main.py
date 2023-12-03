import os
import time
import pyautogui


PAGES = 1
SLEEP_SECONDS = 1
TURNING_PAGE_POINT = {"x": 897, "y": 54}
CAPTURE_REGION = {
    "x_left": 723,
    "x_right": 1419,
    "y_top": 70,
    "y_bottom": 1075
}
FILE_NAME_PREFIX = "this_is_prefix-"
FILE_DIR = os.path.join(os.getcwd(), "captures")


def turn_page():
    pyautogui.moveTo(
        TURNING_PAGE_POINT["x"],
        TURNING_PAGE_POINT["y"]
    )
    pyautogui.click()


def capture(page):
    NOMBRE = str(page).zfill(2)
    FILE_NAME = f"{FILE_NAME_PREFIX}--{NOMBRE}.png"
    FILE_PATH = os.path.join(FILE_DIR, FILE_NAME)
    print(FILE_PATH)
    print(f"NOMBRE={NOMBRE}")
    pyautogui.screenshot(FILE_PATH, region=(
        CAPTURE_REGION["x_left"],
        CAPTURE_REGION["y_top"],
        CAPTURE_REGION["x_right"] - CAPTURE_REGION["x_left"],
        CAPTURE_REGION["y_bottom"] - CAPTURE_REGION["y_top"]
    ))


def setup():
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)
    time.sleep(SLEEP_SECONDS)


def process():
    setup()
    for num in range(PAGES):
        PAGE = num+1
        time.sleep(SLEEP_SECONDS)
        capture(PAGE)
        turn_page()


process()
