import hashlib
from time import sleep

def hash_menu():

    hash_options = {
        1: 'SHA-256',
        2: 'MD5',
        3: 'Return to main menu',
    }
    for key in hash_options.keys():
        print(key, '-', hash_options[key])

def sha_hash():
   
    try:
        filepath = input("Please enter the full path to your file: ")
        
        hasher = hashlib.sha256()
        with open(filepath,"rb") as open_file:
            content = open_file.read()
            hasher.update(content)
        sha_output = hasher.hexdigest()
        print("\n" + sha_output)

        # Close the file
        open_file.close()
    
    except:
        print("Error: Could not access file. Please provide the full file path...")

        # Restart function
        sha_hash()

    else:
        exit()

def md5_hash():
    
    try:
        filepath = input("Please enter the full path to your file: ")
        
        hasher = hashlib.md5()
        with open(filepath,"rb") as open_file:
            content = open_file.read()
            hasher.update(content)
        md5_output = hasher.hexdigest()
        print("\n" + md5_output)

        # Close the file
        open_file.close()
    
    except:
        print("Error: Could not access file. Please provide the full file path...")

        # Restart function
        md5_hash()

    else:
        exit()
    

while(True):
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