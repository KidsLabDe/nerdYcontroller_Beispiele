import time
import board
import busio
import math
from adafruit_lsm6ds.lsm6ds3 import LSM6DS3

# Erstellen Sie eine I2C-Instanz
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)  # SCL an GP7, SDA an GP6

# Initialisieren Sie den Sensor
sensor = LSM6DS3(i2c)

while True:
    # Beschleunigungsdaten lesen (x, y, z Achsen in m/s^2)
    accel_x, accel_y, accel_z = sensor.acceleration
    temp = sensor.temperature
    print(f"Beschleunigung: X: {accel_x:.2f} m/s^2, Y: {accel_y:.2f} m/s^2, Z: {accel_z:.2f} m/s^2")

    # Gyroskopdaten lesen (x, y, z Achsen in Grad pro Sekunde)
    gyro_x, gyro_y, gyro_z = sensor.gyro
    print(f"Gyroskop: X: {gyro_x:.2f} dps, Y: {gyro_y:.2f} dps, Z: {gyro_z:.2f} dps")
    
    print(f"Temperatur: {temp:.2f} Grad Celsius")

    # Winkelberechnung
    angle_x = math.atan2(accel_y, accel_z) * 180 / math.pi
    angle_y = math.atan2(accel_x, accel_z) * 180 / math.pi
    angle_z = math.atan2(accel_x, accel_y) * 180 / math.pi

    print(f"Winkel: X: {angle_x:.2f}°, Y: {angle_y:.2f}°, Z: {angle_z:.2f}°")

    # Eine kurze Pause zwischen den Messungen
    time.sleep(1)
