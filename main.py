import nerdy
import time
import pwmio
import board

# Initialisieren Sie den PWM-Ausgang für den Lautsprecher
speaker = pwmio.PWMOut(board.GP20, duty_cycle=0, frequency=440, variable_frequency=True)

# Frequenzen für die Töne
NOTE_C5 = 523
NOTE_E5 = 659
NOTE_G5 = 784
NOTE_A5 = 880
NOTE_B5 = 988
NOTE_C6 = 1047
NOTE_D6 = 1175
NOTE_E6 = 1319
NOTE_F6 = 1397
NOTE_G6 = 1568

# Tetris-Melodie (Korobeiniki)
melody = [
    NOTE_E5, NOTE_B5, NOTE_C6, NOTE_D6, NOTE_C6, NOTE_B5, NOTE_A5, NOTE_A5, 
    NOTE_C6, NOTE_E6, NOTE_D6, NOTE_C6, NOTE_B5, NOTE_E5, NOTE_G5, NOTE_A5,
    NOTE_F6, NOTE_A5, NOTE_G5, NOTE_F6, NOTE_E6, NOTE_C6, NOTE_E6, NOTE_D6,
    NOTE_C6, NOTE_B5, NOTE_C6, NOTE_D6, NOTE_E6, NOTE_C6, NOTE_A5, NOTE_A5
]

# Notendauern (in Sekunden)
note_durations = [
    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
    0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3
]



def play_tone(frequency, duration):
    speaker.frequency = int(frequency)
    speaker.duty_cycle = 40000  # 50% duty cycle
    time.sleep(duration)
    speaker.duty_cycle = 0  # Turn off the sound

def play_melody():
    # Play the melody
    for i in range(len(melody)):
        play_tone(melody[i], note_durations[i])
        time.sleep(0.05)  # Brief pause between notes
    

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
    chase_effect(nerdy.GRÜN,0.05) # Beispiel: Grüner Chase-Effekt mit einer Wartezeit von 0.05 Sekunden

    play_melody()
    time.sleep(2) 