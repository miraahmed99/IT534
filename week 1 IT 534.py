class Person():

    def __init__(self, name, email):   #initializes person class
        self.name = name #assigns name
        self.email = email #assigns email

    def display_information(self): #print statements for name and email
        print("Name: " + self.name)
        print("Email: " + self.email)


class Student(Person):

    def __init__(self, name, email, student_id, program):
        super().__init__(name, email)
        self.student_id = student_id #assigns student ID
        self.program = program #assigns program

    def display_information(self): #print statement for program and student ID
        print("Program: " + self.program)
        print("Student ID: " + self.student_id)


class Instructor(Person): #class for instructor
    def __init__(self, name, email, instructor_id, degree, institution):
        super().__init__(name, email)
        self.instructor_id = instructor_id #assigns instructor id
        self.degree = degree #assigns degree
        self.institution = institution # assigns institution

    def display_information(self):
        super().display_information()
        print("Instructor ID: " + self.instructor_id)
        print("Degree: " + self.degree)
        print("Institution: " + self.institution)


class Validator():

    def __init__(self):
        self.invalid_name_character = set('!"@#$%^&*()_+=.<.>/?;:[]{}\\') #invalid characters for name
        self.invalid_email_character = set('!"#$%^&*()_+=<>/?;:[]{}\\') #invalid characters for email

    def validate_name(self, name):
        if not name or any(char in self.invalid_name_character for char in name) or not name.replace(" ", "").isalpha(): # if statement for invalid name
            print("Invalid Name")
            return False
        return True

    def validate_email(self, email):
        if not email or any(char in self.invalid_email_character for char in email) or not email.replace(".", "").replace("@",
                                                                                                                 "").isalnum(): #print statement for invalid email
            print("Invalid Email")
            return False
        return True

    def validate_user_type(self, user_type):
        if user_type.lower() in ['s', 'i']:
            return True
        else:
            print("The provided user type is invalid")
            return False

    def validate_student_id(self, student_id):
        if student_id.isdigit() and len(student_id) <= 7:
            return True
        else:
            print("The provided student ID is invalid")
            return False

    def validate_instructor_id(self, instructor_id):
        if instructor_id.isdigit() and len(instructor_id) <= 5:
            return True
        else:
            print("The provided instructor ID is invalid")
            return False

    def validate_value(self, value):
        if value:
            return True

        else:
            print("You must provide a value")
            return False


college_records = []
my_validator = Validator()

while True:

    ind_type_valid = False
    while not ind_type_valid:
        ind_type = input("Are you a Student or Instructor? Type: 'S' or 'I' ").strip()
        ind_type_valid = my_validator.validate_user_type(ind_type)

    name_valid = False
    while not name_valid:
        your_name = input("Enter your name: ").strip()
        name_valid = my_validator.validate_name(your_name)

    email_valid = False
    while not email_valid:
        your_email = input("Enter your email: ").strip()
        email_valid = my_validator.validate_email(your_email)

    if ind_type.lower() == "s":
        ind_id_valid = False
        while not ind_id_valid:
            your_id = input("Enter your Student ID: ").strip()
            ind_id_valid = my_validator.validate_student_id(your_id)

        ind_program_valid = False
        while not ind_program_valid:
            your_program = input("Enter your Program of Study: ").strip()
            ind_program_valid = my_validator.validate_value(your_program)

        student = Student(your_name, your_email, your_id, your_program)
        college_records.append(student)

    else:
        ind_id_valid = False
        while not ind_id_valid:
            your_id = input("Enter your Instructor ID: ").strip()
            ind_id_valid = my_validator.validate_instructor_id(your_id)

        ind_degree_valid = False
        while not ind_degree_valid:
            your_degree = input("Enter your Highest Degree: ").strip()
            ind_degree_valid = my_validator.validate_value(your_degree)

        ind_institution_valid = False
        while not ind_institution_valid:
            your_institution = input("Enter the Last Instiution you Graduated from: ").strip()
            ind_institution_valid = my_validator.validate_value(your_institution)

        instructor = Instructor(your_name, your_email, your_id, your_degree, your_institution)
        college_records.append(instructor)

    cont = input("Would you like to add another record (Y/N)? ").strip().lower()
    if cont == "n":
        break

for record in college_records:
    record.display_information()