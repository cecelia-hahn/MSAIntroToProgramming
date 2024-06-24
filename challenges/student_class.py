#class and file must be named the same thing
#create student class
class Student():
    #define constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        #class property values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = int(credit_hours)
        self.__gpa = float(gpa)
        self.__student_id = int(student_id)

    #get/set methods
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_fname):
        self.__first_name = new_fname
    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_lname):
        self.__last_name = new_lname
    
    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        try:
            self.__major = str(new_major)
        except:
            print("Error: Enter the name of a major\n")
    
    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, additional_hours):
        try:
            self.__credit_hours += int(additional_hours)
        except:
            print("Error: Additional credit hours must be a whole number\n")

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        try:
            self.__gpa = float(new_gpa)
        except:
            print("Error: Must enter a number\n")

    def get_student_id(self):
        return self.__student_id
    
    #get grade level hours
    def get_class_level(self):
        if self.__credit_hours >= 0 and self.__credit_hours <= 30:
            class_level = "Freshman"
            return class_level
        if self.__credit_hours >= 31 and self.__credit_hours <=60:
            class_level = "Sophomore"
            return class_level
        if self.__credit_hours >=61 and self.__credit_hours <= 90:
            class_level = "Junior"
            return class_level
        if self.__credit_hours > 90:
            class_level = "Senior"
            return class_level
        else:
            print("Error: Invalid credit hour input")

    #print student info
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}: {self.__major}")
        print(f"{self.__credit_hours} credit hours, GPA: {self.__gpa}, Grade Level: {self.get_class_level()}")
        print(f"Student ID: {self.__student_id}\n")