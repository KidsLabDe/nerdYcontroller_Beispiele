import nerdy
import time

def chase_effect(farbe = nerdy.ROT, wartezeit = 0.1):
    """Erzeugt einen Chase-Effekt auf den Neopixel-LEDs."""
   
    for i in range(nerdy.num_pixels):
        nerdy.pixels[i] = farbe
        time.sleep(wartezeit)
        nerdy.pixels[i] = nerdy.SCHWARZ  # LED ausschalten

    for i in range(nerdy.num_pixels - 1, -1, -1): # wir zählen rückwärts!
        nerdy.pixels[i] = farbe
        time.sleep(wartezeit)
        nerdy.pixels[i] = nerdy.SCHWARZ  # LED ausschalten



#nerdY.regenbogen()


while True:
# Beispiel: Roter Chase-Effekt mit einer Wartezeit von 0.1 Sekunden
    chase_effect()
    nerdy.regenbogen()
    chase_effect(nerdy.BLAU,0.2)
    chase_effect(nerdy.GRÜN,0.05)
