import time
import board
import pwmio
import GameController


# Notenfrequenzen in Hertz
C4 = 262
D4 = 294
E4 = 330
F4 = 349
G4 = 392
A4 = 440
B4 = 494
C5 = 523

def spiele_ton(frequenz, laenge):
    """Spielt einen Ton mit einer bestimmten Frequenz und Dauer."""
    GameController.lautsprecher.frequency = frequenz
    GameController.lautsprecher.duty_cycle = 49152  # 75% Duty Cycle
    time.sleep(laenge)
    GameController.lautsprecher.duty_cycle = 0  # Ton ausschalten
    time.sleep(0.05)  # Kurze Pause zwischen den Tönen


while True:
    """Spielt eine kleine Melodie."""
    melody = [
        (C4, 0.5),
        (D4, 0.5),
        (E4, 0.5),
        (F4, 0.5),
        (G4, 0.5),
        (A4, 0.5),
        (B4, 0.5),
        (C5, 1)
    ]
    
    for note in melody:
        spiele_ton(note[0], note[1])

    time.sleep(3)