import GameController
import time

def chase_effect(farbe = GameController.ROT, wartezeit = 0.1):
    """Erzeugt einen Chase-Effekt auf den Neopixel-LEDs."""
   
    for i in range(GameController.anzLEDs):
        GameController.setzeLEDFarbe(i, farbe)
        time.sleep(wartezeit)
        GameController.setzeLEDaus(i)  # LED ausschalten

    for i in range(GameController.anzLEDs - 1, -1, -1): # wir zählen rückwärts!
        GameController.setzeLEDFarbe(i, farbe)
        time.sleep(wartezeit)
        GameController.setzeLEDaus(i)  # LED ausschalten

def regenbogen(pause = 0.01):
    for j in range(255):
        for i in range(GameController.anzLEDs):
            pixel_index = (i * 256 // GameController.anzLEDs) + j
            GameController.LEDs[i] = GameController.wheel(pixel_index & 255)
        time.sleep(pause)




while True:
    # Beispiel: Roter Chase-Effekt mit einer Wartezeit von 0.1 Sekunden
    chase_effect()
    # Jetzt etwas Regenbogen...
    regenbogen()
    # Noch mal ein Chase, blau, langsam..
    # - Die Farbe wird als erster Parameter übergeben, hier BLAU
    # - Der 2. Parameter sagt, wie lange nach jeder Farbe gewartet werden soll.
    #   Also 0.2 heißt 0.2 Sekunden.
    chase_effect(GameController.BLAU,0.2)
    # und einer mit Grün - schneller! Wartet nur 0.05 sekunden.
    chase_effect(GameController.GRÜN,0.05)
