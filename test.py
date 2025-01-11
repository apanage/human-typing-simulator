import time
import keyboard
import random

def human_like_typing(text, base_delay=0.1, random_factor=0.05, typo_chance=0.1):
    """
    Simulates human-like typing by typing one character at a time with delays, 
    including occasional random typos that are deleted.

    :param text: The text to be typed.
    :param base_delay: The base delay between each character (in seconds).
    :param random_factor: The maximum random variation added to the delay.
    :param typo_chance: The probability of adding a random typo (0 to 1).
    """
    for char in text:
        # Simulate a random typo
        if random.random() < typo_chance:
            typo_char = random.choice("~!@#$%^&*()_+{}:\"<>?|[];',./")  # Random symbol
            keyboard.write(typo_char)  # Type the typo
            time.sleep(base_delay + random.uniform(-random_factor, random_factor))  # Delay for the typo
            keyboard.write("\b")  # Simulate backspace
            time.sleep(base_delay + random.uniform(-random_factor, random_factor))  # Delay after backspace
        
        # Type the correct character from the file
        keyboard.write(char)
        time.sleep(base_delay + random.uniform(-random_factor, random_factor))  # Delay for each character

def main():
    try:
        print("Preparing to read the file and simulate typing...")
        time.sleep(1.5)  # Delay to simulate preparation
        
        # Open the file with UTF-8 encoding
        with open("output.txt", "r", encoding="utf-8") as file:
            content = file.read()  # Read the entire content of output.txt
            print("Simulating human-like typing from output.txt...")
            time.sleep(2)  # Delay before starting to simulate typing
            human_like_typing(content, base_delay=0.1, random_factor=0.05, typo_chance=0.1)
    except FileNotFoundError:
        print("Error: output.txt file not found. Please create the file and add content to it.")
        time.sleep(1)
    except UnicodeDecodeError:
        print("Error: The file is not encoded in UTF-8. Please save the file with UTF-8 encoding.")
        time.sleep(1)

if __name__ == "__main__":
    main()
