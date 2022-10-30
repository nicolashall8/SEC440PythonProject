from paramiko import SSHClient, AutoAddPolicy
import getpass

# Ask user for the file path to their known_hosts file
key_path = input("Please enter the full path to your SSH known hosts file: ")

client = SSHClient()

# Uses the file path provided by the user
client.load_host_keys(key_path)
client.load_system_host_keys
client.set_missing_host_key_policy(AutoAddPolicy())


ip = input("Please enter the IPv4 address of the endpoint: ")
username = input("Please enter the username for the endpoint: ")

# User prompted to securely enter the password for the endpoint account
password = getpass.getpass()

# SSH connection is made using the variables provided by the user
client.connect(ip, username=username, password=password)

# User can run a custom command on the endpoint
command = input("Please enter a command to execute on the endpoint: ")
stdin, stdout, stderr = client.exec_command(command)

# Prints out the raw paramiko output of the command
"""
print(type(stdin))
print(type(stdout))
print(type(stderr))
"""

# Decodes the paramiko output of the command
print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

# Prints the return code from the command
return_code = (f'Return code: {stdout.channel.recv_exit_status()}')

"""
if return_code != 0:
    print("The command you provided is invalid. Check the syntax.")
"""

stdin.close()
stdout.close()
stderr.close()

# Close the SSH session 
client.close()