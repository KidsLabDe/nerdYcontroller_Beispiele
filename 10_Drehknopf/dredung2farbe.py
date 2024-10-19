import rotaryio
import board
import neopixel

# Farbkonstanten definieren
ROT = (255, 0, 0)
GRÜN = (0, 255, 0)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
LILA = (128, 0, 128)
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
ROSA = (255, 192, 203)
BRAUN = (165, 42, 42)

# Anzahl der LEDs und der Pin
num_pixels = 4
pixel_pin = board.GP12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

# Initialisiere den Drehencoder
encoder = rotaryio.IncrementalEncoder(board.GP1, board.GP2)
last_position = None

# Funktion zum Setzen der LED-Farbe basierend auf der Encoder-Position
def set_led_color(position):
    colors = [ROT, GRÜN, BLAU, GELB, CYAN, MAGENTA, ORANGE, LILA, WEISS, SCHWARZ, ROSA, BRAUN]
    color_index = position % len(colors)
    pixels.fill(colors[color_index])
    pixels.show()

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print("Position:", position)
        set_led_color(position)
    last_position = position