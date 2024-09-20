import time
import board
import analogio
import neopixel
import digitalio
import GameController



# Initialisieren Sie die analogen Eingänge für die X- und Y-Achsen des Joysticks
x_achse = analogio.AnalogIn(board.GP26)
y_achse = analogio.AnalogIn(board.GP27)

# Initialisieren Sie den Schalter
schalter = digitalio.DigitalInOut(board.GP22)
schalter.direction = digitalio.Direction.INPUT
schalter.pull = digitalio.Pull.UP



def spannung_lesen(pin):
    """Gibt die Spannung des angegebenen Pins zurück."""
    return (pin.value * GameController.MAX_SPANNUNG) / 65536

def farbe_berechnen(y_wert):
    """Gibt die Farbe basierend auf der Spannung der Y-Achse zurück."""
    # Interpolieren zwischen Grün (0 Volt) und Rot (3.3 Volt)
    gruen = int((1 - y_wert / GameController.MAX_SPANNUNG) * 255)
    rot = int((y_wert / GameController.MAX_SPANNUNG) * 255)
    return (rot, gruen, 0)



def regenbogen(pause = 0.01):
    for j in range(255):
        for i in range(GameController.anzLEDs):
            pixel_index = (i * 256 // GameController.anzLEDs) + j
            GameController.LEDs[i] = GameController.wheel(pixel_index & 255)
        time.sleep(pause)


while True:
    x_wert = spannung_lesen(x_achse)
    y_wert = spannung_lesen(y_achse)
    
    print(f"X-Achse: {x_wert:.2f} V, Y-Achse: {y_wert:.2f} V")
    
    # Farbe basierend auf der Spannung der Y-Achse berechnen
    farbe = farbe_berechnen(y_wert)
    
    GameController.setzeAlleAus()  # Alle LEDs ausschalten
    
    # LEDs basierend auf der Spannung der X-Achse schalten
    if x_wert < (GameController.MAX_SPANNUNG / 4) * 1:
        GameController.setzeLEDFarbe(0,farbe)
    elif x_wert < (GameController.MAX_SPANNUNG / 4) * 2:
        GameController.setzeLEDFarbe(1,farbe)
    elif x_wert < (GameController.MAX_SPANNUNG / 4) * 3:
        GameController.setzeLEDFarbe(2,farbe)
    else:
        GameController.setzeLEDFarbe(3,farbe)
    
    if not schalter.value:  # Wenn der Schalter gedrückt wird (LOW)
        print("Schalter gedrückt, rufe rainbow_cycle auf")
        regenbogen()  # Rufen Sie die Funktion rainbow_cycle auf

    
    time.sleep(0.1)