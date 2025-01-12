Human Typing Simulator

A Python script that simulates human-like typing by typing text character by character with realistic delays, random typos, and automatic corrections. Perfect for creating natural typing simulations or automating text input with a human touch.
Features

    Simulates human typing by adding delays between each character.
    Random typos are introduced and corrected automatically.
    Reads text from an external file (output.txt) for flexible content.
    Adjustable parameters for typing speed, random delay variations, and typo frequency.

How It Works

    The script reads text from a file named output.txt.
    It simulates typing each character one by one with a base delay.
    Occasionally, it introduces a random typo (e.g., special characters) and deletes it using a backspace.
    The final output matches the content of output.txt.

Installation for windows 10/11:

    Clone this repository:

git clone https://github.com/yourusername/human-typing-simulator.git

Navigate to the project directory:

cd human-typing-simulator

Install the required dependencies using pip:

    pip install keyboard

Installation for Kali Linux:
    sudo pip3 install pyautogui
     test.py code:
      #!/usr/bin/env python3
      
      import time
      import pyautogui  # Import pyautogui for typing
      import random
      import string
      
      def human_like_typing(text, base_delay=0.1, random_factor=0.05, typo_chance=0.1):
          """
          Simulates human-like typing by typing one character at a time with delays, 
          including occasional random typos that are deleted.
      
          :param text: The text to be typed.
          :param base_delay: The base delay between each character (in seconds).
          :param random_factor: The maximum random variation added to the delay.
          :param typo_chance: The probability of adding a random typo (0 to 1).
          """
          # Filter text to include only printable characters
          text = ''.join(char for char in text if char in string.printable)
      
          for char in text:
              # Simulate a random typo
              if random.random() < typo_chance:
                  typo_char = random.choice("~!@#$%^&*()_+{}:\"<>?|[];',./")  # Random symbol
                  pyautogui.typewrite(typo_char)  # Type the typo
                  time.sleep(base_delay + random.uniform(-random_factor, random_factor))  # Delay for the typo
                  pyautogui.typewrite("\b")  # Simulate backspace
                  time.sleep(base_delay + random.uniform(-random_factor, random_factor))  # Delay after backspace
      
              # Type the correct character
              pyautogui.typewrite(char)
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
      

Usage

    Create or edit a file named output.txt in the same directory as the script. Add the text you want to simulate typing.

    Example output.txt content:

Hello there! This is a demonstration of human-like typing simulation.

Run the script:

    python human_typing_simulator.py

    Watch as the text from output.txt is typed out in a human-like manner.

Customization

You can customize the typing behavior by modifying the parameters in the human_like_typing function:

    base_delay: Base delay between typing each character (default is 0.1 seconds).
    random_factor: Adds random variability to the delay for a more natural feel (default is 0.05 seconds).
    typo_chance: Probability of introducing a random typo (default is 0.1 or 10%).

Example:

human_like_typing(content, base_delay=0.2, random_factor=0.1, typo_chance=0.2)

Example Output

If output.txt contains:

Hello, world!

The script might output this (with simulated delays and corrections):

H
e
l
l
o
,
[typo: #] Backspace
[correction:  ]
w
o
r
l
d
!

Requirements

    Python 3.7 or later
    keyboard module (pip install keyboard)

Disclaimer

This script uses the keyboard module, which requires administrative privileges on some systems to simulate keyboard input. Use responsibly and ensure you have permission to automate typing on your device.
License

This project is licensed under the MIT License. See the LICENSE file for details.
