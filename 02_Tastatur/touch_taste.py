"""
Dieses Skript ermöglicht die Eingabe von Tastatureingaben über eine kapazitive Touch-Sensor und eine Adafruit HID-Tastatur.

Verwendung:
- Verbinden Sie den kapazitiven Touch-Sensor mit den angegebenen Touch-Pins auf dem Board.
- Initialisieren Sie die Tastatur und weisen Sie den Touch-Pins entsprechende Tasten zu.
- Überwachen Sie kontinuierlich die Touch-Pins und simulieren Sie Tastendrücke/-freigaben basierend auf der Touch-Eingabe.

Funktionen:
- Keine

Klassen:
- Keine

Konstanten:
- Keine

Variablen:
- touch_pins: Eine Liste von Touch-Pins, die für die kapazitive Touch-Erkennung verwendet werden.
- tastatur: Eine Instanz der Adafruit HID-Tastaturklasse.
- tasten: Eine Liste von Keycodes, die den Touch-Pins entsprechen.
- tasten_status: Eine Liste von booleschen Werten, die den Status jeder Taste (gedrückt oder losgelassen) anzeigen.
"""
import time
import board
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialisieren Sie die Touch-Pins
touch_pins = [
    touchio.TouchIn(board.GP14),
    touchio.TouchIn(board.GP15),
    touchio.TouchIn(board.GP16),
    touchio.TouchIn(board.GP17)
]

# Initialisieren Sie die Tastatur
tastatur = Keyboard(usb_hid.devices)

# Zuordnung der Touch-Pins zu den Tasten
tasten = [Keycode.W, Keycode.A, Keycode.S, Keycode.D]

# Status der Tasten (ob sie gedrückt sind oder nicht)
tasten_status = [False, False, False, False]

while True:
    # enumerate gibt jeweils für eintrag in touch_pins den index i und den eintrag touch_pin zurück
    for i, touch_pin in enumerate(touch_pins):
        if touch_pin.value and not tasten_status[i]:
            # Taste drücken, wenn der Touch-Pin berührt wird und die Taste nicht bereits gedrückt ist
            tastatur.press(tasten[i])
            tasten_status[i] = True
            print(f"Taste {i} gedrückt")
        elif not touch_pin.value and tasten_status[i]:
            # Taste loslassen, wenn der Touch-Pin nicht mehr berührt wird und die Taste gedrückt ist
            tastatur.release(tasten[i])
            tasten_status[i] = False
            print(f"Taste {i} losgelassen")
    time.sleep(0.1)
    
    

# Cursor hier hier, der Pico tippt gleich los:
# 