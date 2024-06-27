import student_class as student
from datetime import datetime
"""
Function to write error log file
Input: Error message
Output: none
"""
def write_to_error_log(error_message):
    try:
        #open log file
        log_file = open("error_log.txt", "a")
        #write error message to log file
        log_file.write(f"{datetime.now()}: {error_message}\n")
        #close log file
        log_file.close()
    except Exception as err:
        print(err)
        return

def load_students(file_name):
    list_of_students = []
    student_file = open(file_name, "r")
    student_file.readline()

    line_number = 1
    for line_of_data in student_file:
        line_number += 1

        #split
        student_data = line_of_data.split(",")
        #make sure line has 6 items
        try:
            if len(student_data) != 6:
                raise Exception(f"There is an error in your data file on line {line_number}\n")
        except Exception as err:
            write_to_error_log(str(err))
            continue

        #get individual values
        try:
            first_name = student_data[0]
            last_name = student_data[1]
            major = student_data[2]
            credit_hours = student_data[3]
            gpa = student_data[4]
            student_id = student_data[5]
        except Exception as err:
            write_to_error_log(f"Error: {err} on line {line_number}\n")
            continue
        
        #create student objects
        new_student = student.Student(first_name, last_name, major, credit_hours, gpa, student_id)

        #append
        list_of_students.append(new_student)

    #close file and return list
    student_file.close()
    return list_of_students

#create a function called student_to_dictionary that creates a student dictionary for each student object
#add student dictionary to a list
#function to create a list of student dictionaries
#input: list of student objects
#output: list of student dictionaries
def student_to_dictionary(list_of_students):
    list_of_student_dictionaries = []

    #loop through the list of students: for loop
    for the_student in list_of_students:
        #create a dictionary for each student object
        student_dictionary = {
            "first_name": the_student.get_first_name(),
            "last_name": the_student.get_last_name(),
            "id": the_student.get_student_id(),
            "major": the_student.get_major(),
            "credit_hours": the_student.get_credit_hours(),
            "gpa": the_student.get_gpa(),
            "class": the_student.get_class_level()
        }

        #append student dictionary to list of dictionaries
        list_of_student_dictionaries.append(student_dictionary)
    return list_of_student_dictionaries


def get_student_dictionaries():
    #load list from file
    list_of_students = load_students("student_data.csv")

    student_dictionaries = student_to_dictionary(list_of_students)

    return student_dictionaries