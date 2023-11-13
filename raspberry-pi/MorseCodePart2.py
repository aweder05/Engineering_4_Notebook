#type: ignore
import board
import digitalio
import time 

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

# The Morse code timing rules we will use for signaling are: 
# a dot (.) lasts for 1/4 second. a dash (-) lasts for 3/4 seconds. 
# the space between dots and dashes that are part of the same letter is 1/4 second.
# space between letters is 3/4 seconds
# space between words is 1+3/4 seconds

modifier = 0.25
dot_time = 0.25
dash_time = 0.75
between_taps = 0.25
between_letters = 0.75
between_words = 1.75

RedLed = digitalio.DigitalInOut(board.GP0) # Sets the pin of the red LED
RedLed.direction = digitalio.Direction.OUTPUT
translated_string = ""
while True:
    print("Enter your Morse Code Message Here, or enter -q to quit:")
    original_text = input() ##This prints back what the user typed into the serial monitor
    if original_text == "-q": ##Checks to see if the user has quit, (typed "-q")
        print("Quit") ##Indicates in the Serial Monitory for the user to see that they have quit 
        break ##Then ends the code after the user has quit 
    else: ##If the user inputs anything other than the quit message, then it will be translated into morse code 
        uppercase_text = original_text.upper()
        for letter in uppercase_text: ##Goes through each inputted letter, and then subsequently translates to morse code 
            print(MORSE_CODE[f"{letter}"], end=" ") ##Prints each letter the user has input into morse code
            translated_string = translated_string + " " + MORSE_CODE[f"{letter}"]
        for character in translated_string: 
            if character == '.':
                RedLed.value = True 
                time.sleep(dot_time) 
            if character == '_':
                RedLed.value = True
                time.sleep(dash_time)
            elif character == " ": 
                RedLed.value = False 
                time.sleep(between_letters)
            elif character == "/":
                RedLed.value = False 
                time.sleep(between_words)
            RedLed.value = False 
            time.sleep(between_taps)
            

##    print("")

##    print(translated_string)