import time
import board
import pwmio

# Initialisieren Sie den PWM-Ausgang für den Lautsprecher
speaker = pwmio.PWMOut(board.GP20, duty_cycle=0, frequency=440, variable_frequency=True)

# Notenfrequenzen in Hertz
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

def play_tone(frequency, duration):
    """Spielt einen Ton mit einer bestimmten Frequenz und Dauer."""
    speaker.frequency = frequency
    speaker.duty_cycle = 49152  # 75% Duty Cycle
    time.sleep(duration)
    speaker.duty_cycle = 0  # Ton ausschalten
    time.sleep(0.05)  # Kurze Pause zwischen den Tönen

def play_melody():
    """Spielt eine kleine Melodie."""
    melody = [
        (C4, 0.5),
        (D4, 0.5),
        (E4, 0.5),
        (F4, 0.5),
        (G4, 0.5),
        (A4, 0.5),
        (B4, 0.5),
        (C5, 0.5)
    ]
    
    for note in melody:
        play_tone(note[0], note[1])

# Beispielaufruf der Funktion, um die Melodie zu spielen
play_melody()
