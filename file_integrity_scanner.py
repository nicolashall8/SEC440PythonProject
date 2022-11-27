from paramiko import *
import paramiko
import getpass
import hashlib
import os
import pyfiglet


def menu():          

    # Format ASCII art
    art = pyfiglet.Figlet(font='banner3-D')          
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
    baselinelist = []

    for file in scan:
        filename = file.name

        sha = hashlib.sha256()

        with open(filepath + "/" + filename,'rb') as file:
            hash = file.read()
            sha.update(hash)
            baseline = sha.hexdigest()
            baselinelist.append(baseline)

        # Close file
        file.close()
    
    # Testing to see if hashes from all files in the directory are put into baselinelist
    print(baselinelist)
    
    # Creates local file with the hashes from the baselinelist. Need to work on putting each hash on a separate line.
    # Will need to ask the user if they want to make a new baseline file. Otherwise a "new scan" file with the date and time should be created instead.
    databasefile = open("filedatabase.txt", "w+")
    for i in baselinelist:
        databasefile.writelines([i])
    databasefile.close()


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