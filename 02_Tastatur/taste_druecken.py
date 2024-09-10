import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialisieren Sie die Tastatur
tastatur = Keyboard(usb_hid.devices)

def taste_druecken(taste, dauer):
    """Drückt eine Taste für eine bestimmte Dauer und lässt sie dann los."""
    tastatur.press(taste)
    time.sleep(dauer)
    tastatur.release(taste)

# Drücken und loslassen der Tasten W, A, S, D jeweils für 1 Sekunde
tasten = [Keycode.W, Keycode.A, Keycode.S, Keycode.D]
for taste in tasten:
    taste_druecken(taste, 1)
    time.sleep(0.5)  # Kurze Pause zwischen den Tastendrücken

# Tastatur loslassen
tastatur.release_all()


