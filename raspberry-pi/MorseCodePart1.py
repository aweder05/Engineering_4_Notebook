#type: ignore
import board

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
    print("")