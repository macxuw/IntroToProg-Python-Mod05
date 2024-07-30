# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   MClark,7/28/2024,Updated constants and variables, dictionary read, menu choices
# ------------------------------------------------------------------------------------------ #

# Import JSON module

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ""  # Hold the choice made by the user.

try:
    # Extract the data from the file
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
# Check for errors
except FileNotFoundError as e:
    # If file not found, create
    print("This script requires an existing text file! Initializing file.\n")
    file = open(FILE_NAME, "w")
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Make sure file is closed
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name.isalpha() or len(student_first_name) < 2:
                raise ValueError("First name should only contain letters and be at least 2 characters.")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name.isalpha() or len(student_last_name) < 2:
                raise ValueError("Last name should only contain letters and be at least 2 characters.")

            course_name = input("Please enter the name of the course: ").strip()
            if not len(course_name) > 2:
                raise ValueError("Course name must be at least 3 characters.")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
            students.append(student_data)
        # If inputs do not meet criteria, display error
        except ValueError as e:
            print(e)  # Print custom message
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            # Save table in a readable format
            json.dump(students, file, indent=1)
            file.close()
            print("Data saved.")
            continue
        except TypeError as e:
            print("File save error.\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please choose a number from the menu.")

print("Program Ended")
