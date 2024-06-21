import pyautogui
import time
import keyboard  # Import the keyboard library

running = False  # Flag to indicate whether the loop should run

def mesaj():
    pyautogui.write("Hi")
    pyautogui.press("enter")
    time.sleep(0.2)

def toggle_running():
    global running
    running = not running

# Register the 's' key press event
keyboard.add_hotkey('s', toggle_running)

while True:
    if running:
        mesaj()
