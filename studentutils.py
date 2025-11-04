from student import Student
from csvutils import save_to_csv
class StudentUtils:
    def __init__(self, students=None):
        self.students = students if students is not None else []
        self.file_path = "data/students.csv"

    def add_new_student(self, student: Student):
        self.students.append(student)
        self.save()
    def check_my_marks (self,  student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s.marks
    def display_records(self):
        for s in self.students:
            print(s)

    def find_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None
    def check_my_grade(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s.grade
    def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
        self.save()
    def modify_student_details(self, student_id = None, first_name=None, last_name=None, course_id=None, grade=None, marks=None, email_address=None ):
        for s in self.students:
            if s.student_id == student_id:
                if first_name is not None:
                    s.first_name = first_name
                if last_name is not None:
                    s.last_name = last_name
                if course_id is not None:
                    s.course_id = course_id
                if grade is not None:
                    s.grade = grade
                if marks is not None:
                    s.marks = marks
                if email_address is not None:
                    s.email_address = email_address
        self.save()

    def sorted_by_name(self):
        return sorted(self.students, key=lambda s: (s.first_name, s.last_name))

    def sorted_by_marks(self, reverse=True):
        return sorted(self.students, key=lambda s: s.marks, reverse=reverse)

    def save(self):
        save_to_csv(
            self.file_path,
            self.students,
            fieldnames=[
                "Student_id",
                "Email_address",
                "First_name",
                "Last_name",
                "Course.id",
                "grades",
                "Marks"
            ]
        )
