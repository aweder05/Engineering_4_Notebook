# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Raspberry Pi Assignments](#raspberry_pi_assignments)
    * [Launch Pad Part 1](#launch_pad_part_1)
    * [Launch Pad Part 2](#launch_pad_part_2)
    * [Launch Pad Part 3](#launch_pad_part_3)
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
