# type: ignore
import board
import digitalio
led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT 
import time 
led.
 
while True: 
led.value = True 
time.sleep(200)
led.value = False
time.sleep(200)