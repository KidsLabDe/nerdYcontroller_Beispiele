import time
import board
import pwmio
import touchio
import GameController
import adafruit_hcsr04

abstand = adafruit_hcsr04.HCSR04(trigger_pin=board.GP1, echo_pin=board.GP0)

from adafruit_motor import servo

# Initialisieren Sie PWM für den Servo-Motor am Pin GP11
# Achtung - u.u. hast du deinen Servo auch an GP10 angeschlossen?
pwm = pwmio.PWMOut(board.GP11, duty_cycle=0, frequency=50)

# Initialisieren Sie den Servo-Motor
mein_servo = servo.Servo(pwm)

def play_gameOver():
    
    GameController.spiele_ton(659,0.3)
    time.sleep(0.2)
    GameController.spiele_ton(659,0.3)
    time.sleep(0.2)
    GameController.spiele_ton(659,0.3)
    time.sleep(0.2)
    GameController.spiele_ton(523,1)

while True:

    # das modell zum drucken findest du hier:
    # https://www.thingiverse.com/thing:3394154 
    # fahre den servo nach ganz unten:
    mein_servo.angle = 180
    
    # über die neigung schauen wir, ab der eimer geleer wird.
    # Wenn ja - dann aufmachen.
    print(f"Neigung:{GameController.neigung()}")
    # wenn er gedreht wird, lassen wir so lange offen:
    while (GameController.neigung()[1] < 0): 
        mein_servo.angle = 45
        print(f"bitte leeren:{GameController.neigung()}")
        time.sleep(5)

        
    
    # jetzt wird der Hunder gestillt:
    # wenn etwas näher als 5 cm ist, dann mampfi mampfi:
    try:
        print(abstand.distance)
        if abstand.distance < 5:
            play_gameOver() 			# Melodie & kurz warten... 2 sek
            mein_servo.angle = 45		# 45 Grad - das ist ganz oben
            time.sleep(0.5)				# halbe sekunde warten...
            mein_servo.angle = 180		# und dann wieder runter.
            time.sleep(2)				# achtung: 2 sek warten vor der nächsten messung, sonst lösst es gleich wieder aus 

    except RuntimeError:
        print("absands-senser Nicht angeschlossen!")
        pass
    time.sleep(0.1)
    
    

