import time

import digitalio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import GameController


# Drücken und loslassen der Tasten W, A, S, D jeweils für 1 Sekunde

# Einfachste Variante - jede Taste nacheinander:
# Eine Liste des Tasten findest du hier:
# https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode


GameController.drueckeTaste(Keycode.H)
GameController.drueckeTaste(Keycode.A)
GameController.drueckeTaste(Keycode.L)
GameController.drueckeTaste(Keycode.L)
GameController.drueckeTaste(Keycode.O)
GameController.drueckeTaste(Keycode.SPACE) # Leertaste
GameController.drueckeTaste(Keycode.W)
GameController.drueckeTaste(Keycode.E)
GameController.drueckeTaste(Keycode.L)
GameController.drueckeTaste(Keycode.T)


time.sleep(5) # 5 Sekunden warten

# Und jetzt als Schleife:
tasten = [Keycode.W, Keycode.A, Keycode.S, Keycode.D]
for taste in tasten:
    GameController.drueckeTaste(taste, 1)
    time.sleep(0.5)  # Kurze Pause zwischen den Tastendrücken


# Cursor hier hier, der Pico tippt gleich los:
# 