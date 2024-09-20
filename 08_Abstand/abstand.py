import time
import board
import GameController
import adafruit_hcsr04

abstand = adafruit_hcsr04.HCSR04(trigger_pin=board.GP21, echo_pin=board.GP22)

def leds_anzeigen(distance):
    """Zeigt den Abstand mit LEDs an. Pro 10 cm geht eine LED mehr an."""
    anzLEDs_on = min(distance // 10, GameController.anzLEDs)
    for i in range(GameController.anzLEDs):
        if i < anzLEDs_on:
            GameController.setzeLEDFarbe(i,GameController.GRÜN)
        else:
            GameController.setzeLEDaus(i)






while True:
    try:
        print((abstand.distance))
        leds_anzeigen(abstand.distance)

    except RuntimeError:
        print("Nicht angeschlossen!")
        pass
    time.sleep(0.1)
    
    
    
    
    