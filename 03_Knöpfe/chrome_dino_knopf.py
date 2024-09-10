import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialisieren Sie den Knopf
knopf = digitalio.DigitalInOut(board.GP4)
knopf.direction = digitalio.Direction.INPUT
knopf.pull = digitalio.Pull.UP

# Initialisieren Sie die Tastatur
tastatur = Keyboard(usb_hid.devices)

# Status des Knopfes (ob er gedrückt ist oder nicht)
knopf_status = False

print("chrome://dino/")

while True:
    if not knopf.value and not knopf_status:
        # Wenn der Knopf gedrückt wird und vorher nicht gedrückt war
        tastatur.press(Keycode.SPACE)
        tastatur.release(Keycode.SPACE)
        print("SPACE gedrückt")
        knopf_status = True
    elif knopf.value and knopf_status:
        # Wenn der Knopf losgelassen wird
        knopf_status = False
    
    time.sleep(0.1)          