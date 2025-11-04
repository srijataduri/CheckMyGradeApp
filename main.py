from csvutils import load_from_csv, save_to_csv
from student import Student
from course import Course
from prof import Professor
from account import Account
from studentutils import StudentUtils
from courseutils import CourseUtils
from profutils import ProfessorUtils
from accountutils import AccountUtils

STUDENTS_CSV = "data/students.csv"
COURSES_CSV = "data/courses.csv"
PROFESSORS_CSV = "data/professors.csv"
ACCOUNTS = "data/login.csv"

def load_data():
    students = load_from_csv(STUDENTS_CSV, Student)
    courses = load_from_csv(COURSES_CSV, Course)
    professors = load_from_csv(PROFESSORS_CSV, Professor)
    accounts = load_from_csv(ACCOUNTS, Account)
    print('Load data from CSV successfully')
    return (
        StudentUtils(students),
        CourseUtils(courses),
        ProfessorUtils(professors),
        AccountUtils(accounts)
    )

student_utils, courses_utils, professors_utils, account_utils = load_data()

def student_input():
    print("\nEnter student details:")
    student_id = input("Student ID: ").strip()
    email_address = input("Email Address: ").strip()
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    course_id = input("Course ID: ").strip()
    grade = input("Grade: ").strip()
    try:
        marks = int(input("Marks: ").strip())
    except ValueError:
        marks = 0
    return Student(
        student_id=student_id,
        email_address=email_address,
        first_name=first_name,
        last_name=last_name,
        course_id=course_id,
        grade=grade,
        marks=marks
    )
def course_input():
    print("\nEnter course details:")
    course_id = input("Course ID: ").strip()
    course_name = input("Course Name: ").strip()
    description = input("Description: ").strip()
    return Course(course_id, course_name, description)

current_user = None

def is_logged_in():
    return current_user is not None

def require_login():
    if not is_logged_in():
        print("You must be logged in to perform this action.")
        return False
    return True

def _menu():
    global current_user
    while True:
        print('--- Menu ---')
        print('1) Add new student')
        print('2) Delete student')
        print('3) Display student records')
        print('4) Save student details')
        print('5) Check my marks')
        print('6) Display ALL courses')
        print('7) Add new course')
        print('8) Delete course')
        print('9) Display ALL professors')
        print('10) Show professor→course details')
        print("11) Login")
        print("12) Logout")
        print('0) Exit')
        choice = input('Choose an option: ').strip()

        if choice == "1":
            if not require_login():
                continue
            new_student = student_input()
            student_utils.add_new_student(new_student)
            print("Student added successfully!")
        elif choice == "2":
            if not require_login():  # protect write
                continue
            student_id = input("Enter Student ID to delete: ").strip()
            student_utils.delete_student(student_id)
            print("Student deleted successfully!")
        elif choice == "3":
            print("\n--- Student Records ---")
            student_utils.display_records()
            print("Displayed all student records successfully!")
        elif choice == "4":
            if not require_login():  # protect write
                continue
            student_utils.save()
            print("Student details saved successfully to CSV!")
        elif choice == "5":
            student_id = input("Enter Student ID to check marks: ").strip()
            marks = student_utils.check_my_marks(student_id)
            if marks is not None:
                grade = student_utils.check_my_grade(student_id)
                print(f"Student ID: {student_id} | Marks: {marks} | Grade: {grade}")
                print("Marks and grade retrieved successfully!")
            else:
                print("Student not found.")
        elif choice == "6":
            if not require_login():  # protect write
                continue
            new_course = course_input()
            courses_utils.add_new_course(new_course)
            print("Course added successfully!")
        elif choice == "7":
            if not require_login():  # protect write
                continue
            course_id = input("Enter Course ID to delete: ").strip()
            courses_utils.delete_course(course_id)
            print("Course deleted successfully!")
        elif choice == "8":
            print("\n--- All Courses ---")
            courses_utils.display_records()
            print("Displayed all courses successfully!")
        elif choice == "9":
            print("\n--- All Professors ---")
            professors_utils.display_records()
            print("Displayed all professors successfully!")
        elif choice == "10":
            print("\n--- Professor → Course Details ---")
            professors_utils.show_course_detalis_by_prof()
            print("Displayed professor-course details successfully!")
        elif choice == "11":
            if is_logged_in():
                print("Already logged in.")
                continue
            email = input("Email: ").strip()
            password = input("Password: ").strip()
            ok = account_utils.login(email, password)
            if ok:
                current_user = ok if ok is not True else {"email": email}
                print("Logged in successfully!")
            else:
                print("Invalid credentials.")
        elif choice == "12":
            if not is_logged_in():
                print("You are not logged in.")
            else:
                current_user = None
                print("Logged out successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    _menu()

