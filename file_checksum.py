import hashlib

def sha_hash():
    # Prompt the user to enter the full file path
    filepath = input("Please enter the full path to your file: ")
    
    hasher = hashlib.sha256()
    with open(filepath,"rb") as open_file:
        content = open_file.read()
        hasher.update(content)
    print(hasher.hexdigest())

def md5_hash():
    # Prompt the user to enter the full file path
    filepath = input("Please enter the full path to your file: ")

    hasher = hashlib.md5()
    with open(filepath,"rb") as open_file:
        content = open_file.read()
        hasher.update(content)
    print(hasher.hexdigest())


md5_hash()