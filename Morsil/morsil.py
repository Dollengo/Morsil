import time
import os

# Function to clear the console screen
def clear_console():
    # Check the operating system to determine the appropriate command to clear the console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Other systems (Linux, MacOS)
        os.system('clear')

# Simulates a loading process with delays
def loading():
    time.sleep(1)
    print("system:Loading information...")  # Message indicating loading of information
    time.sleep(1)
    print("system:Importing data...")  # Message indicating importing of data
    time.sleep(2)
    print("system:Decrypting information...")  # Message indicating decryption of information
    time.sleep(0.5)
    print("system:Completed!")  # Message indicating completion of loading process
    time.sleep(0.1)

# Dictionary to convert ASCII characters to Morse code
codes = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", "0": "-----", " ": "/", ".": ".-.-.-", "?": "..--..",
    "!": "-.-.--", ",": "--..--", "=": "-...-", "/": "-..-.", "-": "-....-",
    "+": ".-.-.", ":": "---...", ";": "-.-.-.", "'": ".----.", "(": "-.--.",
    ")": "-.--.-", "&": ".-..."
}

# Dictionary of error messages
errors = {
    "001": "Unknown error",
    "002": "Network error",
    "003": "Compiler error",
    "004": "Syntax error",
    "005": "Runtime error",
    "006": "Memory error",
    "007": "Hardware error",
    "008": "Software error",
    "009": "Python language error",
    "010": "IDE/Code editor error (not expected to occur in .exe)",
    "011": "Code error",
    "012": "Input typing error",
    "013": "Input key error",
    "014": "Input reading error",
    "015": "Data loading error",
    "016": "Unrecognized characters"
}

# Invert the dictionary to get Morse to ASCII mapping
codes_reversed = {value: key for key, value in codes.items()}

# Run the clear console command
clear_console()
# Run the loading simulation
loading()

print("Morsil: Hello, I'm Morsil, a robot FLUENT in Morse code.")

# Prompt the user to choose the conversion direction
chose = input("Morsil: Type '1' for (morse -> ascii), '2' for (ascii -> morse) or 'esc' for exit: ").lower()

if chose == '1':
    # Morse to ASCII conversion
    morse = input("Morsil: Type the Morse code to be converted (separate each letter with a space): ")
    ascii = ''.join(codes_reversed[i] for i in morse.split(' '))
    print(f"Morsil: {ascii}")
elif chose == '2':
    # ASCII to Morse conversion
    ascii = input("Morsil: Type the text to be converted: ").lower()
    morse = ' '.join(codes[i] for i in ascii)
    print(f"Morsil: {morse}")
elif chose == "errors":
    # Display the list of error messages
    print(errors)
elif chose == "esc": 
    # Exit the program
    print("Morsil: Bye...")
    exit()
else:
    # Display an error message if the input is invalid
    print("system:error 012,014\nType 'errors' for more information.")
