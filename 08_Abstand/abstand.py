import board
import pulseio
import time
import neopixel

# Initialisieren Sie den PWM-Eingang
sig = pulseio.PulseIn(board.GP9)

# Initialisieren Sie die Neopixel-LEDs
num_pixels = 4
pixel_pin = board.GP12
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

def abstand_messen():
    """Gibt den Abstand vom Grove Ultrasonic Ranger in cm zurück."""
    sig.pause()
    sig.clear()
    sig.resume(10)
    time.sleep(0.05)  # sollte hier len(sig) mit einem Timeout abfragen
    sig.pause()
    
    if len(sig) != 0:
        distance_cm = int(sig[0] * 0.017)
        return distance_cm
    else:
        return None

def leds_anzeigen(distance):
    """Zeigt den Abstand mit LEDs an. Pro 10 cm geht eine LED mehr an."""
    num_leds_on = min(distance // 10, num_pixels)
    for i in range(num_pixels):
        if i < num_leds_on:
            pixels[i] = (0, 255, 0)  # Grün
        else:
            pixels[i] = (0, 0, 0)  # Aus
    pixels.show()

# Beispielaufruf der Funktion und Ausgabe des Ergebnisses
while True:
    distance = abstand_messen()
    if distance is not None:
        print(f"Abstand: {distance} cm")
        leds_anzeigen(distance)
    else:
        print("Kein Signal empfangen. Bitte erneut versuchen.")
    # time.sleep(0.1)




