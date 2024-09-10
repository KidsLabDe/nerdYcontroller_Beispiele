import time
import board
import analogio
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

# Initialisieren Sie die analogen Eingänge für die X- und Y-Achsen des Joysticks
x_achse = analogio.AnalogIn(board.GP26)
y_achse = analogio.AnalogIn(board.GP27)

# Initialisieren Sie den Schalter für den Mausklick
schalter = digitalio.DigitalInOut(board.GP22)
schalter.direction = digitalio.Direction.INPUT
schalter.pull = digitalio.Pull.UP

# Initialisieren Sie die Maus
maus = Mouse(usb_hid.devices)

def spannung_lesen(pin):
    """Gibt die Spannung des angegebenen Pins zurück."""
    return (pin.value * 3.3) / 65536

def bewegung_berechnen(spannung, mittel_spannung=1.65, schwelle=0.1):
    """Berechnet die Mausbewegung basierend auf der Spannung."""
    if abs(spannung - mittel_spannung) < schwelle:
        return 0
    return int((spannung - mittel_spannung) * 10)

while True:
    x_wert = spannung_lesen(x_achse)
    y_wert = spannung_lesen(y_achse)
    
    x_bewegung = -bewegung_berechnen(x_wert) # hier muss ein MINUS hin, das drehn die Bewegung um
    y_bewegung = bewegung_berechnen(y_wert)
    
    print(f"X-Achse: {x_wert:.2f} V, Y-Achse: {y_wert:.2f} V")
    print(f"X-Bewegung: {x_bewegung}, Y-Bewegung: {y_bewegung}")
    
    maus.move(x=x_bewegung, y=y_bewegung)
    
    if not schalter.value:  # Wenn der Schalter gedrückt wird (LOW)
        maus.click(Mouse.LEFT_BUTTON)
        print("Mausklick")
    
    time.sleep(0.1)