import time
import board
import analogio
import neopixel
import digitalio
from nerdy import pixels, num_pixels
import nerdy



# Initialisieren Sie die analogen Eingänge für die X- und Y-Achsen des Joysticks
x_achse = analogio.AnalogIn(board.GP26)
y_achse = analogio.AnalogIn(board.GP27)

# Initialisieren Sie den Schalter
schalter = digitalio.DigitalInOut(board.GP22)
schalter.direction = digitalio.Direction.INPUT
schalter.pull = digitalio.Pull.UP



def spannung_lesen(pin):
    """Gibt die Spannung des angegebenen Pins zurück."""
    return (pin.value * nerdy.MAX_SPANNUNG) / 65536

def farbe_berechnen(y_wert):
    """Gibt die Farbe basierend auf der Spannung der Y-Achse zurück."""
    # Interpolieren zwischen Grün (0 Volt) und Rot (3.3 Volt)
    gruen = int((1 - y_wert / nerdy.MAX_SPANNUNG) * 255)
    rot = int((y_wert / nerdy.MAX_SPANNUNG) * 255)
    return (rot, gruen, 0)



while True:
    x_wert = spannung_lesen(x_achse)
    y_wert = spannung_lesen(y_achse)
    
    print(f"X-Achse: {x_wert:.2f} V, Y-Achse: {y_wert:.2f} V")
    
    # Farbe basierend auf der Spannung der Y-Achse berechnen
    farbe = farbe_berechnen(y_wert)
    
    # LEDs basierend auf der Spannung der X-Achse schalten
    if x_wert < (nerdy.MAX_SPANNUNG / 4) * 1:
        pixels.fill((0, 0, 0))  # Alle LEDs ausschalten
        pixels[0] = farbe  # Erste LED einschalten
    elif x_wert < (nerdy.MAX_SPANNUNG / 4) * 2:
        pixels.fill((0, 0, 0))  # Alle LEDs ausschalten
        pixels[1] = farbe  # Zweite LED einschalten
    elif x_wert < (nerdy.MAX_SPANNUNG / 4) * 3:
        pixels.fill((0, 0, 0))  # Alle LEDs ausschalten
        pixels[2] = farbe  # Dritte LED einschalten
    else:
        pixels.fill((0, 0, 0))  # Alle LEDs ausschalten
        pixels[3] = farbe  # Vierte LED einschalten
    
    if not schalter.value:  # Wenn der Schalter gedrückt wird (LOW)
        print("Schalter gedrückt, rufe rainbow_cycle auf")
        nerdy.regenbogen()  # Rufen Sie die Funktion rainbow_cycle auf

    
    time.sleep(0.1)