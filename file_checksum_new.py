from paramiko import SSHClient, AutoAddPolicy
import getpass

def ssh_paramiko():
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

    except:
        # Known_hosts file path provided is invalid
        print("\nError: Could not find known hosts file. Please provide full file path...")  

        # Restart function
        ssh_paramiko()

# Call main function
ssh_paramiko()