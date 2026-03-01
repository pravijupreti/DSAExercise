# CHAPTER 6 EXERCISE 1
'''
Student Grade Lookup (Dictionary) Exercise

A teacher wants a quick way to store and look up student grades.

Create a program that:
- Stores student names and grades in a dictionary
- Lets the user choose from multiple actions:
    add/update a grade
    search a student’s grade
    print all students and grades
    loop until they select 0 (zero)

- If the student is not found, print a message

Example data
"Anna": 5
"Mikko": 4
"Sara": 3

'''

# Hint! Use a dictionary and while loop for example!

student = {}

def student_Add(name, grade):
    """Add a new student to the database"""
    student[name] = grade

def add_students():
    """Function to add multiple students"""
    print("Enter first student Name then their grade")
    while True:
        student_name = input("Enter the student name (or 0 to exit): ")
        if student_name == "0":
            break
        else:
            student_grade = input("Enter student grade: ")
            try:
                student_grade = int(student_grade)
                student_Add(student_name, student_grade)
                print(f"Student {student_name} added successfully!")
            except ValueError:
                print("Please enter student grade as an integer")

def student_Look_Up():
    """Look up a student's grade"""
    while True:
        student_Name = input("Enter the student Name to check their grade (or 0 to exit): ")
        if student_Name == "0":
            break
        else:
            if student_Name in student:
                print(f"Grade of {student_Name} is {student[student_Name]}")
            else:
                print(f"Student with name {student_Name} not found in the database")

def student_dict_update():
    """Update an existing student's grade"""
    while True:
        student_name = input("Enter the student name to update their grade (or 0 to exit): ")
        if student_name == "0":
            break
        else:
            if student_name in student:
                try:
                    student_New_Grade = int(input("Enter the student new grade: "))
                    student[student_name] = student_New_Grade
                    print(f"Grade for {student_name} updated successfully!")
                except ValueError:
                    print("Student Grade must be an integer")
            else:
                print(f"Student with name {student_name} not found in the database")


add_students()
    
print("\nCurrent Student Database:")
print(student)
    

print("\n--- Student Look Up ---")
student_Look_Up()
    

print("\n--- Update Student Grades ---")
student_dict_update()
    

print("\nUpdated Student Database:")
print(student)

