# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import touchio
from adafruit_debouncer import Debouncer, Button
import pwmio


import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.GP12

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 4

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


pixels.fill((0, 0, 255))
pixels.show()


# Touch Stuff




THRESHOLD = 1000
t_r = touchio.TouchIn(board.GP16)
t_r.threshold = t_r.raw_value + THRESHOLD
touchpad_r = Button(t_r, value_when_pressed=True)

t_l = touchio.TouchIn(board.GP14)
t_l.threshold = t_l.raw_value + THRESHOLD
touchpad_l = Button(t_l, value_when_pressed=True)


t_u = touchio.TouchIn(board.GP15)
t_u.threshold = t_u.raw_value + THRESHOLD
touchpad_u = Button(t_u, value_when_pressed=True)



t_d = touchio.TouchIn(board.GP17)
t_d.threshold = t_d.raw_value + THRESHOLD
touchpad_d = Button(t_d, value_when_pressed=True)

"""
t_click = touchio.TouchIn(board.GP6)
t_click.threshold = t_click.raw_value + THRESHOLD
touchpad_click = Button(t_click, value_when_pressed=True)


t_space = touchio.TouchIn(board.GP7)
t_space.threshold = t_space.raw_value + THRESHOLD
touchpad_space = Button(t_space, value_when_pressed=True)
"""
# pwm = pwmio.PWMOut(board.GP20, duty_cycle=2 ** 15, variable_frequency=True)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)



while True:
    """
    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((255, 0, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((255, 0, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 255, 0))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 255, 0, 0))
    pixels.show()
    time.sleep(1)

    # Comment this line out if you have RGBW/GRBW NeoPixels
    pixels.fill((0, 0, 255))
    # Uncomment this line if you have RGBW/GRBW NeoPixels
    # pixels.fill((0, 0, 255, 0))
    pixels.show()
    time.sleep(1)

    rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
    """

    """
    time.sleep(0.1)
    pwm.frequency = 0
    time.sleep(0.1)
    pwm.frequency = 0
    time.sleep(0.1)
    """

    touchpad_l.update()
    if touchpad_l.rose:
        # print("Touch On")
        pixels.fill((255, 0, 0))
        pixels.show()
        keyboard.send(Keycode.A)
    """if touchpad_l.fell:
        # print("Touch Off")
        pixels.fill((0, 255, 0))
        pixels.show()
    """
    touchpad_r.update()
    if touchpad_r.rose:
        # print("Touch On")
        pixels.fill((0, 255, 0))
        pixels.show()
        keyboard.send(Keycode.D)

    touchpad_u.update()
    if touchpad_u.rose:
        # print("Touch On")
        pixels.fill((0, 255, 255))
        pixels.show()
        keyboard.send(Keycode.W)


    touchpad_d.update()
    if touchpad_d.rose:
        # print("Touch On")
        rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step
        pixels.fill((255, 255, 0))
        pixels.show()
        keyboard.send(Keycode.S)

"""    touchpad_space.update()
    if touchpad_space.rose:
        # print("Touch On")
        rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

        #pixels.fill((255, 255, 0))
        #ea,opixels.show()
        #keyboard.send(Keycode.S)

    touchpad_click.update()
    if touchpad_click.rose:
        # print("Touch On")
        pixels.fill((255, 255, 0))
        pixels.show()
        #keyboard.send(Keycode.S)
"""
"""

aaaeee,,,ooooooo
"""
