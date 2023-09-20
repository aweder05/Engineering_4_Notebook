# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry Pi Assignments](#raspberry_pi_assignments)
    * [Launch Pad Part 1](#launch_pad_part_1)
    * [Launch Pad Part 2](#launch_pad_part_2)
    * [Launch Pad Part 3](#launch_pad_part_3)
    * [Launch Pad Part 4](#launch_pad_part_4)
    * [Crash Avoidance Part 1](#crash_avoidance_part_1)
    * [Crash Avoidance Part 2](#crash_avoidance_part_2)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## **Raspberry_Pi_Assignments**

## Launch_Pad_Part_1

### Assignment Description

In Launch Pad Part 1, the goal is to countdown from 10 seconds down to Liftoff (at 0 seconds). That countdown must be printed to the serial monitor

### Evidence 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart1gif.gif?raw=true" width="400">

##### In the above video, the serial monitor can be seen printing T-Minus, and then the countdown from ten seconds to liftoff. 

### Wiring

The wiring for this assignment was very simple. The PicoW board was simply plugged into the COM11 port on my computer. 

### Code

Her is a link to the **commented code** for this assignment: [Click Here](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Lauch_Pad_Part_1.py)

### Reflection

This assignment was pretty straightforward. I got some help from classmates in re-learning the syntax for VS Code. Other than that, I had little no issues with my code, other than sometimes having to google certain ways of formatting code, such as time.sleep of print.("What is being printed"). There were some struggles sometimes with having to connect to the PicoW board from VS Code, but these issues can be solved with a variety of solutions. (Unplugging, Running through code.py, etc.)

&nbsp;

----

## Launch_Pad_Part_2

### Description

The goal for this assignment is to: 

a) Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.

b) Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.

### Evidence 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart2gif.gif?raw=true" width="400">

##### In the above video, the serial monitor can be seen counting down from 10, with the red LED blinking for each second, and the green LED staying stagnant once the timer reaches zero, or "liftoff".

### Wiring 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart2wiringdiagram.png?raw=true" width="400">

### Code 

Here is a link to the commented code for this assignment: [click here](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Launch_Pad_Part_2.py)

### Reflection 

This assignment was relatively straightforward, since I already had the outline from the previous assignment. The only thing that I really had to do was integrate a Red and Green LED into the timing, and wire it all up. At first I was a little confused on how to make the Red LED flash while still counting down, but then I realized for every second that passes, I could just have the Red LED on for half a second, and off for half a second. This worked out perfectly, and I completed the rest of the assignment with little to no issues. 

&nbsp;

----

## Launch_Pad_Part_3

### Description 

The criteria for the following assignment is as follows: 
* Countdown from 10 seconds to 0 (liftoff). 
* Print that countdown to the serial monitor.
* Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.
* (New) **Include a physical button that starts the countdown.**

### Evidence 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart3gif.gif?raw=true" width=400>

##### The button is pressed once briefly, and then the countdown begins. 

### Wiring 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart3wiringdiagram.png?raw=true" width="400">

### Code 

Here is a link for the **commented code** : [link](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Launch_Pad_Part_3.py)

### Reflection

This assignment was also relatively straighforward, as all I essentially had to do was add a button. The tricky part was learning all the new wiring and syntax for the button on the new PicoW board. In the end, my button had to pressed down for the duration of the countdown, which wasnt what I wanted. To fix this, I created a variable that went up each time the button was pressed, and if the variable >0, then the countdown would run. 

&nbsp;

---- 

## Launch_Pad_Part_4

### Description

For this assignment, the objective was to complete the following: 
* Countdown from 10 seconds to 0 (liftoff). Print that countdown to the serial monitor.
* Blink a red light each second of the countdown, and turn on a green LED to signify liftoff.
* Include a physical button that starts the countdown. 
* Actuate a 180 degree servo on liftoff to simulate the launch tower disconnecting.

### Evidence 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart4gif.gif?raw=true" width="400">

##### The above video is similar to the video from Launch Pad Part 3, although now a Servo spins 180 degrees at liftoff, before pausing, and then returning to 0 degrees. 

### Wiring 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/launchpadpart4wiringdiagram.png?raw=true" width="400">

### Code 

Here is a link to the **commented** code for this assignment: [click here](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Launch_Pad_Part_4.py)

### Reflection

This assignment was more difficult than all of the other ones, since I had to basically revamp my code to work with the servo. At first, when I tried integrating the servo into my old code, the servo would always buzz at liftoff, and I couldn't figure out a way to stop the buzzing, or at least prevent it from buzzing indefinitely. Eventually, with help from Vinnie Jones, I changed my seconds variable to a ``for x in range `` line. This ended up working much better because I was able to chronologically count down from 10, then have the servo spin, then wait, and then have it return back to 0. This is because I scrapped the ``else`` line, which confused me anyway. 

## Crash_Avoidance_Part_1

### Description

The module must have an accelerometer that continuously reports x, y, and z acceleration values on the serial monitor.

### Evidence

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/ezgif.com-video-to-gif.gif?raw=true" width="400">

### Wiring 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/crashavoidancepart1wiringdiagram.png?raw=true" height="400">

### Code

Here is a link to the **commented** code for this assignment: [click here](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Part_1.py)

### Reflection 

This assignment was pretty straightforward, except for the new  syntax that I had to learn for this specific sensor. Other than that, It was essentially the same principle as printing values from an HC-SR04 sensor onto the serial monitor. The way that the brackets were set up within the code to print the respectful values. It was interesting to learn how tuples worked, and how to integrate them into my code. Credit goes to Grant Gastinger for explaining how they work to me. 

&nbsp;

---- 

## Crash_Avoidance_Part_2

### Description

The objective of this assignment was as follows: 
* The module must have an accelerometer that continuously reports x, y, and z acceleration values.
* The module must have an LED that turns on if the helicopter is tilted to 90 degrees. 
* The module must be powered by a mobile power source. 

### Evidence 

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/crashavoidancepart2gif.gif?raw=true" width="400">

##### Here you can see myself holding up my contraption, tilting it to 90 degrees on each side, with the red indicator led light turning on once my accelerometer is tilted 90 degrees. 

### Wiring

<img src="https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/crashavoidancepart2wiringdiagram.png?raw=true" height="300">

### Code 

Here is a link to my commented code for this assignment: [click here](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/Crash_Avoidance_Part_2.py)

### Reflection

Even though this assignment only added about 4 lines of code, It was tricky to figure out how acceleration worked so I could find the value at which to turn on my Red Led. Other than that, I came across my usual incompetence at using the proper syntax for the simplest lines, especially colons after ```if else``` statements. At first I thought wiring up a battery to turn my PicoW mobile would be difficult, but it was really just a matter of plugging in two wires and a battery. 

&nbsp;

----

## **Onshape_Assignment_Template**

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

**Test Link**

[Hyperlink to test.py](https://github.com/aweder05/Engineering_4_Notebook/blob/main/raspberry-pi/test.py)

**Test Image**

![Scary Bilbo Baggins](https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/scary-bilbo-baggins.jpg?raw=true)

**Test Gif**

![Jar Jar Binks](https://github.com/aweder05/Engineering_4_Notebook/blob/main/images/star-wars-jar-jar-binks.gif?raw=true)

----

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

### Test Image

### Test GIF
