import os
import shutil
from utils import log_action, validate_directory_path
from basic_mode import change_directory, list_dictionary_contents

def elevated_mode():
    """
    Runs the eleavted mode and has a menu
    """
    while True: # menu for elevated mode
        print("\nBasic Mode Menu:")
        print("1. Change Directory")
        print("2. List Directory Contents")
        print("3. Copy File/Directory")
        print("4. Exit")

        choice = input("Enter Choice: ")
        if choice == '1':
            change_directory()
        elif choice == '2':
            list_dictionary_contents()
        elif choice == '3':
            copy_file_or_directory()
        elif choice == '4':
            break
        else:
            print("Invalid")

def copy_file_or_directory():
    """
    Copies a file or directory with a source and destination 
    """
    source = input("Enter source path: ") # source and destination 
    destination = input(" Enter the destination path: ")
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination) # copy directory 
            log_action(f"Copied directory {source} to {destination}")
        else:
            shutil.copy2(source, destination) # copy file
            log_action(f"Copied file {source} to {destination}")
        print((f"Copied {source} to {destination}"))
    except Exception as e:
        print(f"Error: {e}")

