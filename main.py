import GameController
import time
import board
import pwmio





def chase_effect(farbe = GameController.ROT, wartezeit = 0.1):
    """Erzeugt einen Chase-Effekt auf den Neopixel-LEDs."""
   
    for i in range(GameController.anzLEDs):
        GameController.LEDs[i] = farbe
        time.sleep(wartezeit)
        GameController.LEDs[i] = GameController.SCHWARZ  # LED ausschalten

    for i in range(GameController.anzLEDs - 1, -1, -1): # wir zählen rückwärts!
        GameController.LEDs[i] = farbe
        time.sleep(wartezeit)
        GameController.LEDs[i] = GameController.SCHWARZ  # LED ausschalten

def play_tone(frequency, duration):
    speaker.frequency = int(frequency)
    speaker.duty_cycle = 500  # 50% duty cycle
    time.sleep(duration)
    speaker.duty_cycle = 0  # Turn off the sound


#GameController.regenbogen()


def check_touch():
    """Prüft die Touch-Pins und schaltet die LEDs entsprechend ein."""
    for i, GameController.touch_pin in enumerate(GameController.touch_pins):
        if GameController.touch_pin.value:
            GameController.LEDs[i] = (0, 255, 0)  # Grün bei Berührung
        else:
            GameController.LEDs[i] = (0, 0, 0)  # Aus, wenn nicht berührt
    GameController.LEDs.show()

GameController.spiele_ton(523,0.5)
GameController.spiele_ton(659,0.5)


while True:
# Beispiel: Roter Chase-Effekt mit einer Wartezeit von 0.1 Sekunden

    chase_effect()
    GameController.regenbogen()
    chase_effect(GameController.BLAU,0.2)
    chase_effect(GameController.GRÜN,0.05)
    
    for _ in range(20):
        check_touch()
        time.sleep(0.1)
    