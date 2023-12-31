# type: ignore
import pwmio 
from adafruit_motor import servo
import board
import time 
import digitalio

pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50) 
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

buttonPress = digitalio.DigitalInOut(board.GP3) ## Sets the pin for the push button 
ledGreen = digitalio.DigitalInOut(board.GP0) ## Sets the pin number for the Green LED
ledRed = digitalio.DigitalInOut(board.GP1) ## Sets the pin number for the Red LED

buttonPress.direction = digitalio.Direction.INPUT
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

buttonPress.pull = digitalio.Pull.UP

numberPress = 0 ## sets a variable for the number of button presses

Seconds = 10 ## Sets the amount of time that the code is counting down from 

liftoff = False

while True: 
    if buttonPress.value == False:
        for x in range(10,0,-1): ## Uses intervals from 10 counting down to 0 with an interval of -1, counting down 
            print(x) ## Prints the amount of seconds remaining
            ledRed.value = True ## Turns on the Red LED 
            time.sleep(.5)
            ledRed.value = False ## Turns off the Red LED for the flashing effect 
            time.sleep(.5) 
            Seconds = Seconds - 1 ## Subracts one second of "Seconds"

        servo1.angle = 180 ## Turns the servo to 180 
        ledGreen.value = True ## Turns on the Green LED since the timer has reached zero
        ledRed.value = False ## Stops the flashing of the Red LED
        print("WE HAVE LIFTOFF") ## Prints liftoff statement once the ticker reaches zero 
        time.sleep(3) 
        ledGreen.value = False ## Turns of the Liftoff LED after 3 seconds
        servo1.angle = 0  ## Turns the servo back to 0 degrees
