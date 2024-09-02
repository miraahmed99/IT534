import json

def save_settings(settings, file_path):
    """
    saves setting dictionary

    Args:
        settings (dict): has all configuration settings
        file_path (str): path where settings ae saved
    """
    try:
        with open(file_path, 'w') as file: #open file
            json.dump(settings, file, indent=4) # write dictionary to file
    except Exception as e:
        print(f"Error saving settings: {e}")

def load_settings(file_path):
    """
    loads setting from file and turns to dict

    Args:
        file_path (str): path from settings are loaded

    Returns:
        dictionary or nothing if error
    """
    try:
        with open(file_path, 'r') as file: #open in read
            settings = json.load(file) #read file and convert to dict
        return settings
    except Exception as e:
        print(f"Error loading settings: {e}")
        return None