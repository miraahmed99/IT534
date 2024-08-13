import os
import shutil
import datetime

LOG_DIR = "C:\\Python_LOG" if os.name == 'nt' else "/Python_Log" # log directory 
LOG_FILE = os.path.join(LOG_DIR, "system_log.txt") # set path 
BACKUP_DIR = "C:\\backups" if os.name == 'nt' else "/backups" # backup directory 

def log_action(action):
    """Action done on system files

    Args:
        action (string): what the script did
    """
    with open(LOG_FILE, "a") as log_file:  # open log file
        log_file.write(f"{datetime.datetime.now()}: {action}\n")

def validate_directory_path(path):
    """Validates path to make sure its valid

   

    Raises:
        ValueError: if path has '..'
        FileNotFoundError: if directory is not there
    """
    if ".." in path: # check invalid path 
        raise ValueError("Invalid directory path containing '..'")
    if not os.path.exists(path): #checks valid directory 
        raise FileNotFoundError("Directory does not exist")

def backup_target(target):
    """
    Backup file before delete 
    """
    backup_name = os.path.join(BACKUP_DIR, f"deleted_{os.path.basename(target)}") # creates backup directory
    if os.path.isdir(target):
        shutil.copytree(target, backup_name)
    else:
        shutil.copy2(target, backup_name)
    print(f"Backup up {target} to {backup_name}")
    log_action(f"Backed up {target} to {backup_name}")


