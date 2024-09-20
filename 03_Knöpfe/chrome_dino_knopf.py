import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import GameController     

# Mit diesem Beispiel kannst du ein einfaches 1 Tasten Spiel 
# wie der Chrome-Dino gespielt werden.
# Schließe den Knopf an den Pin GP4 an - die andere Seite des Knopfes auf GND.

# Der Knopf schließt einen Stromkreis: wenn du ihn drückst, fließt der Strom und das kann der Pico messen.

# Knopf initialisieren - wir sagen hier, wo er angeschlossen ist
knopf = digitalio.DigitalInOut(board.GP4)
knopf.direction = digitalio.Direction.INPUT
knopf.pull = digitalio.Pull.UP 
# PullUps oder PullDowns sind etwas komplizierter - aber wichtig. 
# Wenn der Knopf nicht gedrückt ist, hängt der Anschluss ja "in der Luft" 
# Und da kommen dann komische Sachen raus. Mit dem Pull-Widerständen kann man das verhindern.
# PullUp benuzt man, wenn der Schalter auf der anderen Seite an Masse / GND / Minus hängtp
# PullDown betnuzt man, wenn auf der anderen Seite + / 3.3V sind.



# Initialisieren Sie die Tastatur
tastatur = Keyboard(usb_hid.devices)


print("chrome://dino/")

GameController.setzeAlleAus()

while True:
    if not knopf.value :
        GameController.setzeAlleFarbe(GameController.ROT)
        # Wenn der Knopf gedrückt wird und vorher nicht gedrückt war
        GameController.drueckeTaste(Keycode.SPACE,0.2)
        print("SPACE gedrückt")
        GameController.setzeAlleAus()
    
    time.sleep(0.05)
