import csv

class Student:
    def __init__(self, student_id, first_name, last_name, course_id, grade, marks, email_address):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.marks = marks
        self.student_id = student_id
        self.email_address = email_address

    def to_dict(self):
        return {
            "First_name": self.first_name,
            "Last_name": self.last_name,
            "Course.id": self.course_id,
            "grades": self.grade,
            "Marks": self.marks,
            "Student_id": self.student_id,
            "Email_address": self.email_address
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["First_name"],
            last_name=data["Last_name"],
            course_id=data["Course.id"],
            grade=data["grades"],
            marks=float(data["Marks"]),
            student_id=data["Student_id"],
            email_address = data["Email_address"]
        )

    def __str__(self):
        return f"{self.student_id} {self.first_name} {self.last_name} ({self.course_id}) - Grade: {self.grade}, Marks: {self.marks}"


csv