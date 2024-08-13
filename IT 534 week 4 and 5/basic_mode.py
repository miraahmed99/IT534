import os
from utils import log_action, validate_directory_path

def basic_mode():
    """
    Runs the basic mode with a menu
    """
    while True: # input for basic menu 
        print("\nBasic Mode Menu:")
        print("1. Change Directory")
        print("2. List Directory Contents")
        print("3. Exit")

        choice = input("Enter Choice: ")
        if choice == '1':
            change_directory()
        elif choice == '2':
            list_dictionary_contents()
        elif choice == '3':
            break
        else:
            print("Invalid")

def change_directory():
    """
    Changes the directory and logs action if it works
    """
    new_dir = input("enter the directory to change to: ") # new directory 
    try:
        validate_directory_path(new_dir)
        os.chdir(new_dir) # changes directory 
        print(f"Changed directory to: {new_dir}")
        log_action(f"Changed directory to: {new_dir}")
    except Exception as e:
        print(f"Error: {e}")

def list_dictionary_contents():
    """
    Lists whats in the current directory thats being viewed such as the valuable information and logs if it worked or failed
    """
    current_dir = os.getcwd() # gets working directory 
    print(f"Contents of directory: {current_dir}")
    try:
        with os.scandir(current_dir) as it:
            for entry in it:
                if entry.is_dir():
                    print(f"[Dir] {entry.name}") # prints directory names
                else:
                    print(f"[File] {entry.name} - {entry.stat().st_size} bytes") # prints file names and size
        log_action(f"Listed contents of directory: {current_dir}")
    except Exception as e:
        print(f"Error: {e}")
