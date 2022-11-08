import os
import pyfiglet
from time import sleep
# from file_checksum import *
# from paramiko_ssh import ssh

def menu():
    
    # Text for ASCII art
    text = "Cyber Toolkit"           

    # Format ASCII art
    ascii_art = pyfiglet.figlet_format(text,font='5lineoblique',width=100)           
    print(ascii_art)

    # Main menu dictionary
    menu_options = {
        1: 'SSH',
        2: 'Verify File Checksum',
        3: 'NMAP Scan',
        4: 'Help',
        5: 'Exit',
    }
    for key in menu_options.keys():
        print(key, '-', menu_options[key])

# Loop to take in user input for main menu
while(True):
    menu()
    user_choice = ""
    try:
        user_choice = int(input("Select a menu option: "))
    except:
        print("\nInvalid input. Please enter a number... \n")
    if user_choice == 1:
        # ssh()
        print("")
    elif user_choice == 2:
        # Run the menu from file_checksum.py
        # hash_menu()
        print("")
    elif user_choice == 3:
        print("")
    elif user_choice == 4:
        print("")
    elif user_choice == 5:
        exit()