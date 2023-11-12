import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

key = str(input("key: "))
key = key[0]

toggleKey = KeyCode(char=key)
rate = False

while rate == False:
    try:
        rate = float(input("rate (0.001 reccomended): "))
    except:
        print("please try again")

print(f"\nto start autoclicker press {toggleKey}")
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(rate)

def toggle_event(key):
    if key == toggleKey:
        global clicking
        clicking = not clicking

clickThread = threading.Thread(target=clicker)
clickThread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

input("press enter to exit")
