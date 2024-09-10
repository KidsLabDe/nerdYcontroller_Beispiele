import time
import board
import neopixel
import math
import busio

from adafruit_lsm6ds.lsm6ds3 import LSM6DS3

# Erstellen Sie eine I2C-Instanz
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)  # SCL an GP7, SDA an GP6

# Initialisieren Sie den Sensor
sensor = LSM6DS3(i2c)


MAX_SPANNUNG = 3.3

# Farbkonstanten definieren
ROT = (255, 0, 0)
GRÜN = (0, 255, 0)
BLAU = (0, 0, 255)
GELB = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
LILA = (128, 0, 128)
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
ROSA = (255, 192, 203)
BRAUN = (165, 42, 42)

# Anzahl der LEDs und der Pin
num_pixels = 4
pixel_pin = board.GP12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=True)

def set_color(pixel, color):
    pixels[pixel] = color

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def regenbogen(anz_pixel = num_pixels, pause = 0.01):
    for j in range(255):
        for i in range(anz_pixel):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        time.sleep(pause)
        pixels.show()




def neigung_roh():
    """Gibt die x, y, z Werte vom Neigungssensor zurück."""
    accel_x, accel_y, accel_z = sensor.acceleration
    return accel_x, accel_y, accel_z

def neigung_winkel():
    """Gibt die Winkel für x, y, z zurück."""
    accel_x, accel_y, accel_z = neigung_roh()
    angle_x = math.atan2(accel_y, accel_z) * 180 / math.pi
    angle_y = math.atan2(accel_x, accel_z) * 180 / math.pi
    angle_z = math.atan2(accel_x, accel_y) * 180 / math.pi
    return angle_x, angle_y, angle_z

