# Run Script Example: python3.8 file_integrity_remote_scan.py /home/champuser

import hashlib, os, time, sys, socket
from datetime import date

def remote_file_scan():

    # User provides the filepath to scan as an argument
    filepath = sys.argv

    try:
        scan = os.scandir(sys.argv[1])
    
    # Error when user doesn't provide filepath parameter
    except IndexError: 
        print("Error: Please provide a directory to scan as a parameter. Example: python3.8 file_integrity_remote_scan.py /home/champuser")
        input("\nPress enter to exit and try again... ")
        exit()

    scanlist = []

    for file in scan:
        filename = file.name

        sha = hashlib.sha256()
        try:
            with open(sys.argv[1] + "/" + filename,'rb') as file:
                hash = file.read()
                sha.update(hash)
                filehash = sha.hexdigest()
                scanlist.append("\n" + filename + ", " + filehash)

        except IsADirectoryError:
            continue

        # Close file
        file.close()
    
    # Obtains current date for scan output file naming scheme
    mydate = str(date.today())

    # Obtains hostname of the remote endpoint to include in scan ouput file
    hostname = socket.gethostname()

    # Creates output file with scan results
    print("[*] Creating new remote scan file...")
    time.sleep(2)
    databasefile = open(mydate + "-remote-scan" + ".txt", "w+")

    # Writes the hostname and filepath onto the first two lines of file for labeling purposes
    databasefile.writelines(hostname)
    databasefile.writelines("\n" + sys.argv[1])

    for i in scanlist:
        databasefile.writelines([i])
    databasefile.close()


# Need to add function for comparing new scan file with a basleine file



# Start remote file scan
remote_file_scan()
