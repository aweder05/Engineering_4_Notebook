# type: ignore

import board
import adafruit_mpu6050
import busio
import time

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True: 
    XAcceleration = mpu.acceleration[0]
    YAcceleration = mpu.acceleration[1]
    ZAcceleration = mpu.acceleration[2]

    print(f"XAcceleration = {XAcceleration}")
    print(f"YAcceleration = {YAcceleration}")
    print(f"ZAcceleration = {ZAcceleration}")
    print("")
    
    time.sleep(.1)