import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
# Initialisieren Sie die Tastatur
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)

# Funktion zum Senden eines Textes
def send_text(text):
    keyboard_layout.write(text)

# Beispieltext, der gesendet werden soll
text_to_send = "Hallo, dies ist ein Testtext!"

# Warten Sie kurz, bevor Sie den Text senden
time.sleep(2)

# Senden Sie den Text
send_text(text_to_send)

# Tastatur loslassen
keyboard.release_all()

# bitte hier den cursor hinstellen, er schreibt ja:
# 