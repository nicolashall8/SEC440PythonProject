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
    # Prompt the user to enter the full file path
    filepath = input("Please enter the full path to your local file: ")
    
    hasher = hashlib.sha256()
    with open(filepath,"rb") as open_file:
        content = open_file.read()
        hasher.update(content)
    print(hasher.hexdigest())

def md5_hash():
    # Prompt the user to enter the full file path
    filepath = input("Please enter the full path to your local file: ")

    hasher = hashlib.md5()
    with open(filepath,"rb") as open_file:
        content = open_file.read()
        hasher.update(content)
    print(hasher.hexdigest())

while(True):
    hash_menu()
    user_choice = ""
    try:
        user_choice = int(input("Select a menu option: "))
    except:
        print("\nInvalid input. Please enter a number... \n")
    if user_choice == 1:
        sha_hash()
    elif user_choice == 2:
        md5_hash()
    elif user_choice == 3:
        break