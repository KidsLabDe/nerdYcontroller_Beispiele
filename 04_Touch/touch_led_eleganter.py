import time
import board

# Macht das gleiche wie der touch_led.py code, aber mit weniger zeilen.
# Muss man schon 2 mal hinschauen zum verstehen :)

# Farben für die Touch-Pins
farben = [GameController.GRUEN, GameController.ROT, GameController.BLAU, GameController.LILA]

while True:
    for i in range(len(GameController.touch_pins)):
        if GameController.touch_pins[i].value:
            GameController.setzeLEDFarbe(i, farben[i])
        else:
            GameController.setzeLEDaus(i)
    time.sleep(0.1)