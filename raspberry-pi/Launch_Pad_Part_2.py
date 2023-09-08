## Note: The following code up until "time.sleep(1)" is from Launch Pad Part 1, the previous assignment 
# type: ignore
import board
import time 
import digitalio

ledGreen = digitalio.DigitalInOut(board.GP0)
ledRed = digitalio.DigitalInOut(board.GP1)

ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

Seconds = 10 ## Sets the amount of time that the code is counting down from 

while True: 
    if Seconds > 0: 
        print("T-Minus", Seconds) ## Prints the amount of seconds remaining
        ledRed.value = True 
        time.sleep(.5)
        ledRed.value = False 
        time.sleep(.5)
        Seconds = Seconds - 1 
    else:
        ledGreen.value = True 
        ledRed.value = False
        print("WE HAVE LIFTOFF") ## Prints liftoff statement once the ticker reaches zero 
        time.sleep(1)
