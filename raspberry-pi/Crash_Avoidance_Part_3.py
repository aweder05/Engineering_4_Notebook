# type: ignore
## I2C addresses found: '0x68' is MPU6050
## 0x3d is OLED Screen

import terminalio
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
import digitalio
import board
import adafruit_mpu6050 
import busio
import time

displayio.release_displays()

sda_pin = board.GP14 ## States the pin for SDA
scl_pin = board.GP15 ## States the pin for SCL

i2c = busio.I2C(scl_pin, sda_pin) ## States the pins for I2C

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)



ledRed = digitalio.DigitalInOut(board.GP1) ## Sets the pin number for the Red LED
ledRed.direction = digitalio.Direction.OUTPUT  

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

splash = displayio.Group()
title = "ANGULAR VELOCITY"
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    
display.show(splash)


while True: 
    XAcceleration = mpu.acceleration[0] ## States which value of the Tuple corresponds to which accelerometer value 
    YAcceleration = mpu.acceleration[1] ## For Y
    ZAcceleration = mpu.acceleration[2] ## For Z

    print(f"XAcceleration = {XAcceleration}") ## Prints the X Accel Value 
    print(f"YAcceleration = {YAcceleration}") ## Prints the Y Accel Value 
    print(f"ZAcceleration = {ZAcceleration}") ## Prints the Z Accel Value 
    print("") ## Adds a space between each reading 
    
    time.sleep(.1) ## Adds a slight pause after each cycle 

    if ZAcceleration < 0:
        ledRed.value = True ## Turns on the Red LED
    else:
        ledRed.value = False ## Turns off the Red LED when the accelerometer is not tilted to exactly 90 degrees
    
    text_area.text = f"Rotation: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}"



