from bs4 import BeautifulSoup

def remove_non_ascii(text):
    """removes non-ascii characters

    Args:
        text (_type_): input string the acharacters will be removed

    Returns:
        _type_: string with ascii characters
    """
    return ''.join([char if ord(char) < 128 else '' for char in text])

def clean_xml(file_path):
    """reads and cleans xml file

    Args:
        file_path (_type_): path to xml file cleaned

    Returns:
        _type_: clean xml file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    cleaned_data = remove_non_ascii(data)
    return cleaned_data
    
def save_cleaned_xml(data, new_file_path):
    """saves new, clean xml file

    Args:
        data (_type_): _cleaned xml file
        new_file_path (_type_): path to saved xml file
    """
    with open(new_file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def employee_information(cleaned_file_path):
    """Takes employee info from clean file

    Args:
        cleaned_file_path (_type_): path to clean file 

    Returns:
        _type_: dictionary list of name, title, and profile pic path
    """
    with open(cleaned_file_path, 'r', encoding= 'utf-8') as file:
        soup = BeautifulSoup(file, 'xml')
    employees = []
    for employee in soup.find_all('employee'):
        name_elem = employee.find('emp_name')
        title_elem = employee.find('title')
        profile_pic_elem = employee.find('profile_pic')

        name = name_elem.text if name_elem else ''
        title = title_elem.text if title_elem else ''
        profile_pic = profile_pic_elem.text if profile_pic_elem else ''

        if name and title and profile_pic:
            employees.append({'name': name, 'title': title,'profile_pic': profile_pic})
        else:
            print(f"warning")

    return employees