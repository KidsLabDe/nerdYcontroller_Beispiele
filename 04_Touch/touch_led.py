import time
import board
import touchio
import neopixel

# Initialisieren Sie die Touch-Pins
touch_pins = [
    touchio.TouchIn(board.GP14),
    touchio.TouchIn(board.GP15),
    touchio.TouchIn(board.GP16),
    touchio.TouchIn(board.GP17)
]

# Initialisieren Sie die Neopixel-LEDs
num_pixels = 4
pixel_pin = board.GP12
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

def check_touch():
    """Prüft die Touch-Pins und schaltet die LEDs entsprechend ein."""
    for i, touch_pin in enumerate(touch_pins):
        if touch_pin.value:
            pixels[i] = (0, 255, 0)  # Grün bei Berührung
        else:
            pixels[i] = (0, 0, 0)  # Aus, wenn nicht berührt
    pixels.show()

while True:
    check_touch()
    time.sleep(0.1)