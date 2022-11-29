from paramiko import *
import paramiko
import getpass
import hashlib
import os
import pyfiglet
from datetime import date
import time


def menu():          

    # Format ASCII art
    art = pyfiglet.Figlet(font='slant')          
    print(art.renderText("File Integrity Scanner"))

    menu_options = {
        1: 'New File Integrity Scan',
        2: 'File Integrity Check',
        3: 'SSH',
        4: 'Help',
        5: 'Exit Program',
    }
    for key in menu_options.keys():
        print(key, '-', menu_options[key])


def file_scan():
    filepath = input("Please enter the directory to scan: ")

    scan = os.scandir(filepath)
    scanlist = []

    for file in scan:
        filename = file.name

        sha = hashlib.sha256()

        with open(filepath + "/" + filename,'rb') as file:
            hash = file.read()
            sha.update(hash)
            filehash = sha.hexdigest()
            scanlist.append("\n" + filename + " - " + filehash)
            
        # Close file
        file.close()
    
    # Testing to see if hashes from all files in the directory are put into scanlist
    print(scanlist)
    
    filetype = input("Would you like to make this scan the baseline? Type yes or no: ")
    filetype.lower()

    # Obtains current date for file name scheme
    mydate = str(date.today())

    # If user enters yes, the baseline file is created in the current directory. Need to add option to choose directory to save to
    if filetype == "yes":
        print("[*] Creating new baseline file...")
        time.sleep(2)
        databasefile = open(mydate + "-baseline-scan" + ".txt", "w+")
        for i in scanlist:
            databasefile.writelines([i])
        databasefile.close()

    # If user enters no, a scan file is created in the current directory. Need to add option to choose directory to save file to
    elif filetype == "no":
        print("[*] Creating new scan file...")
        time.sleep(2)
        databasefile = open(mydate + "-scan" + ".txt", "w+")
        for i in scanlist:
            databasefile.writelines([i])
        databasefile.close()
    
    # If user enters invalid option (example: integer)
    else:
        input("Error: Invalid input. Please type yes or no.\n\nPress Enter to return to the main menu.")


def file_integrity_check():
    """
    Compares the hashes in the new scan file with the baseline file. Provides output on whether they're the same or changes
    that were made to specific file(s).
    """
    print("")


def ssh_paramiko():
    """
    Provides the user with an interactive commandline via SSH on the remote endpoint
    """

    # User provides full file path to known hosts file
    try:
        key_path = input("Please enter the full path to your SSH known hosts file: ")
        
        # Launch SSH Client
        client = SSHClient()
        
        # Attempts to use the file path provided by the user
        client.load_host_keys(key_path)
        client.load_system_host_keys
        client.set_missing_host_key_policy(AutoAddPolicy())

        ip = input("Please enter the IPv4 address of the endpoint: ")
        username = input("Please enter the username for the endpoint: ")

        # User prompted to securely enter the password for the endpoint account
        password = getpass.getpass()

        # Connect to the endpoint using user provided variables
        client.connect(ip, username=username, password=password)

        # Command line loop
        while True:
            try:
                cmdline = input("-> ")
                if cmdline == "exit": break
                stdin, stdout, stderr = client.exec_command(cmdline)
                print(stdout.read().decode())

            except KeyboardInterrupt:
                break
        
        # Close out SSH session
        stdin.close()
        stdout.close()
        stderr.close()
        client.close()

    except FileNotFoundError:
        # Path to known_hosts file is invalid
        print("\nError: Could not find known hosts file. Please provide full file path...")  

        # Restart function
        ssh_paramiko()
    
    except paramiko.AuthenticationException as error:
        print("\nError: Authentication failure. Please double check that the credentials are correct.")

        ssh_paramiko()


def help_info():
    """
    Information about the program. Below are placeholders/examples.
    """

    print("\nThe first option is to do a file scan of a desired directory on a remote endpoint. ")
    print("\nMake sure the endpoint is accessible via SSH. ")
    print("\nThe scan will collect a baseline of file hashes and save that baseline to a database file. ")
    print("\nThe first option is to do a file scan of a desired directory on a remote endpoint. ")


while(True):
    menu()
    user_choice = ""
    try:
        user_choice = int(input("Select a menu option: "))
    except:
        print("\nInvalid input. Please enter a number... \n")
    else:
        if user_choice == 1:
            file_scan()
        elif user_choice == 2:
            file_integrity_check()
        elif user_choice == 3:
            ssh_paramiko()
        elif user_choice == 4:
            help_info()
        elif user_choice == 5:
            exit()