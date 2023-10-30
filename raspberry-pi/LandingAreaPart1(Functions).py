#type: ignore

import board

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