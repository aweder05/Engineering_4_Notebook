# type: ignore
import board
import time 
Seconds = 10 ## Sets the amount of time that the code is counting down from 

while True: 
    if Seconds > 0: 
        print("T-Minus", Seconds) ## Prints the amount of seconds remaining
        time.sleep(1)  ## Subracts 1 from "Seconds" each time one second passes
        Seconds = Seconds - 1 
    else:
        print("WE HAVE LIFTOFF") ## Prints liftoff statement once the ticker reaches zero 
        time.sleep(1)
