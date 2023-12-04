#type: ignore

## I used large portions of Grant Gastinger's code. Here is a link to their notebook: https://github.com/ggastin30/Engineering_4_Notebook 


import board
import displayio
import busio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import time

displayio.release_displays()

sda_pin = board.GP14 ## States the pin for SDA

scl_pin = board.GP15 ## States the pin for SCL

i2c = busio.I2C(scl_pin, sda_pin) ## States the pins for I2C

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP13) #Connects the OLED to I2C
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) #Define OLED

splash = displayio.Group() # create the display group
display.show(splash)

def TriArea(x1,y1,x2,y2,x3,y3): #Creates a function to find the area
    try: #Find the area if coordinates are valid
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) #Triangle area formula
        return area
    except: #If coordinates are invalid
        print("Invalid Coordinates") #Error message for when the coordinates the user input into the terminal are invalid
        area = 0 
        return area

while True:
    print("Point 1 Coordinates (x,y):") #Print so the perwson running code knows which coordinates
    p1 = input() #Return whatever the user types in
    x1, y1 = p1.split(",") #Turn p1 into two variables separated by a comma
    print(f"Point 1: ({p1})") #Confirm the coordinates

    print("Point 2 Coordinates (x,y):") #Repeat for coordinate 2
    p2 = input() #Sets p2 as the input 
    x2, y2 = p2.split(",") #Turns p1 into two variables separated by a comma
    print(f"Point 2: ({p2})") #Confirms the p2 coordinates

    print("Point 3 Coordinates (x,y):") #Repeat for coordinate 3
    p3 = input() #Returns whatever the user types in for the 2nd coordinates
    x3, y3 = p3.split(",") #Splits p3 into the x3 and y3 coordinates 
    print(f"Point 3: ({p3})") #Confirms the p3 coordinates 

    x1 = float(x1) #Turn varibles from strings into floats so they can be plugged into the function
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    
    area = TriArea(x1,y1,x2,y2,x3,y3) #Plug in floats to find area
    print(" ")
    print(f"AREA IS: {area}") #Prints the Area after all of the inputs and calculations are done
    print(" ") #Adds a blank space to the end of the loop 

    text_area = label.Label(terminalio.FONT, text= f"A= {area}", color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    hline = Line(0,32,128,32, color=0xFFFF00) # Print the X-Axis, by using two coordinates
    splash.append(hline) 

    vline = Line(64,0,64,64, color=0xFFFF00) # Print the Y-Axis, by using two coordinates
    splash.append(vline)

    circle = Circle(64, 32, 2, outline=0xFFFF00) ## These coordinates are able to print a Circle on the OLED, by using a center coordinate and a radius value
    splash.append(circle)
    
    X1 = int(x1 + 64)
    X2 = int(x2 + 64)
    X3 = int(x3 + 64)
    Y1 = int(32 - y1)
    Y2 = int(32 - y2)
    Y3 = int(32 - y3)

    triangle = Triangle(X1, Y1, X2, Y2, X3, Y3, outline=0xFFFF00) # These coordinates print a triangle using three different coordinates, this is what will be used for this assignment. 
    splash.append(triangle)
