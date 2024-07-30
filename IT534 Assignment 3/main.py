import xml_file
import image

def main():
    """Cleans the data, get the information, and adds the information to the images
    """
    original_xml = 'text_files/employee_data.xml' #define paths 
    cleaned_xml = 'text_files/cleaned_employee_data.xml'
    images_folder = 'images/'
    output_folder = 'images/output_files'
    font_path = 'fonts/Syne_regular.otf'

    cleaned_data = xml_file.clean_xml(original_xml) # clean and save XML
    xml_file.save_cleaned_xml(cleaned_data, cleaned_xml)

    employees = xml_file.employee_information(cleaned_xml)
    for emp in employees:
        name_title = f"{emp['name']} - {emp['title']}" #create text for image
        original_image_path = f"{images_folder}{emp['profile_pic']}"
        output_image_path = f"{output_folder}{emp['profile_pic']}"
        image.add_text(original_image_path, output_image_path, name_title, font_path, position=(10,10))

if __name__ == "__main__":
    main()
