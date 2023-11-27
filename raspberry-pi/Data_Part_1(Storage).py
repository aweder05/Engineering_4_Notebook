#type:ignore
import board
import time
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c


Led = digitalio.DigitalInOut(board.GP0) # Set LED pin
Led.direction = digitalio.Direction.OUTPUT # Pin is using output

mpu = adafruit_mpu6050.MPU6050(i2c) # Sets up the MPU

with open("/data.csv", "a") as datalog: #When Data Mode is Active
    while True:
        XAcceleration = mpu.acceleration[0] ## States which value of the Tuple corresponds to which accelerometer value 
        YAcceleration = mpu.acceleration[1] ## For Y
        ZAcceleration = mpu.acceleration[2] ## For Z
        
        time.sleep(.1) ## Adds a slight pause after each cycle 

        if ZAcceleration < 0:
            Led.value = True ## Turns on the Red LED
        else:
            Led.value = False ## Turns off the Red LED when the accelerometer is not tilted to exactly 90 degrees
           
    
        datalog.write(f"{time_elapsed},{Xaccel},{Yaccel},{Zaccel},{Tilted}\n") #Put the data into a chart

        Led.value = True # LED cycle
        time.sleep(.5)
        Led.value = False

        datalog.flush() # Save the data
        time.sleep(.1)
