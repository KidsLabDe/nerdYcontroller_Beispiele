import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# Initialize Keyboard
kbd = Keyboard(usb_hid.devices)

# Press and release CapsLock.
while True:
    kbd.press(Keycode.CAPS_LOCK)
    # Check status of the LED_CAPS_LOCK
    print(kbd.led_on(Keyboard.LED_CAPS_LOCK))
    time.sleep(1)
    kbd.release(Keycode.CAPS_LOCK)
    time.sleep(1)
    # Check status of the LED_CAPS_LOCK
    print(kbd.led_on(Keyboard.LED_CAPS_LOCK))
