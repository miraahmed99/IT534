import os
import shutil
from utils import log_action, validate_directory_path, backup_target
from basic_mode import change_directory, list_dictionary_contents
from elevated_mode import copy_file_or_directory

def admin_mode():

    """
    runs admin and helps create a menue
    """
    while True: # shows menu options for admin 
        print("\nBasic Mode Menu:")
        print("1. Change Directory")
        print("2. List Directory Contents")
        print("3. Copy File/Directory")
        print("4. Move File/Directory")
        print("5. Delete File/Directory")
        print("6. Exit")

        choice = input("Enter Choice: ") # input for choice of menu 
        if choice == '1':
            change_directory()
        elif choice == '2':
            list_dictionary_contents()
        elif choice == '3':
            copy_file_or_directory()
        elif choice == '4':
            move_file_or_directory()
        elif choice == '5':
            delete_file_or_directory()
        elif choice == '6':
            break
        else:
            print("Invalid")

def move_file_or_directory():
    """moves file or directory to a new location and shows the source path
    """

    source = input("Enter source path: ") # wants source 
    destination = input(" Enter the destination path: ") # wants destination 
    try:
        shutil.move(source, destination) # moves file or directory
        log_action(f"Moved {source} to {destination}") # logs if successful
        print(f"Moved {source} to {destination}")
    except Exception as e:
        print(f"Error: {e}")

def delete_file_or_directory():
    """deletes the file or directory, helps delete target path 
    """
    target = input("Enter path to delete: ") # where target path is deleted
    try:
        backup_target(target)
        if os.path.isdir(target):
            shutil.rmtree(target)
            log_action(f"Deleted directory {target}")
        else:
            os.remove(target) # deletes file
            log_action(f"Deleted file {target}")
        print(f"Deleted {target}")
    except Exception as e:
        print(f"Error: {e}")