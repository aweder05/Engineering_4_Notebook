# type: ignore

import board
import time
import busio


sda_pin = board.GP4
scl_pin = board.GP5
i2c = busio.I2C(scl_pin, sda_pin)

while not i2c.try_lock():
    pass

try:
    while True:
        print(
            "I2C addresses found:",
            [hex(device_address) for device_address in i2c.scan()],
        )
        time.sleep(2)

finally:  # unlock the i2c bus when ctrl-c'ing out of the loop
    i2c.unlock()

## I2C addresses found: '0x68' is MPU6050
## 0x3d is OLED Screen