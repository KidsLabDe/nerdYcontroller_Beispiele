import time
import board
import GameController





while True:
    # Prüfe, ob der Touch-Pin 1 gedrückt ist:
    if GameController.touch_pins[0].value == True:
        # Wenn ja, dann schalte die erste Lampe auf GRUEN:
        GameController.setzeLEDFarbe(0,GameController.GRÜN)
    else: 
        # Wenn nicht, dass schalte die erste Lampe aus:
        GameController.setzeLEDaus(0)
    
    """ Vielleicht schon aufgefallen, die Computer fangen immer bei 0 zum zählen an - drum ist der 1. Pin = pin[0] """
    
    # und so weiter mit Pin 1...
    if GameController.touch_pins[1].value == True:
        GameController.setzeLEDFarbe(1,GameController.ROT)
    else: 
        GameController.setzeLEDaus(1)
    # Pin2...
    if GameController.touch_pins[2].value == True:
        GameController.setzeLEDFarbe(2,GameController.BLAU)
    else: 
        GameController.setzeLEDaus(2)

    # ...weisst du eh!
    if GameController.touch_pins[3].value == True:
        GameController.setzeLEDFarbe(3,GameController.LILA)
    else: 
        GameController.setzeLEDaus(3)


    time.sleep(0.1)