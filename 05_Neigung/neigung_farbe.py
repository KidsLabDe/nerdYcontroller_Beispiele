import time
import board
import busio
import math
import neopixel
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3

# Erstellen Sie eine I2C-Instanz
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)  # SCL an GP7, SDA an GP6

# Initialisieren Sie den Sensor
sensor = LSM6DS3(i2c)

# Initialisieren Sie die Neopixel-LEDs
pixel_pin = board.GP12  # Pin für die Neopixel
num_pixels = 8  # Anzahl der LEDs
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def angle_to_color(angle):
    """Konvertiert einen Winkel in eine Farbe."""
    # Normiere den Winkel auf den Bereich 0-360
    angle = angle % 360
    # Konvertiere den Winkel in eine RGB-Farbe
    if angle < 120:
        return (int(255 * (120 - angle) / 120), int(255 * angle / 120), 0)
    elif angle < 240:
        angle -= 120
        return (0, int(255 * (120 - angle) / 120), int(255 * angle / 120))
    else:
        angle -= 240
        return (int(255 * angle / 120), 0, int(255 * (120 - angle) / 120))

while True:
    # Beschleunigungsdaten lesen (x, y, z Achsen in m/s^2)
    accel_x, accel_y, accel_z = sensor.acceleration
    temp = sensor.temperature
    #print(f"Beschleunigung: X: {accel_x:.2f} m/s^2, Y: {accel_y:.2f} m/s^2, Z: {accel_z:.2f} m/s^2")

    # Gyroskopdaten lesen (x, y, z Achsen in Grad pro Sekunde)
    gyro_x, gyro_y, gyro_z = sensor.gyro
    #print(f"Gyroskop: X: {gyro_x:.2f} dps, Y: {gyro_y:.2f} dps, Z: {gyro_z:.2f} dps")
    
    #print(f"Temperatur: {temp:.2f} Grad Celsius")

    # Winkelberechnung
    angle_x = math.atan2(accel_y, accel_z) * 180 / math.pi
    angle_y = math.atan2(accel_x, accel_z) * 180 / math.pi
    angle_z = math.atan2(accel_x, accel_y) * 180 / math.pi

    print(f"Winkel: X: {angle_x:.2f}°, Y: {angle_y:.2f}°, Z: {angle_z:.2f}°")

    # Farbe basierend auf den Winkeln berechnen
    color_x = angle_to_color(angle_x)
    color_y = angle_to_color(angle_y)
    color_z = angle_to_color(angle_z)

    # LEDs entsprechend der berechneten Farben setzen
    pixels[0] = color_x
    pixels[1] = color_y
    pixels[2] = color_z
    pixels.show()

    # Eine kurze Pause zwischen den Messungen
    time.sleep(0.1)