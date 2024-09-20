import time
import board
import busio
import math
import neopixel
import GameController

def drehung_zu_farbe(winkel):
    """Konvertiert die Drehung in eine Farbe."""
    if winkel < 0.1:
        return GameController.GRÜN
    if winkel < 0.4:
        return GameController.GELB
    else:
        return GameController.ROT
 
while True:
    # Beschleunigungsdaten lesen (x, y, z Achsen in m/s^2)
    beschl_x, beschl_y, beschl_z = GameController.neigung_roh()
    
    print(f"Beschleunigung: X: {beschl_x:.2f} m/s^2, Y: {beschl_y:.2f} m/s^2, Z: {beschl_z:.2f} m/s^2")

    # Gyroskopdaten lesen (x, y, z Achsen in Grad pro Sekunde)
    drehung_x, drehung_y, drehung_z = GameController.drehung()
    print(f"Gyroskop: X: {drehung_x:.2f} dps, Y: {drehung_y:.2f} dps, Z: {drehung_z:.2f} dps")

    temp = GameController.temperatur()
    print(f"Temperatur: {temp:.2f} Grad Celsius")

    # Winkelberechnung
    winkel_x, winkel_y, winkel_z = GameController.neigung()


    print(f"Winkel: X: {winkel_x:.2f}°, Y: {winkel_y:.2f}°, Z: {winkel_z:.2f}°")

    # Überprüfen, ob die Bewegung stark ist
    if GameController.ist_bewegung_stark():
        # Setze alle LEDs auf rot
        for i in range(0,4):
            GameController.setzeAlleFarbe(GameController.ROT)
            time.sleep(0.2)
            GameController.setzeAlleAus()
            time.sleep(0.2)
    else:
        # Farbe basierend auf den Winkeln berechnen
        color_x = drehung_zu_farbe(drehung_x)
        color_y = drehung_zu_farbe(drehung_y)
        color_z = drehung_zu_farbe(drehung_z)

        # LEDs entsprechend der berechneten Farben setzen
        GameController.setzeLEDFarbe(0,color_x)
        GameController.setzeLEDFarbe(1,color_y)
        GameController.setzeLEDFarbe(2,color_z)


    # Eine kurze Pause zwischen den Messungen
    time.sleep(1)