import nerdy
import time
import board
import pwmio
import touchio


# Initialisieren Sie den PWM-Ausgang für den Lautsprecher
speaker = pwmio.PWMOut(board.GP20, duty_cycle=0, frequency=440, variable_frequency=True)


# Initialisieren Sie die Touch-Pins
touch_pins = [
    touchio.TouchIn(board.GP14),
    touchio.TouchIn(board.GP15),
    touchio.TouchIn(board.GP16),
    touchio.TouchIn(board.GP17)
]


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

def play_tone(frequency, duration):
    speaker.frequency = int(frequency)
    speaker.duty_cycle = 500  # 50% duty cycle
    time.sleep(duration)
    speaker.duty_cycle = 0  # Turn off the sound


#nerdY.regenbogen()


def check_touch():
    """Prüft die Touch-Pins und schaltet die LEDs entsprechend ein."""
    for i, touch_pin in enumerate(touch_pins):
        if touch_pin.value:
            nerdy.pixels[i] = (0, 255, 0)  # Grün bei Berührung
        else:
            nerdy.pixels[i] = (0, 0, 0)  # Aus, wenn nicht berührt
    nerdy.pixels.show()

play_tone(523,0.5)
play_tone(659,0.5)


while True:
# Beispiel: Roter Chase-Effekt mit einer Wartezeit von 0.1 Sekunden

    chase_effect()
    nerdy.regenbogen()
    chase_effect(nerdy.BLAU,0.2)
    chase_effect(nerdy.GRÜN,0.05)
    
    for _ in range(20):
        check_touch()
        time.sleep(0.1)
    