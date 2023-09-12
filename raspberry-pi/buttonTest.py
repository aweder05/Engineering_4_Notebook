# type: ignore
import board
import time 
import digitalio

buttonPress = digitalio.DigitalInOut(board.GP3)

buttonPress.direction = digitalio.Direction.INPUT

buttonPress.pull = digitalio.Pull.UP

while True: 
    if buttonPress.value == False:
        print("Button Pressed")
    else: 
        print("Button not Pressed")