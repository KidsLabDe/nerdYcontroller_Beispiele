import time
import board
import digitalio

# Pins für den Drehencoder definieren
dt_pin = board.GP2
clk_pin = board.GP1

# Pins initialisieren
dt = digitalio.DigitalInOut(dt_pin)
dt.direction = digitalio.Direction.INPUT
clk = digitalio.DigitalInOut(clk_pin)
clk.direction = digitalio.Direction.INPUT

# Variablen zur Verfolgung des Zustands
last_clk = clk.value
counter = 0

while True:
    current_clk = clk.value
    if current_clk != last_clk:
        if dt.value != current_clk:
            counter += 1
        else:
            counter -= 1
        print("Counter:", counter)
    last_clk = current_clk
    time.sleep(0.01)