## Note: The following code up until "time.sleep(1)" is from Launch Pad Part 1, the previous assignment 
# type: ignore
import board
import time 
import digitalio

buttonPress = digitalio.DigitalInOut(board.GP3)
ledGreen = digitalio.DigitalInOut(board.GP0) ## Sets the pin number for the Green LED
ledRed = digitalio.DigitalInOut(board.GP1) ## Sets the pin number for the Red LED

buttonPress.direction = digitalio.Direction.INPUT
ledGreen.direction = digitalio.Direction.OUTPUT 
ledRed.direction = digitalio.Direction.OUTPUT  

buttonPress.pull = digitalio.Pull.UP

numberPress = 0 ## sets a variable for the number of button presses

Seconds = 10 ## Sets the amount of time that the code is counting down from 

while True: 
    if buttonPress.value == False:
        numberPress = numberPress + 1 ## adds 1 to whenever the button is pressed
    if numberPress > 0: ## if the button has been pressed, then "numberpress" will be >0 
        if Seconds > 0: 
            print("T-Minus", Seconds) ## Prints the amount of seconds remaining
            ledRed.value = True ## Turns on the Red LED 
            time.sleep(.5)
            ledRed.value = False ## Turns off the Red LED for the flashing effect 
            time.sleep(.5) 
            Seconds = Seconds - 1 ## Subracts one second of "Seconds"
        else:
            ledGreen.value = True ## Turns on the Green LED since the timer has reached zero
            ledRed.value = False ## Stops the flashing of the Red LED
            print("WE HAVE LIFTOFF") ## Prints liftoff statement once the ticker reaches zero 
            time.sleep(1) 
