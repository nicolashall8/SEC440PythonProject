import os
import pyfiglet
import time
import hashlib

def menu():
    
    # Text for ASCII art
    text = "Cyber Tools"           

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
        print("")
    elif user_choice == 2:
        def hash_menu():

            hash_options = {
            1: 'SHA-256',
            2: 'MD5',
            3: 'Exit Program',
        }
            for key in hash_options.keys():
                print(key, '-', hash_options[key])


        def sha_hash():

            try:
                filepath = input("Please enter the full path to your file: ")
                verified_sha = input("\nPlease paste the verified hash included on the website of the downloaded file: ").lower()

                hasher = hashlib.sha256()
                with open(filepath, "rb") as open_file:
                    content = open_file.read()
                    hasher.update(content)
                sha_output = hasher.hexdigest()
                print("\nThe hash of the provided file is: " + sha_output.lower())

                if verified_sha == sha_output:
                    print("\nCongratulations, the hash of the file is legitimate.\n")
                else:
                    print("\nThe hash of the file is not legitimate. Please take the necessary steps to dispose of this file as it may be malicious.\n")

                # Close the file
                open_file.close()

                # Return to main menu
                time.sleep(2)
                print("Returning to main menu...")
                time.sleep(2)
                hash_menu()

            except:
                print("Error: Could not access file. Please provide the full file path...")

                # Restart function
                sha_hash()
            
            else:
                exit()

        def md5_hash():

            try:
                filepath = input("Please enter the full path to your file: ")
                verified_md5 = input("\nPlease paste the verified hash included on the website of the downloaded file: ").lower()

                hasher = hashlib.md5()
                with open(filepath, "rb") as open_file:
                    content = open_file.read()
                    hasher.update(content)
                md5_output = hasher.hexdigest()
                print("\nThe hash of the provided file is: " + md5_output.lower())

                if verified_md5 == md5_output:
                    print("\nCongratulations, the hash of the file is legitimate.")
                else:
                    print("\nThe hash of the file is not legitimate. Please take the necessary steps to dispose of this file as it may be malicious. ")

                # Close the file
                open_file.close()

                # Return to main menu
                time.sleep(2)
                print("Returning to main menu...")
                time.sleep(2)
                hash_menu()

            except:
                print("Error: Could not access file. Please provide the full file path...")

                # Restart function
                md5_hash()

            else:
                exit()


        while (True):
            hash_menu()
            user_choice = ""
            try:
                user_choice = int(input("Select a menu option: "))
            except:
                print("\nInvalid input. Please enter a number... \n")
            else:
                if user_choice == 1:
                    sha_hash()
                elif user_choice == 2:
                    md5_hash()
                elif user_choice == 3:
                    break
    elif user_choice == 3:
        print("")
    elif user_choice == 4:
        print("")
    elif user_choice == 5:
        exit()