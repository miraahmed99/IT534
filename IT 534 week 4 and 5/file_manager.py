import os
import argparse
from basic_mode import basic_mode
from elevated_mode import elevated_mode
from admin_mode import admin_mode
from utils import log_action, validate_directory_path

def parse_arguments():
    """File management script

    Returns:
        tuple: contains whether basic, eleavated, or admin
    """
    parser = argparse.ArgumentParser(description= "File Management Script") # creates arhument for script
    parser.add_argument('-m', '--mode', required= True, choices= ['basic', 'elevated', 'admin'], help = 'Mode to runn the script in')
    parser.add_argument('-d', '--directory', help= 'Directory path to browse files') # directory argument
    args = parser.parse_args() # return arguements
    return args.mode, args.directory

def main():
    mode, directory = parse_arguments()
    if directory:
        validate_directory_path(directory) # validate and change directory 
        os.chdir(directory)
    else:
        directory = os.getcwd() # if no directory, use current directory 
    print(f"Running in {mode} mode")
    print(f"Current Directory: {directory}")

    if mode == 'basic': # executed user choice of mode
        basic_mode()
    elif mode == 'elevated':
        elevated_mode()
    elif mode == 'admin':
        admin_mode()
    else:
        print('Bad mode')
if __name__ == "__main__":
    main()